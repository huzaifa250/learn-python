# script use to send authorization header by  Basic Auth
import requests
from requests.auth import HTTPBasicAuth

url = 'https://example.com'
username = 'user123'
password = 'mypassword'

response = requests.get(url, auth=HTTPBasicAuth(username, password))

print(response.json())
