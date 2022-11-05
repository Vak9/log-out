import time
import os
import colorama
from colorama import Fore
    
#print name 
name = input("Enter your name: ")
print(f"Hello {name}")
#time
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(Fore.RED + timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
#print
        os.system('cls')
    for i in range(200):
     print(Fore.RED + f"Goodbye {name}")
    time.sleep(1)
#logoff
    os.system("shutdown /l") #logoff
    time.sleep(3)

countdown(10)











