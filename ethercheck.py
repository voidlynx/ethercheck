from colorama import init, Style, Fore
from datetime import datetime
from time import sleep
import subprocess
init()
hostname = '1.1.1.1'
cmd = 'ping -c 4 -w 5 ' + hostname
prevresp = 99 #random number above 2
print(f'{Fore.LIGHTBLUE_EX}[{datetime.now()}] Started ethercheck.{Style.RESET_ALL}')

def ping(cmd):
    proc = subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    #print(proc) # for debug purposes
    return proc

while True:
    resp = ping(cmd)
    if resp != prevresp:
        if resp == 0:   # good
            print(f"{Fore.GREEN}[{datetime.now()}] Response recieved, connection up.{Style.RESET_ALL}")
            prevresp = resp
        elif resp == 1: # error
            print(f"{Fore.RED}[{datetime.now()}] Can't ping, connection down.{Style.RESET_ALL}")
            prevresp = resp
        elif resp == 2: # something is wrong
            print(f"{Fore.YELLOW}[{datetime.now()}] Ping sent, but no response, remote down?{Style.RESET_ALL}")
    sleep(60) 
