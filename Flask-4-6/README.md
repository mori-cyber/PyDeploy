- [ ]  In this task we do:
    - [X]  I Download a paid admin template using https://github.com/Alex313031/Resources-Saver
    - [X]  and Add `html`, `CSS`, `js` and images files to your Flask web app
    - [x]  and i Fix static file paths
    - [x]  Add `/admin` route to access the admin dashboard
    - [x]  Read all users from the database and show them in the admin dashboard
    - [x]  Add the `join_time` column to the `users` table in the database
    - [x]  Show the user’s `join_time` in the admin dashboard:
 
- [x]  Docker 🐳

   In the second section,  I did the following:
   
    - [X]  Create a Docker network
    
    ```
    docker network create my_network
    ```
    
    - [X]   I run the Flask app Docker container and connect it to the network
    
    ```
    docker run --network my_network --name my-postgres -e POSTGRES_PASSWORD=***** -e POSTGRES_USER=***** -e POSTGRES_DB=***** -d postgres
    ```
    
    - [x]  Run the PostgreSQL Docker container and connect it to the network
    
    ```
    docker run --rm --network my_network --name ai_web_app -p 8080:5000 -v $(pwd):/myapp ai_web_app
    ```
    
    - [X]  My screenshot of the output is the following images:
    
   


 


    
    
    ![Untitled-2024-07-07-0947.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f36084e4-06a5-4ee8-8cbd-0ea24d0efa73/abbdf6d4-cd34-4651-8e0c-2355f0288bf2/Untitled-2024-07-07-0947.png)
