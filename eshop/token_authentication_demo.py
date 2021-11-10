import requests
from dotenv import load_dotenv
import os

load_dotenv()   

# REQUEST AND OBTAIN ACCESS TOKEN
token_endpoint = 'http://127.0.0.1:8000/api-token-auth/'
user_data = {"username":os.getenv('API_USER'), "password":os.getenv('API_PWD')}
print(user_data)
response = requests.post(token_endpoint, data = user_data)
response_data = response.json()
access_token = response_data['token']

# SEND ACCESS TOKEN
api_endpoint = 'http://127.0.0.1:8000/products/'
headers = {
    'Token' : access_token
}
response = requests.get(api_endpoint, headers=headers)
print(response.text)