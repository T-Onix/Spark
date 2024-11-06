from time import sleep
import subprocess
import platform
import sys
import os


#for Windows====================================================================================================
if os.name == "nt":
    try:
        from colorama import Fore , init ;init()
        
    except (ImportError , ModuleNotFoundError):
        subprocess.call("pip install colorama" , shell=True)
        sys.exit()
              
#for termux ====================================================================================================
try:
    from colorama import Fore , init; init()
    
except (ImportError , ModuleNotFoundError):
    
    if platform.uname()[1] == "localhost" :
        print("\nYou may have missing libraries , colorama  !\n")
        subprocess.call("pkg install python-colorama" , shell=True)
        sleep(1)
        sys.exit()
    else:
        pass
#for Linux ====================================================================================================

else:
    try:
        from colorama import Fore , init ;init()
        
    except (ImportError , ModuleNotFoundError):
        try:
            print("\nYou may have missing libraries , colorama !")
            
            package_installer = input("\nEnter your package installer (like 'apt install' or 'pacman -S') >> ")
            python_v = input("\nYour linux using [1]python3 or [2]python for installing packages of python (Enter 1 or 2) >> ")
            if python_v == "1":
                subprocess.call(f"{package_installer} python3-colorama" ,  shell=True)
                sys.exit()
                
            elif python_v == "2":
                subprocess.call(f"{package_installer} python-colorama" ,  shell=True)
                sys.exit()
        except NameError:
            exit("\nWrong package installer name or python name !")
        except KeyboardInterrupt:
            exit("\n\nUser Exited :)")

#Run with Sudo command ====================================================================================================
def uid():
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
#smooth rotation====================================================================================================
def rotation(text):
    for _ in range(4):
        print(Fore.BLUE + "[\\]" ,text ,  end= "\r")
        sleep(0.7)
        print(Fore.RED + "[|]" , end= "\r")
        sleep(0.7)
        print(Fore.CYAN + "[/]" , end= "\r")
        sleep(0.7)
        print(Fore.GREEN + "[-]" , end= "\r" + Fore.RESET)
        sleep(0.7)
#Check php is installed ====================================================================================================
def check_php():
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