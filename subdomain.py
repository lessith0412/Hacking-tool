import requests
import json
cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
yellow = '\033[1;33;40m'

import subprocess
from tkinter import Y
from numpy import size
import pyfiglet

def subdomain():
    text = pyfiglet.figlet_format('SubDomain Lookup', justify='center')
    print(text)
    dom=input(yellow + "Enter the url :: ")
    url="https://sonar.omnisint.io/subdomains/"+dom
    r=requests.get(url)
    print(cyan+"Finding Subdomain x) .....")
    for i in r.json():
        print(cyan+"[+]"+i)
    print(red+"Subdomain Enumeration Success")
if __name__=="__main__":
    subdomain()