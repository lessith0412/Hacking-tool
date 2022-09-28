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

text = pyfiglet.figlet_format('KeyLogger', justify='center')
print(brightred + text)

print("Lets view this in Virtual Box")


# Key Logger Script : Check the KeyLogger Folder