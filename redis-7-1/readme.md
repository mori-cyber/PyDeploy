# Redis
[![My Skills](https://skillicons.dev/icons?i=redis)](https://redis.io)

```
thank's : https://github.com/tandpfun/skill-icons/tree/main
```

In this project, we have done the following tasks: 

## **1. Setup Redis Server**

In this part, we set up a Redis server either using Docker or on a cloud service. and Choose the following method preference.

### **Option 1: Setup Redis Server with Docker**

1. Docker installed on your machine.
2. Pull and run the Redis image from Docker Hub:
    
    ```bash
    docker pull redis
    docker run --name redis-server -d -p 6379:6379 redis
    ```
    
3. Verify that Redis is running by connecting to it:
    
    ```bash
    docker exec -it redis-server redis-cli
    ```
    
3. Take note of the connection details (hostname, port, and password) as you’ll need these to connect from your Python code.

## **2. Hello World with Redis and Python**

Install the Redis Python client by running:

```bash
pip install redis
```

Create a Python script to perform the following tasks:

1. **Connect to the Redis server** using the `redis` Python package.
2. **Set** a key-value pair in Redis with key `"name"` and value `"<YOUR NAME>"`.
3. **Retrieve** the value of the key `"name"` from Redis and print it.

## **3. Store User Session Information**

I Write a Python function that stores and retrieves session information for a user. The session information should include user ID and last login time. Use the Redis `HMSET` and `HGETALL` commands to store this data in a hash.


**Deliverable**: Write a Python script that:

- Stores the session data.
- Retrieves and prints the session data from Redis.

## **4. Expire Keys**

Write a Python script that stores a temporary OTP (one-time password) for a user that expires after 60 seconds using the `SETEX` command.

**Deliverable**: Write a Python script that:

- Stores the OTP with a 60-second expiration.
- Verifies that after 60 seconds, the OTP is no longer available in Redis.

## **5. Rate Limiter**

Implement a rate limiter that restricts a user from performing more than 5 requests per minute. If the user exceeds the limit, they should receive a "Rate limit exceeded" message.

- Store the request timestamps in a Redis list.
- Use `LTRIM` to keep only the most recent 5 timestamps and `EXPIRE` to ensure the list resets every minute.

**Deliverable**: Write a Python script that:

- Tracks requests and checks if the user is allowed to make the request or if they have exceeded their limit.
- Outputs a message based on whether the rate limit has been exceeded.

## **6. Leaderboard Implementation**

Create a leaderboard using Redis sorted sets. The leaderboard should store user scores for a game.

- Use the `ZADD` command to add users and their scores.
- Implement a function that returns the top N users.

**Deliverable**: Write a Python script that:

- Adds users and their scores to a Redis sorted set.
- Retrieves and prints the top 3 users from the leaderboard.

## **7. Batch User Data Updates with Redis Pipelines**

Redis pipelines allow you to optimize multiple commands by batching them together. In this problem, you'll use pipelines to efficiently update user data in bulk.

### **Task:**

1. I am  given a list of user information where each user has the following attributes:
    - `user_id` (string)
    - `name` (string)
    - `score` (float)
    
2. I store this information in Redis using hashes where:
    - The Redis key for each user is `"user:<user_id>"`.
    - Each hash will store the user’s `name` and `score`.
3.I Use a Redis pipeline to efficiently batch and execute the Redis commands for storing all users' data.

**Deliverable**: Write a Python script that:

- I Use a Redis pipeline to store the list of users' data in Redis.
- After storing, retrieves the data for each user and prints it out.

**Hint**: Use the `pipeline` and `hmset` commands in Redis to batch the operations.

### **Example Solution**:

This problem  help me to understand how to optimize multiple Redis operations using pipelines, making the interaction more efficient, especially when dealing with a large number of commands.
# thank you mr sajad aemmi❤️❤️❤️
