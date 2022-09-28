import time
import sys
from tokenize import Number
from phonenumber import phonenum
from url import urlinfo

from webscrap import Links

cyan ='\033[1;36;40m'
font_negativecolor = '\033[3;37;40m'
brightred = '\033[1;31;40m'
yellow ='\033[1;33;40m'

import subprocess
from tkinter import Y
from numpy import size
import pyfiglet
from Iplocation import ip_information

def infogathering():
    text = pyfiglet.figlet_format('Information Gathering', justify='center')
    print(brightred + text)
    print(font_negativecolor + yellow + """
                Available Modules 
           
           1.Trace Single Ip,
           2.URL Information,
           3.Hidden Data Linked With Website,
           4.Information about Phone Number.
    """)
    i=int(input("Information>> "))
    if(i == 1):
        ip_information()
    elif(i == 2): 
        urlinfo()
    elif(i == 3):
        Links()
    elif(i == 4):
        phonenum()
    elif(i == 'exit'):
        exit()
    else:
        print(yellow + "Please check your Input!!!")
    # while True:
    #     infogathering()
if __name__=="__main__":
    infogathering()
    