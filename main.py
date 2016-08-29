#using UTF-8
import math
import naoqi
import numpy
import cv2
import moveto
import detection
import config
import posinit
from naoqi import ALProxy

##Xupper=
##Xlower=
##Yupper=
##Ylower=
IP = "169.254.76.111" # set your Ip adress here
PORT = 9559

high=detection.getImage(IP,PORT,0).shape[0]
wide=detection.getImage(IP,PORT,0).shape[1]

def main(IP,PORT):
    posinit.posinit()
    tts = ALProxy("ALTextToSpeech", IP, PORT)
    tts.say("Hello!")
    posinit.posinit()
    center=(0,0)
    while (center[1] > (wide/2+10)) or (center[1] < (wide/2-10)):
        if detection.check(IP,PORT,0)==1:
            center=detection.GetCenter(IP,PORT,0)
            print detection
            tts.say("found the bar,check the position")
##        else:
##            posinit.posinit2(45,0)
##            if detection.check(IP,PORT,0)==1 :
##                center=detection.GetCenter(IP,PORT,0)
##            else:
##                posinit.posinit2(-45,0)
##                if detection.check(IP,PORT,0)==1:
##                    center=detection.GetCenter(IP,PORT,0)
        posinit.posinit()
        if center[1] > (wide/2+10):
            moveto.move(0,3,0)
            tts.say("found the bar,check the position")
        elif center[1] < (wide/2-10):
            moveto.move(0,-3,0)
        else:
            break
    center=detection.GetCenter(IP,PORT,0)
    print "Found the bar"
    tts.say("found the bar")
   
    moveto.move(30,0,0)
    posinit.posinit()
    center=GetCenter(IP,PORT,1)
##    while Xlower>center[0] and center[0]>Xupper and Ylower>center[1] and center[1]>Yupper:
##        moveto.move((center[0]-wide/2)/50,(center[1]-high/2)/50,0)
##    grab.grab(IP,PORT)

if __name__ == '__main__':
    IP="169.254.76.111"
    PORT=9559
    naoImage = main(IP, PORT)

