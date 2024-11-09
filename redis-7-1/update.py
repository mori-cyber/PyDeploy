import redis


r = redis.Redis(host='localhost', port=6379, db=0)


users_data = [
    {"user_id": "user_1", "name": "reza", "score": 85.5},
    {"user_id": "user_2", "name": "amin", "score": 90.0},
    {"user_id": "user_3", "name": "maryam", "score": 76.4},
    {"user_id": "user_3", "name": "morteza", "score": 76.4},
    {"user_id": "user_3", "name": "hasan", "score": 76.4},
    {"user_id": "user_3", "name": "shima", "score": 76.4},
    {"user_id": "user_3", "name": "aida", "score": 76.4}
]


pipe = r.pipeline()


for user in users_data:
    user_key = f"user:{user['user_id']}"
    pipe.hmset(user_key, {"name": user["name"], "score": user["score"]})


pipe.execute()


for user in users_data:
    user_key = f"user:{user['user_id']}"
    user_data = r.hgetall(user_key)
    
    decoded_data = {key.decode('utf-8'): value.decode('utf-8') for key, value in user_data.items()}
    print(f"{user_key} -> {decoded_data}")
