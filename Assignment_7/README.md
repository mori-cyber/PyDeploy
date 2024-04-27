In this section, we learned synchronous and asynchronous execution of multiple functions and understood their differences.
1. Classroom Activities
    - [ ]  Write sync and async marriage program
    - [ ]  Write async Download + Printer + AI program
    
2. Async API
    - [ ]  Write a function named `rhyme_finder` for use the following api to get a word and return it’s rhymes
    
    ```python
    url = f"https://rhyming.ir/api/rhyme-finder?api={API_KEY}&w={word}&sb=1&mfe=2&eq=1"
    response = requests.request("GET", url)
    ```
    
    - [ ]  Write two functions named `get_states` and `get_cities` for use the following apis to return list of states of Iran and list of cities of your state respectively
    
    ```python
    url = "https://iran-locations-api.vercel.app/api/v1/fa/states"
    response = requests.request("GET", url)
    ```
    
    ```python
    url = f"https://iran-locations-api.vercel.app/api/v1/fa/cities?state_id={state_id}"
    response = requests.request("GET", url)
    ```
    
    - [ ]  Write a function named `get_coordinates`
        - [ ]  Get list of states from `get_states`
        - [ ]  Find your state’s id with search by name in the list of states
        - [ ]  Get list of cities of your state using your state’s id from `get_cities`
        - [ ]  Find your city with search by name in the list of cities
        - [ ]  Return `latitude` and `longitude` of your city
    
    - [ ]  Write a function named `main` for call above functions
    - [ ]  To reduce running time, Use `AsyncIO` when you can
