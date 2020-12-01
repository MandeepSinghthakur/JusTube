

# read the input 

# pre process the input 

# feeed he inout 

#pro-process the output 

#feed the the output with process.///


import cv2
import numpy as np
import time 
import socket
import urllib.request
import sys

HOSTNAME = 'http://127.0.0.1'
PORT = 8080
data = "Hello from Blender"


def handshake(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))
    return sock


sock = handshake(HOSTNAME, PORT)

video = cv2.VideoCapture(0)

if video.isOpened():
    for i in range(int(1e12)):
        check, frame = video.read()
        if check:
            sock.send(bytes(data+"\n","utf8"))
        	#check here with framees. 
        	# time # apply filter here if needded but first play  simple conversion- what strcuture, algo to use- deecide priot->]]
        	# flow char --- check near  by fry's . 
            print(f'{i}.png', np.array(frame))
            #cv2.imwrite(f'{i}.png', np.array(frame))

        else:
            print('Frame not available')
            print(video.isOpened())
else:
    print("video not opened")