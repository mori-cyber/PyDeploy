1. My Personal Website
    - [ ]  Add `layout.html` to template directory for [**Template Inheritance**](https://jinja.palletsprojects.com/en/3.1.x/templates/#template-inheritance)
    - [ ]  Connect your web app to a SQL database (e.g. postgresql) using [SQLModel](https://sqlmodel.tiangolo.com/) or [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)
    - [ ]  Create class User contains following properties:
        - [ ]  id (Primary Key)
        - [ ]  first_name
        - [ ]  last_name
        - [ ]  email
        - [ ]  username
        - [ ]  age
        - [ ]  city
        - [ ]  country
        - [ ]  password
        - [ ]  join_time
    - [ ]  Create PyDantic classes to validate all properties in register and login steps
    - [ ]  Add register and login form in templates (Front-end)
        - [ ]  Add 2 fields for password:
            - [ ]  Password
            - [ ]  Confirm password
    - [ ]  Add register and login functions contains `GET` and `POST` methods in app (Back-end)
        - [ ]  Compare password and confirm password values to make sure they are equal
        - [ ]  At the registration step, make sure that the username has not been used before
    - [ ]  Hash password using bcrypt
        
        [GitHub - pyca/bcrypt: Modern(-ish) password hashing for your software and your servers](https://github.com/pyca/bcrypt/?tab=readme-ov-file#password-hashing)
        

---

1. AI app
    - [ ]  Add `layout.html` to template directory for [**Template Inheritance**](https://jinja.palletsprojects.com/en/3.1.x/templates/#template-inheritance)
    - [ ]  Use YOLOv8 classification model instead of DeepFace as AI model in our story
        
        [Classify](https://docs.ultralytics.com/tasks/classify/#predict)
        
    - [ ]  Create class User contains following properties:
        - [ ]  id (Primary Key)
        - [ ]  first_name
        - [ ]  last_name
        - [ ]  email
        - [ ]  username
        - [ ]  age
        - [ ]  city
        - [ ]  country
        - [ ]  password
        - [ ]  join_time
    - [ ]  Create PyDantic classes to validate all properties in register and login steps
    - [ ]  Add register and login form in templates (Front-end)
        - [ ]  Add 2 fields for password:
            - [ ]  Password
            - [ ]  Confirm password
    - [ ]  Add register and login functions contains `GET` and `POST` methods in app (Back-end)
        - [ ]  Compare password and confirm password values to make sure they are equal
        - [ ]  At the registration stage, make sure that the username has not been used before
    - [ ]  Hash password using bcrypt
