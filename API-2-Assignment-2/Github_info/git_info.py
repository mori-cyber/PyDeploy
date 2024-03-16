import requests

# Replace 'your_username' with your actual GitHub username
username = 'mori-cyber'

# GitHub API endpoints
followers_url = f'https://api.github.com/users/{username}/followers'
following_url = f'https://api.github.com/users/{username}/following'

# Send GET requests to get follower and following counts
followers_response = requests.get(followers_url)
following_response = requests.get(following_url)

# Parse response JSON and get counts
followers_count = len(followers_response.json())
following_count = len(following_response.json())

# Print counts
print(f'I have {followers_count} followers❤️ \n and i am following {following_count} users🍎 on GitHub.')
