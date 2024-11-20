from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from celery.result import AsyncResult
from main import app as celery_app, dummy_task_2


app = FastAPI()


class TaskOut(BaseModel):
    id: str
    status: str


@app.get("/start")
def start() -> TaskOut:
    r = dummy_task_2.delay()
    return _to_task_out(r)


@app.get("/status")
def status(task_id: str) -> TaskOut:
    try:
        r = celery_app.AsyncResult(task_id)
        return _to_task_out(r)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


def _to_task_out(r: AsyncResult) -> TaskOut:
    return TaskOut(id=r.task_id, status=r.status)
