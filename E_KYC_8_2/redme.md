[![My Skills](https://skillicons.dev/icons?i=redis)](https://redis.io)
[![My Skills](https://skillicons.dev/icons?i=celery)](https://docs.celeryq.dev/en/stable/)
[![My Skills](https://skillicons.dev/icons?i=fastapi)](https://fastapi.tiangolo.com/)
1. Redis
    - [ ]  Pull Redis docker image
    - [ ]  Run redis docker container
2. Celery
    - [ ]  Create a `backend` folder and go to it
    - [ ]  Create a `celery_tasks.py` file
    - [ ]  Write some celery tasks in the `celery_tasks.py` file.
3. FastAPI
    - [ ]  Go to backend folder
    - [ ]  Create an `app.py` file
    - [ ]  Write some routes in the `app.py` file.       
2. Gesture Recognition API
    1. FastAPI
        - [ ]  Create a `gesture_recognition` folder and go to it
        - [ ]  Create an `app.py` file
        - [ ]  Write some routes in the `app.py` file.        
3. Postman
    1. Test your APIs with Postman
    2. Save responses
    3. Export from Postman to a `.json` file
    4. Send the `.json` file to the telegram group

## How to run

1. run Redis container

```
sudo docker pull redis

sudo docker run --name some-redis -d -p  6379:6379 redis

```
2. run celery_tasks

```
celery -A celery_tasks worker --loglevel=ERROR

```
3. run main API

```
fastapi dev app.py

```

## output for postman:


![gesture_2](https://github.com/user-attachments/assets/95e6854c-83b2-48b8-b081-42f144e463f5)
![gesture_1](https://github.com/user-attachments/assets/42716515-a3d9-450b-8005-c8de8e09e6eb)
![gesture](https://github.com/user-attachments/assets/23b28709-1fd6-4280-a23c-d61adbca2de8)

