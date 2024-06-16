#نحلیل عکس چهره یک شخص با هوش مصنوعی
#https://github.com/serengil/deepface
import os
from flask import Flask, render_template,request,redirect,session , url_for
from deepface import DeepFace
import cv2
import user_database


app = Flask("Analyze Face")
app.config["UPLOAD_FOLDER"] = './uploads'
app.config["ALLOWED_EXTENSION"] = {'.png',".jpg",'.jpeg'}



def allowed_file(filname):
    postfix = app.config["ALLOWED_EXTENSION"]
    a_filename = list(postfix)
    _, extension = os.path.splitext(filname)
    if extension == a_filename[0] or extension == a_filename[1] or extension == a_filename[2]:
        return True
    else:
        return False



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method =="GET":
        return render_template("login.html")
    
    elif request.method == "POST":
        my_email = request.form["email"]
        my_password = request.form["password"]
        user_verify = user_database.auth(my_email, my_password)
        ai_classes =request.form["ai_class"]
        if user_verify and ai_classes:
            if ai_classes == '0':
                return redirect(url_for("bmr"))
            elif ai_classes == '1':
                return redirect(url_for("upload"))
        else:
            #Register
            message = " Surry! This user has not been found, please first register your info and insert ai_classes"
            return render_template("login.html", message=message)

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    
    elif request.method == "POST":
        my_image = request.files["image"]
        if my_image.filename == "" or allowed_file(my_image.filename) == False:
            text = "Warning: This file is not valid, only(.jpg , .png , .jpeg)"
            return render_template("upload.html", text=text)
            
        else:
            if my_image and allowed_file(my_image.filename):
                save_path= os.path.join(app.config["UPLOAD_FOLDER"], my_image.filename)
                my_image.save(save_path)
                result = DeepFace.analyze(
                img_path = save_path, 
                actions = ['age'],
                )
                age = result[0]['age']
            return render_template("age_result.html", age=age)
        
@app.route("/register", methods = ["GET","POST"])
def register():
    if request.method =="GET":
        return render_template("Register.html")
    
    elif request.method == "POST":
        my_email = request.form["email"]
        my_password = request.form["password"]
        user_database.register(my_email, my_password)
        return render_template("Register.html")

@app.route("/bmr", methods=["GET", "POST"])
def bmr():
    if request.method == "GET":
        return render_template("bmr.html")
    elif request.method == "POST":
       
        my_weight = request.form["weight"]
        my_height =request.form["height"]
        my_gender = request.form['gender']
        my_age =request.form["age"]
        if my_weight and my_gender and my_height and my_age == "":
            return render_template("bmr.html")
            
        else:
            try:
                my_weight = float(my_weight)
                my_height = float(my_height)
                my_age = int(my_age)
            except ValueError:
                return render_template("bmr.html")
            
            if my_gender == 'male':
                user_bmr = ((10 * my_weight) + (6.25 * my_height) - (5 * my_age) + 5)
                print(user_bmr)
                return render_template("bmr_result.html", user_bmr=user_bmr)
                    
            elif my_gender == 'female':
                user_amr = ((10 * my_weight) + (6.25 * my_height) - (5 * my_age) - 161)
                print(user_amr)
                return render_template("bmr_result.html", user_amr=user_amr)
    
    
# @app.route("/result")
# def result():
#     return render_template("result.html")