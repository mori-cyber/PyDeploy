[![My Skills](https://skillicons.dev/icons?i=django)](https://django.io)

 **I Write my first Django app**
    - [ ]  Install Django
   ```
   pip install Django
   ```
    - [ ]  Create a project
   ```
   mkdir djangotutorial
   django-admin startproject mysite djangotutorial
   python manage.py runserver
   ```
    - [ ]  Create the Polls app
   ```
   python manage.py startapp polls
   python manage.py runserver
   ```
    - [ ]  Create `Question` and `Choice` models
    ```
    python manage.py migrate
    
    from django.db import models
    class Question(models.Model):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField("date published")
    
    
    class Choice(models.Model):
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)
    ```
    - [ ]  Migrate database
    ```
    python manage.py makemigrations polls
    python manage.py sqlmigrate polls 0001
    ```
    - [ ]  Run project 🚀
   ```
   python manage.py migrate
   ```
   
