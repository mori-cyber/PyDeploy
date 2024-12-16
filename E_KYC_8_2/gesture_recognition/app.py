import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import urllib
from fastapi import FastAPI, UploadFile


app = FastAPI()



@app.get("/")
def root():
  return {"hello":"gesture"}

@app.post("/authentication/gesture")
async def gesture_authentication(file: UploadFile):
        url = f'https://storage.googleapis.com/mediapipe-tasks/gesture_recognizer/{file.filename}'
        urllib.request.urlretrieve(url, file.filename)
        base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')
        options = vision.GestureRecognizerOptions(base_options=base_options)
        recognizer = vision.GestureRecognizer.create_from_options(options)

        images = []
        results = []
       
        image = mp.Image.create_from_file(file.filename)
            
        recognition_result = recognizer.recognize(image)

        top_gesture = recognition_result.gestures[0][0]
        hand_landmarks = recognition_result.hand_landmarks
        results.append((top_gesture, hand_landmarks))

        return top_gesture