from pymongo import MongoClient
from fastapi import FastAPI, HTTPException
from celery.result import AsyncResult
from .tasks import add_numbers




app = FastAPI()

client = MongoClient("mongodb://mongodb:27017/")
db = client.ekyc_db

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/add-sample/")
def add_sample():
    db.users.insert_one({"name": "John Doe"})
    return {"message": "User added"}

@app.post("/add")
async def add_task(num1: float, num2: float):
    task = add_numbers.delay(num1, num2)
    return {"task_id": task.id}

@app.get("/result/{task_id}")
async def get_result(task_id: str):
    result = AsyncResult(task_id, app=celery_app)
    if result.state == "PENDING":
        return {"status": "PENDING"}
    elif result.state == "SUCCESS":
        return {"status": "SUCCESS", "result": result.result}
    elif result.state == "FAILURE":
        return {"status": "FAILURE", "error": str(result.info)}
    else:
        return {"status": result.state}
