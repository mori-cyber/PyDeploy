import sqlite3
from typing import Union
from fastapi import FastAPI, HTTPException, status,Form,File
from pydantic import BaseModel
from fastapi.responses import StreamingResponse,Response, HTMLResponse
import cv2
import io
from threading import Thread
#________________________________________________________________________________________#

connection =sqlite3.connect("todo.db",check_same_thread=False)
my_cursor =connection.cursor()


app = FastAPI()

@app.get("/")
def root_read():
    return {"hello":"world"}


@app.get("/items")
def read_database():   
    table={}
    for i,data in enumerate(my_cursor.execute("SELECT * FROM tasks")):
        table[i]=data
    return (str(table))
Thread(target=read_database).start()

@app.delete("/items/{id}")
def remove_items(id:int):
    my_cursor.execute("SELECT EXISTS(SELECT 1 FROM tasks WHERE id = ?)", (id,))
    exists = my_cursor.fetchone()[0]
     # Print the result
    if exists:
        print(f"The number {id} exists in the table id.")
        my_cursor.execute("DELETE FROM tasks WHERE id= ?",(id,))
        connection.commit()
        
    else:
        print(f"The number {id} does not exist in the table id.")
     
    return {"message":"item deleted"}
Thread(target=remove_items).start()

@app.post("/items/{id}/{title}/{description}/{time}/{status}")
def insert_data(id:int, title:str, description:str,time:str,status:int):
    my_cursor.execute("INSERT INTO tasks(id,title,description,time,status) VALUES (?,?,?,?,?)",(id, title, description,time,status))
    connection.commit()
            
    return {"items":"is insertes"}
Thread(target=insert_data).start()

@app.put('/items/{id}/{description}/{status}')
def update_table(id:int, description:str,status:int):
    # Construct SQL query
        update_query = "UPDATE tasks SET description = ?,status=? WHERE id = ?"

# Execute SQL query
        my_cursor.execute(update_query, (description,status, id))
        connection.commit()
        connection.close()  
        return {"table":"is update"}
Thread(target=update_table).start()


        
        

    




# @
# my_cursor.execute("INSERT INTO student(id,title,description,time,status) VALUES(3,'reza','kord',34)")