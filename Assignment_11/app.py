from flask import Flask , render_template, send_file


app = Flask("my_website")

@app.route("/")
def design_1():
    
    return  render_template("index.html")

@app.route("/my_cv")
def my_cv():
    
    cv_file = 'static/my_resume.pdf'
    return send_file(cv_file, as_attachment=True)

@app.route("/contact")
def my_contact():
 
    contact=["Address:Mrkazi,Arak,Mohajeran-NewTown","Telegram-Id :@AI_Dev20", "Gmail:mortezabiran1401@gmail.com", "Email:tabandeh_taban@yahoo.com"]
    
 
    return render_template("contact.html", contact=contact)
@app.route("/research")
def my_research():
 
    research=["traking targets using learning spatio-temporal contexts despits large occlusion ،Journal of Economics and Administrative Sciences .1399, ISC",
              "Image retrieval through content-based deep learning using the K-nearest neighbor method in large image datasets, 27th International Conference on Computer Society. 1400", 
              "Target tracking using spatio-temporal context learning despite heavy occlusions. The first soft computing conference, Gilan University, 2014.", 
              "Thesis title: video retrieval with deep learning algorithms using an attention mechanism"]
    
 
    return render_template("research.html", research=research)

@app.route("/courses")
def my_courses ():
    courses =['Machine learning course.',
              'Python programming course with artificial intelligence approach at three levels (introductory, intermediate and advanced).',
              "Deep learning course (in the heart of Nesformers).",
              "Data science and data analysis course","Course against hacking and espionage.",
              "Penetration course based on Kali Linux operating system.",
               "Course on dealing with cyber attacks against websites, web servers and the web Applications.",
                "Mobile phone cyber attack description course and coping strategies.",
                 "Security course in the field of communication and information technology.",
                  "Information security engineering and penetration testing course." ]
    return  render_template("courses.html", courses=courses)
