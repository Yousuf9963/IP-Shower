print("[+] Tool Namee:IP-SHOWER")

print("[+] Author:Yousuf Shafi'i Muhammad. Junior Programmer")

print("[+] Version:1.0")

print("[+] Team:Junior Programmers")

print("[+] Github:https://github.com/Yousuf9963/phone-num-info")

print("[+] Follow me on Github: https://github.com/Yousuf9963")

print("[-] Website muhammadabdirahman.wixsite.com/yousuf9963blog.")

print("[!] legal disclaimer: Usage of this Program for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.")

print("[+] I hope for you good future and i am willing that you will come high effort.")

print("")

import os
os.system("pip install socket")
os.system("pip install requests")
os.system("pip install colorama")
os.system("pip install time")
os.system("clear")
#_________________.
import requests
import time
import socket
import colorama
from colorama import Fore, init
import sys
#//////

init()

print (Fore.YELLOW+ """

_                 ____  _   _  _____        _______ ____ 

(_)_ __           / ___|| | | |/ _ \ \      / / ____|  _ \ 

| | '_ \   _____  \___ \| |_| | | | \ \ /\ / /|  _| | |_) | 

| | |_) | |_____|  ___) |  _  | |_| |\ V  V / | |___|  _ < 

|_| .__/          |____/|_| |_|\___/  \_/\_/  |_____|_| \_\ 

  |_|
  

""")


print("[+] Tool Namee:IP-SHOWER")

print("[+] Author:Yousuf Shafi'i Muhammad. Junior Programmer")

print("[+] Version:1.0")

print("[+] Team:Junior Programmers")

print("[+] Github:https://github.com/Yousuf9963/phone-num-info")

print("[+] Follow me on Github: https://github.com/Yousuf9963")

print("[-] Website muhammadabdirahman.wixsite.com/yousuf9963blog.")

print("[!] legal disclaimer: Usage of this Program for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.")

print("[+] I hope for you good future and i am willing that you will come high effort.")

print("")

print (Fore.BLUE+"""
OPTIONS:

[1] GET Your LOCAL IP Address

[2] GET Your PUBLIC IP Address {Global IP}""")
print("")
print(Fore.GREEN+"")

get = input("""ENTER YOUR OPTIONS 1 or 2
>_ """)

if get == "1":

        hostname = socket.gethostname()

        ip_local = socket.gethostbyname(hostname)
        print (Fore.RED+"PLEASE WAIT THANK YOU...")
        time.sleep(3.0)
        print (Fore.GREEN+"Your Local IP is:",Fore.RED + ip_local)
#.....$.$.$.$..$_..$.$
if get == "2":
        print (Fore.RED+"PLEASE WAIT THANK YOU...")
        time.sleep(3.0)
        public = requests.get("https://api.ipify.org").text
        print("")
        print("")
        time.sleep(3)
        print (Fore.GREEN+"Your Public IP is:",Fore.RED + public)
else:
        print (Fore.RED+'[×]'+Fore.YELLOW+' command invalid')
        input ('Press Enter for Exit')
        sys.exit()
         
