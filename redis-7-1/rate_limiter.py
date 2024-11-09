import time
import redis


client = redis.Redis(host='localhost', port=6379, db=0)


MAX_REQUESTS = 5
TIME_WINDOW = 60  

def is_request_allowed(user_id):
   
    user_key = f"request_timestamps:{user_id}"
    
   
    current_time = int(time.time())
    
    
    client.rpush(user_key, current_time)
    
  
    client.ltrim(user_key, -MAX_REQUESTS, -1)
    
    
    client.expire(user_key, TIME_WINDOW)
    
    
    timestamps = client.lrange(user_key, 0, -1)
    
    
    if len(timestamps) < MAX_REQUESTS:
        print("Request allowed.")
        return True
    else:
        
        time_diff = current_time - int(timestamps[0])
        if time_diff < TIME_WINDOW:
            print("Rate limit exceeded. Please try again later.")
            return False
        else:
            print("Request allowed.")
            return True


user_id = "user_123"
for i in range(7):  
    is_request_allowed(user_id)
    time.sleep(10) 
