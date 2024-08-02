## In this task we create and run these works:
2. AI app
    - [ ]  Blog
        - [ ]  Create class `Topic` in `user_database.py`
        - [ ]  Client
            - [ ]  Show blog posts on `/blog` page
            - [ ]  Summarize long texts
        - [ ]  Admin
            - [ ]  Show blog posts in the admin panel
            - [ ]  Add new post
            - [ ]  Edit post
            - [ ]  Delete post    
    ---
    
3. MicroServices
    - [ ]  Create a directory named `microservices`
    - [ ]  Hafez
        - [ ]  Create a file named `hafez.py` ****in the `microservices` directory
        - [ ]  Create a flask app in `hafez.py` and define a route named `/fal`
        - [ ]  Use the https://pypi.org/project/hafez/ package to generate a random **Omen (فال)** and return it in json format (just `interpretation` part)
        - [ ]  Run the Hafez microservice on a port (e.g. 8081)
    - [ ]  Khayyam
        - [ ]  Create a file named `khayyam.py` ****in the `microservices` directory
        - [ ]  Create a flask app in `khayyam.py` ****and define a route named **`/**today`
        - [ ]  Use the https://pypi.org/project/Khayyam/ package to convert today's date to **Jalali (هجری شمسی)** and return it in json format
        - [ ]  Run the Khayyam microservice on a port (e.g. 8082)
    - [ ]  QR Code
        - [ ]  Create a file named `qr_code.py` ****in the `microservices` directory
        - [ ]  Create a flask app in `qr_code.py` ****and define a route named ****`/generate`
        - [ ]  Use the https://pypi.org/project/qrcode/ package to convert text to qrcode image and return it
        - [ ]  Run the QR Code microservice on a port (e.g. 8083)
    - [ ]  Main
        - [ ]  Create a file named `main.py` ****in the `microservices` directory
        - [ ]  Create a flask app in `main.py` ****and define a route named **`/`**
        - [ ]  The main microservice will call the Hafez microservice and the Kayyam microservice and get the results, then merge them in json format
            
            ```
            ```
            
        - [ ]  Send the JSON data to the QR Code microservice and finally return the resulting image
        - [ ]  Run the Main microservice on a port (e.g. 8080)
   ##The overview of this work:

    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f36084e4-06a5-4ee8-8cbd-0ea24d0efa73/7b2a35ac-4c20-42d1-a3a9-704aa8ca8e08/Untitled.png)
    
