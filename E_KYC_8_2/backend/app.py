from fastapi import FastAPI , UploadFile
from celery_task import celery_app, speech_to_text, gesture_recognition
app = FastAPI()



@app.get("/")
def root():
    return {"Hello": "world"}

@app.post("/authentication/speech")
async def authenticate_speech(file: UploadFile):
    task = speech_to_text.delay(await file.read())
    return {"task_id":task.id,
            "status": "processing"
            }   
@app.post("/authenticate/gesture")
async def authenticate_gesture(file: UploadFile):
    task = gesture_recognition.delay(await file.read())
    return {"task_id": task, "status": task.state}


@app.get("/task_status")
def  get_task_status(task_id:str):
    result = celery_app.AsyncResult(task_id)  
    return {"status":result.state}