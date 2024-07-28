
#https://github.com/serengil/deepface
import os
from flask import Flask, render_template,request,redirect,session as flask_session, url_for, flash
from sqlmodel import  Session, select, create_engine, SQLModel
from user_database import User , Comment
from base_model import RegisterModel , LoginModel
import bcrypt
from ONNX.yolov8 import YOLOv8
import cv2
from datetime import datetime
from dateutil import parser
import humanize

def get_relative_time(datetime_str):
    # Parse the datetime string to a datetime object
    input_datetime = parser.parse(datetime_str)
    # Get the current time
    current_datetime = datetime.now()
    # Calculate the difference between the current time and the input datetime
    time_difference = current_datetime - input_datetime
    # Return the human-readable relative time
    return humanize.naturaltime(time_difference)


app = Flask("Analyze Face")
app.config["UPLOAD_FOLDER"] = 'uploads'
app.secret_key = 'your_secret_key'


DATABASE_URL = "postgresql://admin123:mori_cyber@ai_postgres:8080//db_postgres"
# DATABASE_URL = 'sqlite:///./database.db'
engine = create_engine(DATABASE_URL  ,echo=True )
SQLModel.metadata.create_all(engine)


def allowed_file(filname):
    return True



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signin", methods = ["GET","POST"])
def signin():
    if request.method =="GET":
        return render_template("signin.html")
    
    elif request.method == "POST":
        try:
               login_model =  LoginModel(
                username = request.form["username"],
                password = request.form["password"],
                confirm_password = request.form["confirmpassword"]
                )
               
        except:
            flash('Type Error', "info")
            return redirect(url_for('signin'))
        
        with Session(engine) as db_session:
            statment = select(User).where(User.username == login_model.username)
            user = db_session.exec(statment).first()

        if user:
            password_byte = login_model.password.encode("utf-8")
            confirm_password=login_model.confirm_password.encode("utf-8")
            if bcrypt.checkpw( password_byte , user.password) and bcrypt.checkpw(confirm_password,  user.password):
                
                flash("Wellcome, you are signed in", "success")
                flask_session["user_id"] = user.id
                return redirect(url_for("upload"))
            else:
                flash("pssword is  incorrect", "danger")
                return redirect(url_for("signin"))
        else:
            flash("username is incorrect", "warning")
            return redirect(url_for("signin"))
        

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        try:
                register_data = RegisterModel(first_name=request.form["firstname"], 
                                              last_name = request.form["lastname"],
                                               email = request.form["email"],
                                               age = request.form["age"],
                                               country = request.form["country"],
                                                city=request.form["city"],
                                                username = request.form["username"], 
                                                password = request.form["password"],  
                                                confirm_password = request.form["confirmpassword"]
                                                
                            
                                      )
        except:
            flash("type error", "warning")
            return redirect(url_for("signup"))
        
        with Session(engine) as db_session:
            statment = select(User).where(User.username == register_data.username)
            result =db_session.exec(statment).first()
        if not result:
            pass_byte = register_data.password.encode("utf-8")
            pass_hashed = bcrypt.hashpw(pass_byte , bcrypt.gensalt())
            confirn_pass = bcrypt.hashpw(pass_byte , bcrypt.gensalt())
            
            with Session(engine) as db_session:
                user = User(
                   first_name= register_data.first_name,
                   last_name= register_data.last_name,
                   email= register_data.email,
                    age= register_data.age,
                    country= register_data.country,
                    join_time=datetime.now(),
                    city = register_data.city,
                    username = register_data.username,
                    password=pass_hashed,
                    confirm_password = confirn_pass
                )
                db_session.add(user)
                db_session.commit()
                flash("Your register done succssesfuly", "success")
                return redirect(url_for("signin"))
        else:
            flash('username already exist, Try another username',"danger")    
            return redirect(url_for("signup"))


@app.route("/signout")
def signout():
    flask_session.pop("user_id")
    return redirect(url_for("index"))



@app.route("/upload", methods=["GET", "POST"])
def upload():
    if flask_session.get('user_id'):
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

                        model_path = "ONNX/yolov8/yolov8m.onnx"
                        
                        yolov8_detector = YOLOv8(model_path, conf_thres=0.2, iou_thres=0.3)
                        
                        try:
                            
                            img= cv2.imread(file.name)
                            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                            
                            boxes, scores, class_ids = yolov8_detector(img)

                            combined_img = yolov8_detector.draw_detections(img)
                            cv2.imwrite("static/images/img.jpg", combined_img)
                            flash("Image processed and saved", "info")
                        except Exception as e:
                            print(f"Error processing image: {e}", "danger")
                            return redirect(url_for("upload"))

                        return render_template("result.html", combined_img ="static/images/img.jpg")
                    else:
                        flash("File type not allowed.", "warning")
                        return redirect(url_for("upload"))
    else:
        return redirect(url_for("index"))
    
@app.route("/read-your-mind" , methods=["GET","POST"])
def read_your_mind():
    if request.method=="POST":
        x = request.form["number"]    
        return redirect(url_for('read_your_mind_result', number=x))
    return render_template("read-your-mind.html")

@app.route('/read-your-mind/result')
def read_your_mind_result():
    y = request.args.get("number")
    return render_template("read-your-mind-result.html", number=y)

@app.route("/admin")
def admin():
    # user_id = flask_session.get("user_id")
    # role = flask_session.get("role")
    # if not user_id or role !="Admin":
    #     return redirect(url_for("login.html"))
    with Session(engine) as db_session:
            statment = select(User)
            users = list(db_session.exec(statment))

    for user in users:
        user.join_time = get_relative_time( user.join_time)

    return render_template("admin.html", users = users)


@app.route("/add-new-comment", methods=["POST"])
def add_new_comment():
    text = request.form["text"]
    user_id = flask_session.get("user_id")
    
    with Session(engine) as db_session:
        # Fetch the user's name
        user = select(User)
        user = db_session.query(User).filter(User.id == user_id).first()
        
        if user:
            # Add the new comment
            new_comment = Comment(
                user_id=user_id,
                content=text
            )
            db_session.add(new_comment)
            db_session.commit()
            
              # Flash the user's name and message content
            flash(f'Message from {user.first_name}: {new_comment.content}', 'success')
        else:
                flash('User not found', 'error')
        
        return redirect(url_for('upload'))
    
    return render_template('upload.html')