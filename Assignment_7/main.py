
import asyncio
import requests
import os
from dotenv import load_dotenv




async def rhyam(API_KEYWORD, word):
    url = f"https://rhyming.ir/api/rhyme-finder?api={API_KEYWORD}&w={word}&sb=1&mfe=2&eq=1"
    response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url)
    return print(response.json())

async def get_states():
    url = "https://iran-locations-api.vercel.app/api/v1/fa/states"
    response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url)
    return response.json()

async def get_cities(state_id):
    url = f"https://iran-locations-api.vercel.app/api/v1/fa/cities?state_id={state_id}"
    response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url)
    return response.json()

async def get_coordinates(state_name, city_name):
    print("Coordinates Started")
    states = await get_states()
    for state in states:
        if state["name"] == state_name:
            response = await get_cities(state["id"])
            cities = response["cities"]
            for city in cities:
                if city["name"] == city_name:
                    latitude = city["latitude"]
                    longitude = city["longitude"]
                    break
            else:
                print(f"Not found city {city_name}" )
                latitude = None
                longitude = None
            break
    else:
        print(f"Not found state {state_name}")
        latitude = None
        longitude = None

    print("Latitude is:",latitude,"longitude is:",longitude )
    return latitude, longitude
         
              
async def main():
    load_dotenv(dotenv_path="FastAPI/Assignment_7/.env")
    API_KEYWORD = os.environ.get("RHYME_API_KEY")
    word =input("enter a rhyme word:")
    state_name =input("enter your state name:")
    city_name = input("enter your city name:")
    await asyncio.gather(rhyam(API_KEYWORD, word), get_coordinates(state_name=state_name, city_name=city_name))
    print("Main ended") 





if __name__ == '__main__':
    asyncio.run(main())