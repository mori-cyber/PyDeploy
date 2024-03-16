from typing import Union
from fastapi import FastAPI
import requests
app = FastAPI()


@app.get("/morteza")
def read_root():
    return { "requests version":requests.__version__,
            "Licence":requests.__license__,
            "Copyright":requests.__copyright__,
            "Author":requests.__author__,
            "Author email":requests.__author_email__,
            "Document url":requests.__url__,
            "title":requests.__title__,
            "description":requests.__description__


}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}