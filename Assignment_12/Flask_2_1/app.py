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


def auth(email, password):
    if email =="morteza@yahoo.com" and password == "moricyber":
        return True
    else:
        return False
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
        result = user_database.auth(my_email, my_password)
        if result:
            #upload
            return redirect(url_for("upload"))
        else:
            #Register
            message = " Surry! This user has not been found, please first register your info"
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
            return render_template("result.html", age=age)
        
@app.route("/register", methods = ["GET","POST"])
def register():
    if request.method =="GET":
        return render_template("Register.html")
    
    elif request.method == "POST":
        my_email = request.form["email"]
        my_password = request.form["password"]
        user_database.register(my_email, my_password)
        return render_template("Register.html")
    
# @app.route("/result")
# def result():
#     return render_template("result.html")