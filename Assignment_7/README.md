In this section, we learned synchronous and asynchronous execution of multiple functions and understood their differences.
1. Classroom Activities
    - [ ] We write sync and async marriage program
    - [ ]  We write async Download + Printer + AI program
    
2. Async API
    - [ ]  We write a function named `rhyme_finder` to use the following API to get a word and return its rhymes
    
    ```python
    url = f"https://rhyming.ir/api/rhyme-finder?api={API_KEY}&w={word}&sb=1&mfe=2&eq=1"
    response = requests.request("GET", URL)
    ```
    
    - [ ]  We write two functions named `get_states` and `get_cities` for use in the following APIs to return a list of states of Iran and a list of cities of your state respectively
    
    ```python
    url = "https://iran-locations-api.vercel.app/api/v1/fa/states"
    response = requests.request("GET", URL)
    ```
    
    ```python
    url = f"https://iran-locations-api.vercel.app/api/v1/fa/cities?state_id={state_id}"
    response = requests.request("GET", URL)
    ```
    
    - [ ]  We write a function named `get_coordinates`
        - [ ]  Get the list of states from `get_states`
        - [ ]  Find your state’s ID with a search by name in the list of states
        - [ ]  Get the list of cities of your state using your state’s ID from `get_cities`
        - [ ]  Find your city with search by name in the list of cities
        - [ ]  Return `latitude` and `longitude` of your city
    
    - [ ]  We write a function named `main` to call the above functions
    - [ ]  To reduce running time, we Used `AsyncIO` when you can
```