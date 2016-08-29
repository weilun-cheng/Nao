# -*-coding:utf-8 -*-
import naoqi
import Image
import time
import cv2
import numpy as np
from naoqi import ALProxy
import math
IP="169.254.76.111"
PORT=9559

def getImage(IP, PORT, flag):
    camProxy = ALProxy("ALVideoDevice", IP, PORT)
    resolution = 2  ## VGA
    colorSpace = 11  ## RGB
    ##转换摄像头
    camProxy.setParam(18, flag)
    videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)
    # Get a camera image.
    # image[6] contains the image data passed as an array of ASCII chars.
    t0 = time.time()
    naoImage = camProxy.getImageRemote(videoClient)
    t1 = time.time()
    print "acquisition delay", t1 - t0
    camProxy.unsubscribe(videoClient)
    # package.
    # Get the image size and pixel array.
    imageWidth = naoImage[0]
    imageHeight = naoImage[1]
    array = naoImage[6]
    # Create a PIL Image from our pixel array.
    im = Image.fromstring("RGB", (imageWidth, imageHeight), array)
    ci = np.array(im)  ##转化成numpy格式图像
    r, g, b = cv2.split(ci)  ##opencv的图像为BGR因此需要转换一下
    ci = cv2.merge([b, g, r])
    return ci

def check(IP, PORT, flag):
    detection = 0
    counter=0
    frame = getImage(IP, PORT, flag)
    frame = cv2.pyrMeanShiftFiltering(np.asarray(frame), 10.0, 35.0)
    frame = cv2.blur(frame, (5, 5))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([35, 43, 46])
    upper_green = np.array([77, 255, 255])
    lower_red = np.array([0, 43, 46])
    upper_red = np.array([10, 255, 255])
    lower_red2 = np.array([156, 43, 46])
    upper_red2 = np.array([180, 255, 255])
    Rmask1 = cv2.inRange(hsv, lower_red, upper_red)
    Rmask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    Gres = cv2.inRange(hsv, lower_green, upper_green)
    Rres = cv2.bitwise_or(Rmask1, Rmask2)
    res = cv2.bitwise_or(Gres, Rres)
    ret, binary = cv2.threshold(res, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
        a = cv2.contourArea(contours[i], False)
        b = cv2.arcLength(contours[i], False)
    	c = cv2.moments(contours[i])
    	# if b != 0 and 200 < a < 76800:
     #    	d = c['mu11'] / (c['m00'] * c['m00'])
     #    	print b * b / a, a, c['nu20'], c['nu02']
     #    	if flag == 0 and (10 < b * b / a < 35) and (3000 > a > 200) and (0.02 < c['nu20'] < 0.05) and (0.20 < c['nu02'] < 0.37):
     #    		detection = 1
     #    		break
     #    	if flag==1 and (10 < b * b / a < 35) and (10000 > a > 1000) and (c['nu02'] / c['nu20'] > 4):
     #    		detection=1
     #    		break
     	if cv2.contourArea(contours[i])>counter:
	 		counter=cv2.contourArea(contours[i])
	 		detection=1
	 		point=i
    return detection

def GetCenter(IP, PORT, flag):
    detection = 0
    frame = getImage(IP, PORT, flag)
    frame = cv2.pyrMeanShiftFiltering(np.asarray(frame), 10.0, 35.0)
    # frame = cv2.blur(frame, (5, 5))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([35, 43, 46])
    upper_green = np.array([77, 255, 255])
    lower_red = np.array([0, 43, 46])
    upper_red = np.array([10, 255, 255])
    lower_red2 = np.array([156, 43, 46])
    upper_red2 = np.array([180, 255, 255])
    Rmask1 = cv2.inRange(hsv, lower_red, upper_red)
    Rmask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    Gres = cv2.inRange(hsv, lower_green, upper_green)
    Rres = cv2.bitwise_or(Rmask1, Rmask2)
    res = cv2.bitwise_or(Gres, Rres)
    res= cv2.medianBlur(res,5) 
    ret, binary = cv2.threshold(res, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    point=0
    counter=0
    for i in range(len(contours)):
    #     a = cv2.contourArea(contours[i], False)
    #     b = cv2.arcLength(contours[i], False)
    #     c = cv2.moments(contours[i])
    # 	# if b != 0 and 200 < a < 76800:
    #     d = c['mu11'] / (c['m00'] * c['m00'])
    #     print b * b / a, a, c['nu20'], c['nu02']
    #     if flag == 0 and (10 < b * b / a < 35) and (3000 > a > 200) and (0.02 < c['nu20'] < 0.05) and (0.20 < c['nu02'] < 0.37):
    #     	point=i
    #     	break
    #     if flag==1 and (10 < b * b / a < 35) and (10000 > a > 1000) and (c['nu02'] / c['nu20'] > 4):
    #     	point=i
    #     	break
    # 	if cv2.contourArea(contours[i])>counter:
	 		# counter=cv2.contourArea(contours[i])
	 		# point=i
  		d=cv2.minAreaRect(contours[i])
  		if d[1][1]!=0.0 and d[1][0]!=0.0:
                    if (d[1][0]/d[1][1])>5.4 and (d[1][0]/d[1][1])<6 and cv2.contourArea(contours[i])>(d[1][1]*d[1][0]*0.8):
                        point=contours[i]
                        detection=1
    c = cv2.moments(contours[point])
    y= c['m10'] / c['m00']
    x = c['m01'] / c['m00']
    # cv2.drawContours(frame,contours[point],-1,(0,0,255),3)
    print (x,y)
    # cv2.namedWindow('image')
    # while(1):
  		# cv2.imshow('image',frame)
  		# if cv2.waitKey(20)&0xFF==27:
  		# 	break
    # cv2.destoryAllWindows()
    return (x, y)

def GetArea(IP, PORT, flag):
    detection = 0
    frame = getImage(IP, PORT, flag)
    frame = cv2.pyrMeanShiftFiltering(np.asarray(frame), 10.0, 35.0)
    frame = cv2.blur(frame, (5, 5))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([35, 43, 46])
    upper_green = np.array([77, 255, 255])
    lower_red = np.array([0, 43, 46])
    upper_red = np.array([10, 255, 255])
    lower_red2 = np.array([156, 43, 46])
    upper_red2 = np.array([180, 255, 255])
    Rmask1 = cv2.inRange(hsv, lower_red, upper_red)
    Rmask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    Gres = cv2.inRange(hsv, lower_green, upper_green)
    Rres = cv2.bitwise_or(Rmask1, Rmask2)
    res = cv2.bitwise_or(Gres, Rres)
    ret, binary = cv2.threshold(res, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
        a = cv2.contourArea(contours[i], False)
        b = cv2.arcLength(contours[i], False)
    	c = cv2.moments(contours[i])
    	if b != 0 and 200 < a < 76800:
        	d = c['mu11'] / (c['m00'] * c['m00'])
        	print b * b / a, a, c['nu20'], c['nu02']
        	if flag == 0 and (10 < b * b / a < 35) and (3000 > a > 200) and (0.02 < c['nu20'] < 0.05) and (0.20 < c['nu02'] < 0.37):
        		point=i
        		break
        	if flag==1 and (10 < b * b / a < 35) and (10000 > a > 1000) and (c['nu02'] / c['nu20'] > 4):
        		point=i
        		break
    return cv2.countourArea(contours[point])

def check2(IP, PORT, flag):
    detection = 0
    frame = getImage(IP, PORT, flag)
    frame = cv2.pyrMeanShiftFiltering(np.asarray(frame), 10.0, 35.0)
    frame = cv2.blur(frame, (5, 5))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 46])
    mask = cv2.inRange(hsv, lower_black, upper_black)
    res = cv2.bitwise_or(Gres, Rres)
    ret, binary = cv2.threshold(res, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
  		d=cv2.minAreaRect(contours[i])
  		if d[1][1]!=0.0 and d[1][0]!=0.0:
                    if (d[1][1]/d[1][0])>1.4 and (d[1][1]/d[1][0])<1.6 and cv2.contourArea(contours[i])>(d[1][1]*d[1][0]*0.8):
                        point=contours[i]
                        detection=1
    return detection

# center=GetCenter(IP,PORT,0)