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
  
![docker_1](https://github.com/user-attachments/assets/c43f8781-fa05-4d40-a691-73ca07166457)

![docker](https://github.com/user-attachments/assets/cef12b14-6699-4756-a317-12507c498fb3)

![docker_2](https://github.com/user-attachments/assets/f6c556db-b102-47e2-a730-606969d43db1)

![docker_3](https://github.com/user-attachments/assets/2f6374e8-2c99-4019-b011-dae5c3d44cef)

- [X] My admin output is:

![docker_6](https://github.com/user-attachments/assets/4d437880-aee6-4973-b2df-af7508164b63)






   
