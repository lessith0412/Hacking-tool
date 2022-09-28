import time
import sys

from clickjack import ClickJacking
from hostheader import HostHeader
from reverseip import ReverseIP
from subdomain import subdomain

cyan ='\033[1;36;40m'
font_negativecolor = '\033[3;37;40m'
brightred = '\033[1;31;40m'
yellow ='\033[1;33;40m'

import subprocess
from tkinter import Y
from numpy import size
import pyfiglet

def webmodule():
    text = pyfiglet.figlet_format('Web Vulnerability Scanning', justify='center')
    print(brightred + text)
    print(font_negativecolor + yellow + """
                Available Modules 
           
           1.Click Jacking,
           2.Reverse Ip,
           3.Host Header Injection,
           4.Subdomain Extractor.
    """)
    i=int(input("Information>> "))
    if(i == 1):
        ClickJacking()
    elif(i == 2):
        ReverseIP()
    elif(i == 3):
        HostHeader()
    elif(i == 4):
        subdomain()
    elif(i == 'exit'):
        exit()
    else:
        print(yellow + "Please check your Input!!!")
    # while True:
    #     infogathering()
if __name__=="__main__":
    webmodule()
    