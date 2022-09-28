from urllib.request import urlopen
import subprocess
from tkinter import Y
from numpy import size
import pyfiglet

cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
yellow = '\033[1;33;40m'
def ClickJacking():
    text = pyfiglet.figlet_format('Click Jacking', justify='center')
    print(text)
    host=input(green + "Enter the website to Check :: ")
    port=int(input(green + "Enter port :: "))
    if port == 80:
          port = 'http://'
    elif port == 443:
          port = 'https://'
    else:
         print(red + "Could'nt fetch data for the given PORT")


    url = (port+host)

    data = urlopen(url)
    headers = data.info()

    if not "X-Frame-Options" in headers:
          print(yellow+"Website is vulnerable to ClickJacking")

    else:
        print(yellow+"Website is not Vulnerable to ClickJacking")
if __name__=="__main__":
    print(cyan + '80 if it is HTTP and 443 if it is HTTPS')
    ClickJacking()