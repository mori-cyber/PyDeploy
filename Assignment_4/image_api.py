
import sqlite3
from typing import Union
from fastapi import FastAPI, HTTPException, status,Form,File,UploadFile
import numpy as np
from fastapi.responses import StreamingResponse,Response, HTMLResponse
import keras
from keras.models import load_model
import cv2
import io
from threading import Thread

connection =sqlite3.connect("image_api.db",check_same_thread=False)
my_cursor =connection.cursor()

with open('person.jpg', 'rb') as file:
     image_data = file.read()

insert_query = "INSERT INTO image_tabel (image) VALUES (?)"

    # Execute the query, passing the image data as a parameter
my_cursor.execute(insert_query, (sqlite3.Binary(image_data),))
connection.commit()



app = FastAPI()

@app.get("/")
def root_read():
    return {"hello":"world"}


@app.post("/convert/{id}")
def gender_recog(id:int):
   # Define SQL query to retrieve image data
    my_cursor.execute("SELECT image FROM image_tabel WHERE id = ?", (id,))
    input_file = my_cursor.fetchone()[0]
    # connection.close()

    np_array = np.frombuffer(input_file, dtype=np.uint8)
    image_rgb = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)

    # cv2.imwrite("my_image_1.jpg", image_rgb)
    model = load_model("Gender_detection.h5")
    image =np.resize(image_rgb,(64,64,3))
    image= image.reshape(1,64,64,3)
    # image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
    pred =model.predict(image)
    result =np.argmax(pred)
    
    return   {"zero mean person is man and one maen person is woman":(str(result))}

Thread(target=gender_recog).start()