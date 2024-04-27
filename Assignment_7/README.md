In this section, we learned synchronous and asynchronous execution of multiple functions and understood their differences.
1. Classroom Activities
    - [x] We write sync and async marriage program
    - [x]  We write async Download + Printer + AI program
    
2. Async API
    - [x]  We write a function named `rhyme_finder` to use the following API to get a word and return its rhymes
    
    ```python
    url = f"https://rhyming.ir/api/rhyme-finder?api={API_KEY}&w={word}&sb=1&mfe=2&eq=1"
    response = requests.request("GET", URL)
    ```
    
    - [x]  We write two functions named `get_states` and `get_cities` for use in the following APIs to return a list of states of Iran and a list of cities of your state respectively
    
    ```python
    url = "https://iran-locations-api.vercel.app/api/v1/fa/states"
    response = requests.request("GET", URL)
    ```
    
    ```python
    url = f"https://iran-locations-api.vercel.app/api/v1/fa/cities?state_id={state_id}"
    response = requests.request("GET", URL)
    ```
    
    - [x]  We write a function named `get_coordinates`
        - [ ]  Get the list of states from `get_states`
        - [ ]  Find your state’s ID with a search by name in the list of states
        - [ ]  Get the list of cities of your state using your state’s ID from `get_cities`
        - [ ]  Find your city with search by name in the list of cities
        - [ ]  Return `latitude` and `longitude` of your city
         
   output is:
![Screenshot from 2024-04-27 21-04-49](https://github.com/mori-cyber/PyDeploy/assets/65276280/d818099c-acec-485d-886a-3a4a0efed2fd)

        
    - [x]  We write a function named `main` to call the above functions
    - [x]  To reduce running time, we Used `AsyncIO` when you can
To execute this code first install requirements:
```
requirements.txt
```
and then main.py code with:
```
!python main.py
```

