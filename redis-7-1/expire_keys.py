import time
import redis

client = redis.Redis(host='localhost', port=6379, db=0)

def set_otp(user_id, otp, expiration=60):
    client.setex(user_id, expiration, otp)
    print(f"OTP '{otp}' set for user '{user_id}' with a {expiration}-second expiration.")

def get_otp(user_id):
    otp = client.get(user_id)
    if otp is None:
        print(f"OTP for user '{user_id}' has expired or does not exist.")
    else:
        print(f"Retrieved OTP for user '{user_id}': {otp.decode('utf-8')}")

user_id = "user_123"
otp = "987654"

set_otp(user_id, otp)

print("Checking OTP before expiration:")
get_otp(user_id)

time.sleep(60)
print("Checking OTP after expiration:")
get_otp(user_id)
