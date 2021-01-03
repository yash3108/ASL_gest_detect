# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 11:50:45 2020

@author: shahy_mxyzd8u
"""


import urllib.request
import cv2 
import numpy as np 
import time 
 
url='http://192.168.100.8:8080/shot.jpg'
while True:
    #imgResp=urllib.request.urlopen(url) 
    #imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8) 
    #img=cv2.imdecode(imgNp,-1)  
    #cv2.imshow('IPWebcam',img) 
	cam = cv2.VideoCapture('http://192.168.0.101:4747/mjpegfeed')
   
	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break 