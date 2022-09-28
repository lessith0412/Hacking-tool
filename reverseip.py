from requests import get
import subprocess
from tkinter import Y
from numpy import size
import pyfiglet

cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
yellow = '\033[1;33;40m'
def ReverseIP():
    text = pyfiglet.figlet_format('Reverse IP ', justify='center')
    print(text)
    host=input(green+ "Enter the IP address :: ")
    # This is the website for the reverse ip look up
    lookup = 'https://api.hackertarget.com/reverseiplookup/?q=%s' % host
    try:
        result = get(lookup).text
        print(cyan+result)
    except:
        print(red+'Invalid IP address')
if __name__=="__main__":
    ReverseIP()