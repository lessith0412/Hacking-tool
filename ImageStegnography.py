import cv2
import numpy as np
from PIL import Image
import subprocess
from tkinter import Y
from numpy import size
import pyfiglet

cyan ='\033[1;36;40m'
font_negativecolor = '\033[3;37;40m'
brightred = '\033[1;31;40m'
yellow ='\033[1;33;40m'
green ='\033[1;32;40m'

def data2binary(data):
    if type(data) == str:
        p = ''.join([format(ord(i), '08b')for i in data])
    elif type(data) == bytes or type(data) == np.ndarray:
        p = [format(i, '08b')for i in data]
    return p

def hidedata(img, data):
    data += "$$"                                   
    d_index = 0
    b_data = data2binary(data)
    len_data = len(b_data)

 #iterate pixels from image and update pixel values

    for value in img:
        for pix in value:
            r, g, b = data2binary(pix)
            if d_index < len_data:
                pix[0] = int(r[:-1] + b_data[d_index])
                d_index += 1
            if d_index < len_data:
                pix[1] = int(g[:-1] + b_data[d_index])
                d_index += 1
            if d_index < len_data:
                pix[2] = int(b[:-1] + b_data[d_index])
                d_index += 1
            if d_index >= len_data:
                break
    return img


def encode():
    img_name = input(green + "Enter image name to be encrypted:")
    image = cv2.imread(img_name)
    img = Image.open(img_name, 'r')
    w, h = img.size
    data = input(green + "Enter the Message:")
    if len(data) == 0:
        raise ValueError(brightred+"No message")
    enc_img = input(green + "Enter the name of encoded image:")
    enc_data = hidedata(image, data)
    cv2.imwrite(enc_img, enc_data)
    img1 = Image.open(enc_img, 'r')
    img1 = img1.resize((w, h),Image.ANTIALIAS)
    # optimize with 65% quality
    if w != h:
        img1.save(enc_img, optimize=True, quality=65)
    else:
        img1.save(enc_img)

# decoding

def find_data(img):
    bin_data = ""
    for value in img:
        for pix in value:
            r, g, b = data2binary(pix)
            bin_data += r[-1]
            bin_data += g[-1]
            bin_data += b[-1]

    all_bytes = [bin_data[i: i + 8] for i in range(0, len(bin_data), 8)]

    readable_data = ""
    for x in all_bytes:
        readable_data += chr(int(x, 2))
        if readable_data[-2:] == "$$":
            break
    return readable_data[:-2]


def decode():
    img_name = input(green + "Enter Image name : ")
    image = cv2.imread(img_name)
    img=Image.open(img_name,'r')
    msg = find_data(image)
    return msg


def stegnography():
    text = pyfiglet.figlet_format('IMAGE STEGNOGRAPHY', justify='center')
    print(brightred + text)
    print(cyan + 'Enter image with extension .png')
    x = 1
    while x != 0:
       print(yellow + '''Image Stegnography
       1.Encoding the Image
       2.Decoding the Image''')
       a = int(input(green + "Enter what you want to do!!:"))
       if a == 1:
           encode()
       else:
           ans = decode()
           print(green + "Encoded Message is :"+ans)
       x = int(input(green + "Enter 1 for continue otherwise 0 for Exit!!:"))
       if(x==0):
           print("Thanks")
if __name__=="__main__":
    stegnography()