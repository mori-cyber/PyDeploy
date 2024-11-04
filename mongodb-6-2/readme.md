In this task
- [ ]  I created a MongoDB project called Hose Price, which you can make at the following address:
```
https://cloud.mongodb.com/
```
- [X] I created a database called Test.
- [ ] I created a cluster called User.
- [ ] I created two collections or tables called user and house.
 
 And then using Flask code  I wrote Python and inserted the information into the database with Postman, which includes the user and password definitions and the house-price.csv file. After the features in this file, I ran the RandomForestRegressor model on the training data and converted the model to onnx, then I tested the model with the test data.
 - [X] This is how the syllabus works:

    1. Database 🌱
        - [ ]  First, I create a local MongoDB database with Docker 🐳
    2. API & Back-end 🌐
        - [ ]  Create the back-end app. I use FastAPI and define endpoints below:
            
            
            | Endpoint | Method | Parameters | Result |
            | --- | --- | --- | --- |
            | `/signup` | POST | username
            password
            confirm_password | True, if successful or False, if unsuccessful |
            | `/signin` | POST | username password | 🔑 access token |
            | `/add` | POST | 🔑 access token house features (including price) | True, if successful or False, if unsuccessful |
            | `/predict` | POST | 🔑 access token house features (except price) | house price |
            | `/train` | GET | 🔑 access token | True, if successful or  False, if unsuccessful |
            - `/signup`: Register user in the database
            - `/signin`: Generate an 🔑 access token to using it in other endpoints
            - `/add`: Insert new house features (including price) to the database (It should not work without an access token!)
            - `/predict`: Predict house price based on the given house features (It should not work without an access token!)
            - `/train`: Train the AI model again and export it to ONNX format
            (It should not work without an access token!)
        - [ ]  Use `MongoEngine` ODM to connect to the database
        - [ ]  Write a `dockerfile` for this microservice 🐳
    3. AI Model 🧠
        - [ ]  I Created a machine learning model RandomFrest with the framework you want (Scikit-Learn)
        - [ ]  Read dataset from database
        - [ ]  Train your model
        - [ ]  Export to ONNX
        - [ ]  Write ONNX inference
        - [ ]  Write a `dockerfile` for this microservice 🐳
    4. Just one more thing to do: After all, I Write a `docker-compose.yml` file for this shit :)
       - [ ]
       
      ![image](https://github.com/user-attachments/assets/bfd4ef7d-150f-48a8-8f9a-c0fd83d6fe19)

    - [ ] This is my out put of endpoint in postman:

       
