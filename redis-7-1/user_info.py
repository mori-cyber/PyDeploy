import redis
from datetime import datetime


r = redis.Redis(host='localhost', port=6379, db=0)

def store_session(user_id, last_login):
    session_data = {
        "user_id": user_id,
        "last_login": last_login
    }
    
    
    r.hmset(f"session:{user_id}", session_data)
    print(f"Stored session data for user {user_id}")

def retrieve_session(user_id):
    session_data = r.hgetall(f"session:{user_id}")
    
    session_data = {key.decode('utf-8'): value.decode('utf-8') for key, value in session_data.items()}
    return session_data


if __name__ == "__main__":
    user_id = "admin12"
    last_login = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    store_session(user_id, last_login)
    session_data = retrieve_session(user_id)
    print(f"Retrieved session data: {session_data}")
