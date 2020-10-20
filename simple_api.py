import requests
import json

def getData():
    x = requests.get('https://reqres.in/api/users/2')
    response = json.loads(x.text)
    print(response['data']['email'])   
    return x.text

getData()