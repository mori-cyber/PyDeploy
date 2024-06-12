#نحلیل عکس چهره یک شخص با هوش مصنوعی
#https://github.com/serengil/deepface
import os
from flask import Flask, render_template,request,redirect,session , url_for

import user_database

app = Flask("AMR_ANALYSIS")


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

@app.route("/register", methods = ["GET","POST"])
def register():
    if request.method =="GET":
        return render_template("Register.html")
    
    elif request.method == "POST":
        my_email = request.form["email"]
        my_password = request.form["password"]
        user_database.register(my_email, my_password)
        return render_template("Register.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    elif request.method == "POST":
       
        my_weight = request.form["weight"]
        my_height =request.form["height"]
        my_gender = request.form['gender']
        my_age =request.form["age"]
        if my_weight and my_gender and my_height and my_age == "":
            return redirect(url_for("upload"))
            
        else:
            try:
                my_weight = float(my_weight)
                my_height = float(my_height)
                my_age = int(my_age)
            except ValueError:
                return redirect(url_for("upload"))
            
            if my_gender == 'male':
                result = ((10 * my_weight) + (6.25 * my_height) - (5 * my_age) + 5)
                print(result)
                return render_template("result.html", result=result)
                    
            elif my_gender == 'female':
                result = ((10 * my_weight) + (6.25 * my_height) - (5 * my_age) - 161)
                print(result)
                return render_template("result.html", result=result)
    

