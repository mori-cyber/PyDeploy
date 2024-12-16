import time
import random
import requests
from celery import Celery


celery_app = Celery(
    'tasks', 
    broker='redis://localhost:6379',
    backend='redis://localhost:6379'
)

@celery_app.task
def face_task(face_data: bytes):
    time.sleep(20)
    result = random.choice([True, False])
    return {"status": "completed",
            "result": result}



@celery_app.task
def speech_to_text(speech_data: bytes):
    time.sleep(5)
    result = random.choice([True, False])
    return {"status": "completed",
            "result": result}



@celery_app.task
def gesture_recognition(gesture_data: bytes):
    response = requests.post("http://127.0.0.1:8080/authentication/gesture")
    result = response.json()
    return {"status": "completed",
            "result": result}