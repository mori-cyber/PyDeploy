from flask import Flask, request, jsonify
from mongoengine import *
import bcrypt
import jwt
import datetime
from functools import wraps
from pydantic import BaseModel
import pandas as pd 
# Additional Imports
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
# from sklearn.utils import FloatTensorType
import torch
import onnx
import onnxmltools
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
import pandas as pd  
import onnxruntime as rt
import joblib
import os

MODEL_PATH = 'model.onnx'


app = Flask(__name__)
# bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = 'your_secret_key'

# Connect to MongoDB
connect(host='mongodb+srv://mongo_admin:mongo123@user.sdmm2.mongodb.net/')

class LoginModel(BaseModel):
    username: str
    password: str
    # confirm_password: str

class RegisterModel(BaseModel):
    password:  str
    confirm_password: str
# MongoDB User Model
class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    confirm_password = StringField(required=True)
    

# MongoDB House Model
class House(Document):
    price = FloatField(required=True)
    sqft = FloatField(required=True)
    bedrooms=FloatField(required=True)
    bathroom=FloatField(required=True)
    offers =FloatField(required=True)
    
    

# Helper function for token validation
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({"message": "Token is missing!"}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.objects(username=data['user']).first()
            if not current_user:
                return jsonify({"message": "User not found!"}), 403
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired!"}), 403
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token!"}), 403
        return f(current_user, *args, **kwargs)
    return decorated

@app.route("/")
def root():
    return {"hello":"world"}

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get("username")
    

    register_data = RegisterModel(password = data.get("password"),
                                  confirm_password=data.get("confirm_password"))
    
    if register_data.password != register_data.confirm_password:
        return jsonify(False), 400
    
    pass_byte = register_data.password.encode("utf-8")
    password_hash = bcrypt.hashpw(pass_byte , bcrypt.gensalt())
    confirm_password = bcrypt.hashpw(pass_byte , bcrypt.gensalt())
    user = User(username=username, password=password_hash, confirm_password = confirm_password)
    try:
        user.save()
        return jsonify(True)
    except:
        return jsonify(False), 400

@app.route('/signin', methods=['POST'])
def signin():
    data = request.json
    try:
        # Validate and parse input data
        login_model = LoginModel(**data)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

    user = User.objects(username=login_model.username).first()
    if user and bcrypt.checkpw(login_model.password.encode("utf-8"), user.password.encode("utf-8")):
        token = jwt.encode(
            {'user': login_model.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
            app.config['SECRET_KEY'], algorithm="HS256"
        )
        return jsonify({'token': token}), 200
    
    return jsonify({"message": "Invalid username or password!"}), 401



@app.route('/add', methods=['POST'])
@token_required
def add_house(current_user):
    # Check if the request contains a file
    if 'file' in request.files:
        file = request.files['file']

        # Ensure the file is a CSV
        if file and file.filename.endswith('.csv'):
            try:
                # Read the CSV file into a DataFrame
                df = pd.read_csv(file)
                df.to_csv('house_price.csv', index=False)
                # Iterate over the DataFrame rows and save each house
                for _, row in df.iterrows():
                    

                    # Home = row.get('Home')
                    Price = row.get('Price')
                    SqFt = row.get('SqFt')
                    Bedrooms = row.get('Bedrooms')
                    Bathrooms = row.get('Bathrooms')
                    Offers = row.get('Offers')
                    
                    print()
                    if Price and SqFt and Bedrooms and Bathrooms and	Offers  is not None:
                        house = House(price=Price, sqft = SqFt,
                                      bedrooms=Bedrooms, bathroom=Bathrooms,offers =Offers)
                        house.save()

                return jsonify({'message': 'Houses added successfully'}), 201
            except Exception as e:
                print(e , row)  # Log the error if needed
                return jsonify({'error': 'Failed to process the CSV file'}), 500 

    # If no file, process JSON data as before
    data = request.json
    features = data.get("features")
    price = data.get("price")

    if features and price is not None:
        house = House(features=features, price=price)
        try:
            house.save()
            return jsonify(True), 201
        except Exception as e:
            print(e)  # Log the error if needed
            return jsonify(False), 500

    return jsonify(False), 400


@app.route('/train', methods=['GET'])
@token_required
def train_model(current_user):
    # Fetch dataset from MongoDB
    houses = House.objects()
    data = {
        'price': [house.price for house in houses],
        'sqft': [house.sqft for house in houses],
        'bedrooms': [house.bedrooms for house in houses],
        'bathroom': [house.bathroom for house in houses],
        'offers': [house.offers for house in houses]
    }
    
    df = pd.DataFrame(data)

    # Split the dataset
    X = df[['sqft', 'bedrooms', 'bathroom', 'offers']]
    y = df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model (e.g., RandomForestRegressor)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate and save the model as ONNX
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print("Mean Squared Error:", mse)
    
    initial_types = [("float_input", FloatTensorType([None, 4]))]
    onnx_model = convert_sklearn(model, initial_types=initial_types)
    
    # Convert and save the model in ONNX format
    # onnx_model = convert_sklearn(model, initial_types=[("float_input", torch.FloatTensor([None, 4]))])
    with open(MODEL_PATH, "wb") as f:
        f.write(onnx_model.SerializeToString())
    
    return jsonify({"message": "Model trained and saved to ONNX", "mse": mse}), 200

@app.route('/predict', methods=['POST'])
@token_required
def predict(current_user):
    data = request.json
    sqft = data.get("sqft")
    bedrooms = data.get("bedrooms")
    bathroom = data.get("bathroom")
    offers = data.get("offers")

     # Validate input data
    if not all([sqft, bedrooms, bathroom, offers]):
        return jsonify({"error": "Missing input data"}), 400

    try:
        # Convert inputs to the expected data type
        input_data = [[float(sqft), float(bedrooms), float(bathroom), float(offers)]]

        # Load ONNX model and perform inference
        session = rt.InferenceSession(MODEL_PATH)
        
        # Prepare input data
        input_name = session.get_inputs()[0].name
        prediction = session.run(None, {input_name: input_data})[0]
        
        # Convert prediction to a JSON-serializable format
        prediction_value = prediction[0].item()  # Extracts as a Python scalar (float/int)
        
        return jsonify({"prediction": prediction_value}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
