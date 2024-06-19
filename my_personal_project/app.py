#نحلیل عکس چهره یک شخص با هوش مصنوعی
#https://github.com/serengil/deepface
import os
from flask import Flask, render_template,request,redirect,session , url_for
from deepface import DeepFace
from sqlmodel import  Session, select, create_engine, SQLModel
from user_database import User
from base_model import RegisterModel , LoginModel
import bcrypt
from imread_from_url import imread_from_url
from ONNX.yolov8 import YOLOv8
import cv2

app = Flask("Analyze Face")
app.config["UPLOAD_FOLDER"] = 'uploads'
app.config["ALLOWED_EXTENSION"] = {'png',"jpg",'jpeg'}



engine = create_engine('sqlite:///./database.db' ,echo=True )
SQLModel.metadata.create_all(engine)

#pydantic models for request validation



# def auth(email, password):
#     if email =="morteza@yahoo.com" and password == "moricyber":
#         return True
#     else:
#         return False
def allowed_file(filname):
    return True



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method =="GET":
        return render_template("login.html")
    
    elif request.method == "POST":
        try:
               login_model =  LoginModel(
                username = request.form["username"],
                password = request.form["password"],
                confirm_password = request.form["confirmpassword"]
                )
               
        except:
            print('Type Error')
            return redirect(url_for('login'))
        
        with Session(engine) as db_session:
            statment = select(User).where(User.username == login_model.username)
            result = db_session.exec(statment).first()

        if result:
            password_byte = login_model.password.encode("utf-8")
            confirm_password=login_model.confirm_password.encode("utf-8")
            if bcrypt.checkpw( password_byte , result.password) and bcrypt.checkpw(confirm_password,result.password):
        
                print("Wellcome, you are logged in ")
                return redirect(url_for("upload"))
            else:
                print("pssword is  incorrect")
                return redirect(url_for("login"))
        else:
            print("username is incorrect")
            return redirect(url_for("login"))
        

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        try:
                register_data = RegisterModel(first_name=request.form["firstname"], 
                                              last_name = request.form["lastname"],
                                               email = request.form["email"],
                                               age = request.form["age"],
                                               country = request.form["country"],
                                                join_time = request.form["join_time"],
                                                city=request.form["city"],
                                                username = request.form["username"], 
                                                password = request.form["password"],                      
                                                
                            
                                      )
        except:
            print("type error")
            return redirect(url_for("register"))
        
        with Session(engine) as db_session:
            statment = select(User).where(User.username == register_data.username)
            result =db_session.exec(statment).first()
        if not result:
            pass_byte = register_data.password.encode("utf-8")
            pass_hashed = bcrypt.hashpw(pass_byte , bcrypt.gensalt())
            with Session(engine) as db_session:
                user = User(
                   first_name= register_data.first_name,
                   last_name= register_data.last_name,
                   email= register_data.email,
                    age= register_data.age,
                    country= register_data.country,
                    join_time=register_data.join_time,
                    city = register_data.city,
                    username = register_data.username,
                    password=pass_hashed
                )
                db_session.add(user)
                db_session.commit()
                print("Your register done succssesfuly")
                return redirect(url_for("login"))
        else:
            print('username already exist, Try another username')    
            return redirect(url_for("register"))



@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    elif request.method == "POST":
        my_image = request.files["image"]
        if my_image.filename == "":
            return redirect(url_for("upload"))
            
        else:
            if my_image and allowed_file(my_image.filename):
                save_path = os.path.join(app.config["UPLOAD_FOLDER"], my_image.filename)
                my_image.save(save_path)
                file = open(save_path , "r", encoding='UTF-8')

                model_path = ""ONNX/yolov8/.env/yolov8m.onnx""
                yolov8_detector = YOLOv8(model_path, conf_thres=0.2, iou_thres=0.3)

                try:
                    
                    img= cv2.imread(file.name)
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    
                    boxes, scores, class_ids = yolov8_detector(img)

                    combined_img = yolov8_detector.draw_detections(img)
                    cv2.imwrite("static/images/img.jpg", combined_img)
                    print("Image processed and saved.")
                except Exception as e:
                    print(f"Error processing image: {e}")
                    return redirect(url_for("upload"))

                return render_template("result.html", combined_img="static/images/img.jpg")
            else:
                print("File type not allowed.")
                return redirect(url_for("upload"))
