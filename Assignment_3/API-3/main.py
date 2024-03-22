from typing import Union
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import StreamingResponse
# import cv2
# import numpy as np
# import io

app = FastAPI()
print(app)
solar = { "sun": {
        "radius": 695508000,
        "distanceFromSun": 0,
        "didYouKnow": "The color of the Sun in space is actually mostly white, not yellow or orange. The reason it appears yellow or orange on Earth is due to atmospheric scattering, especially when it is low in the sky."
    },

    "Mercury": {
        "distanceFromSun": 57900000000,
        "radius": 2439000,
        "didYouKnow": "Mercury is actually smaller than some moons of our solar system including Ganymede of Jupiter and Titan of Saturn.",
    },
    "Venus": {
        "distanceFromSun": 108200000000,
        "radius": 6051000,
        "didYouKnow": "While having the second hottest surface temperature in the solar system after The Sun, which is 450C (842F), its atmosphere is so dense that it actually crushes CO2 at the surface and turns it into an exotic material called \"super critical fluid\" which is neither a gas or a liquid but has properties of both. Humans could never live on the surface of Venus but some have proposed living <a href=\"http://www.bbc.com/future/story/20161019-the-amazing-cloud-cities-we-could-build-on-venus\" target=\"_blank\">up in the clouds.</a>"
    },
    "Earth": {
        "distanceFromSun": 149600000000,
        "radius": 6371000,
        "didYouKnow": "Earth's first line of defense against harmful radiation from The Sun is its magnetosphere which extends much further out than the atmosphere. However, the magnetosphere is not perfectly round. On the north and south poles it plunges back down to the Earth making a funnel shape. Occasionally charged particles from The Sun will get trapped in the funnel and fall down to Earth and interact with our atmosphere. This is what causes the visual phenomenon called an         <a href =\"https://en.wikipedia.org/wiki/Aurora\" target =\"_blank\">aurora</a> or northern lights.",
        "moons": {
            "The Moon": {
                "radius": 1738000,
                "distanceFromPlanet": 384400000,
            }
        }
    },
    
}
sun =solar["sun"]
Mercury=solar["Mercury"]
Venus=solar["Venus"]
Earth=solar["Earth"]


@app.get("/")
def read_root():
    return {"Hi! Welcome to my API": "The Solar System API provides information for thousands of all solar system planets and their moons."}
           
@app.get("/{P}")
def read_root(P):
     if P=="planets":
        return solar
     elif P=="sun":
         return sun 
     elif P=="Mercury":
         return Mercury
     elif P=="Venus":
         return Venus
     elif P=="Earth":
         return Earth
                 
     else:
          raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                  detail="you must be correct request:To get the information of each of the planets,please enter /name of planets or /planets for all of them ")