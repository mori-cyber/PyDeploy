import redis


client = redis.Redis(host='localhost', port=6379, db=0)


LEADERBOARD_KEY = "game_leaderboard"

def add_users_to_leaderboard(users_scores):
    
    for user, score in users_scores.items():
        client.zadd(LEADERBOARD_KEY, {user: score})
    print("Users added to leaderboard.")

def get_top_n_users(n):
    
    top_users = client.zrevrange(LEADERBOARD_KEY, 0, n - 1, withscores=True)
    return top_users


users_scores = {
    'user1': 100,
    'user2': 20,
    'user3': 80,
    'user4': 90,
    'user5':10
}


add_users_to_leaderboard(users_scores)

top_3_users = get_top_n_users(2)
print("Top 2 users:")
for rank, (user, score) in enumerate(top_3_users, start=1):
    print(f"{rank}. {user.decode('utf-8')} - Score: {int(score)}")
