import requests
import webbrowser
import time
import subprocess
from tkinter import Y
from numpy import size
import pyfiglet

cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
yellow = '\033[1;33;40m'
def ip_information():
    text = pyfiglet.figlet_format('IP TRACING', justify='center')
    print(red + text)
    ipinformation={}
    ip=input(yellow + "Enter your IP Address :: ")
    # Basically this is ip geolocation free api,here it provide a wide range of the data in json file.
    url="http://ip-api.com/json/"+ ip +"?fields=66846719"
    r=requests.get(url)
    # print(r.content)
    ipinformation=r.json()
    if ipinformation['status'] == 'success':
        lat=ipinformation['lat']
        lon=ipinformation['lon']        
        print(red+"Ip location Found !!")
        print(yellow +'Status      : ',ipinformation['status'])
        print(yellow +'Continent   : ',ipinformation['continent'])
        print(yellow +'Country     : ',ipinformation['country'])
        print(yellow +'City        : ',ipinformation['city'])
        print(yellow +'Time zone   : ',ipinformation['timezone'])
        if(ipinformation['proxy']==False):
            {
                print(yellow + "No proxy is used!")
            }
        else:
            print(yellow + 'The proxy is used!')
        print(cyan+'Opening Location in browser')
        time.sleep(5)
        mapurl = "https://maps.google.com/maps?q=%s,+%s" % (lat, lon)
        webbrowser.open(mapurl, new=2) 
        print('')
    else:
        print(red+"Ip location Not Found !!")
                
if __name__=="__main__":
    ip_information()