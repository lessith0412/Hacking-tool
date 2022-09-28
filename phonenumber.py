import requests
import pyfiglet
cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
yellow = '\033[1;33;40m'

def phonenum():
  text = pyfiglet.figlet_format('Phone Number Information', justify='center')
  print(text)
  phonenum = input(yellow  + "Enter Mobile Number with country code ::  ")
  url = ("https://api.apilayer.com/number_verification/validate?number="+phonenum)

  payload = {}
  headers= {
  "apikey": "gEBQZ4srQhRvDG5fmMcQtoOp9KlD7MwR"
  }

  response = requests.request("GET", url, headers=headers, data = payload)

  status_code = response.status_code
  result = response.text
  print(red + 'The Response status and Results are::')
  print(response)
  print(result)

if __name__=="__main__":
    phonenum()