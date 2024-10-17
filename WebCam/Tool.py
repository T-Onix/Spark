import sys ; sys.dont_write_bytecode = True
from colorama import Fore , init ; init()
from time import sleep
import subprocess
import os


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