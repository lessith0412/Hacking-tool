import requests
from bs4 import BeautifulSoup
import pyfiglet

cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
yellow = '\033[1;33;40m'
def Links():
    text = pyfiglet.figlet_format('Hidden Link Analysis', justify='center')
    print(text)
    print(yellow+"Note : http://example.com")
    url=input(cyan + "Enter the URL int this way (http://) ::  ")
    print('')
    print(green +"[+] Fetching links.....")
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    for link in soup.find_all('a'):
        lin=link.get('href')
        if(lin.startswith('http')):
            print(cyan+"[+] ",lin)
    print(green+"Fetched Successfully...")
    
if __name__=="__main__":
    Links()