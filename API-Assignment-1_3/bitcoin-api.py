import sys
import json
import requests

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
json.loads(response.text)