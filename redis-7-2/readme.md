
[![My Skills](https://skillicons.dev/icons?i=redis)](https://redis.io)
```
 https://docs.celeryq.dev/en/stable/
```


## Redis&Celery
1. Redis insight
    - [ ] I Download https://redis.io/insight/ and install it


![redis-insight](https://github.com/user-attachments/assets/46c23b3a-a4b2-4082-97de-97a24bdef400)



2. **Getting Started**
    - [ ]  I Create a virtual environment 
        
        ```bash
        virtualenv -p python3.10.12 myvenv
        . venv/bin/activate
        ```
        
    - [ ]  I Install radis, celery and fastapi with this command:
        ```bash
        pip install "redis" "celery" "fastapi[standard]"
        salt and pepper به مقدار لازم
        ```
        
    - [ ]  Create a celery app object 
        
        ```python
        redis_url = "redis://localhost:6379"
        app = Celery(__name__, broker=redis_url, backend=redis_url)
        ```
   - [ ] pull Redis and run it on a docker container in ubuntu os
     ```bash
     sudo docker pull redis
     sudo docker run --name min_redis -d -p 6379:6379 redis
     ```        
    - [ ]  Launch a worker 
        ```bash
        celery --app main --concurrency=1 --loglevel=DEBUG
        ```
     - [ ] Launch a fastapi
       ```bash
       uvicorn api:app --reload
       ```
        
3. **Using Celery with FastAPI**
    - [ ]  With those building blocks, we can now bind the two together. We simply import `main.py` in FastAPI, and call our task.delay() from a REST call. We can return the task ID and its status to the user:

![2](https://github.com/user-attachments/assets/8447da8f-3248-4645-a7db-a0708bbe5717)

![3](https://github.com/user-attachments/assets/fc56f455-401c-408c-94eb-63d9e7e874d0)

## Overview of this plan

![03-celery excalidraw](https://github.com/user-attachments/assets/4dea865a-0bc1-439b-928b-5bfe1700e5da)

          
   
