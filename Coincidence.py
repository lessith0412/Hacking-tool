cyan ='\033[1;36;40m'
font_negativecolor = '\033[3;37;40m'
brightred = '\033[1;31;40m'
yellow ='\033[1;33;40m'
brightmagenta ='\033[1;35;40m'
brightblue='\033[1;34;40m'

import subprocess
from tkinter import Y
from numpy import size
import pyfiglet
from InfoGathermainpage import infogathering
from ImageStegnography import stegnography
from Webmodule import webmodule

def Coincidence(a):
    if(a==1):
        infogathering()
    elif(a==2):
        webmodule()
    elif(a==3):
        stegnography()
    elif(a==4):
        print(cyan + 'Key Logger x)')
        print('Lets view this in Virtual Box!!')

    else:
        print(cyan + 'Please Select the Correctly')

if __name__=="__main__":
    text = pyfiglet.figlet_format('Coincidence', justify='center')
    print(brightred + text)
    print(brightblue + "                           Created By : Shreel Trivedi & Jainam Shah")
    print(brightmagenta + """
            Available Modules 
           
           1.Information gathering,
           2.Web vulnerability scanning,
           3.Image Stegnography,
           4.Key logger,
    """) 
    a=int(input(brightred + "Enter the Module >> "))
    Coincidence(a)