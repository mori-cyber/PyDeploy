import os
from datetime import datetime
from celery import Celery
from time import sleep

redis_url = "redis://localhost:6379"
app = Celery(__name__, broker=redis_url, backend=redis_url)


@app.task
def hello_world():
    return 'Hello, World!'


@app.task
def add(x, y):
    print("add function")
    return x + y


@app.task
def dummy_task_1():
    folder = "/tmp/celery"
    os.makedirs(folder, exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    with open(f"{folder}/task-{now}.txt", "w") as f:
        f.write("hello!")


@app.task        
def dummy_task_2(name='morijooon') -> str:
    sleep(5)
    return f'Hello {name}!'


@app.task
def dummy_task_3() -> str:
    folder = "/tmp/celery"
    os.makedirs(folder, exist_ok=True)
    with open(f"{folder}/x.txt", "w") as f:
        f.write("dummy content")
    return "File created successfully."
