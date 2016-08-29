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
import grab

IP = "169.254.76.111" # set your Ip adress here
PORT = 9559

high=480
wide=640

def main(IP,PORT):
    posinit.posinit()
    tts = ALProxy("ALTextToSpeech", IP, PORT)
    tts.say("Hello!")
    posinit.posinit()
    center=detection.GetCenter(IP,PORT,0)
    while (center[0] > (wide/2+10)) or (center[0] < (wide/2-10)):
        if center==(0,0):
            center=detection.GetCenter(IP,PORT,0)
            print center
            continue
        if center[0] > (wide/2+10):
            moveto.move(0,-2,0)
            tts.say("found the bar,check the x position")
            print "found the bar,check the x position"
        elif center[0] < (wide/2-10):
            moveto.move(0,2,0)
            tts.say("found the bar,check the x position")
            print "found the bar,check the x position"
        center=detection.GetCenter(IP,PORT,0)
        print center
    center=detection.GetCenter(IP,PORT,0)
    print "Found the bar"
    tts.say("found the bar")
    while center!=(0,0):
        moveto.move(6,0.1,0)
        center=detection.GetCenter(IP,PORT,0)
        print center
    center=detection.GetCenter(IP,PORT,0)
    while center!=(0,0):
        moveto.move(6,0.1,0)
        center=detection.GetCenter(IP,PORT,0)
    tts.say("change camera")
    print "change camera"
    

    posinit.posinit()
    center=detection.GetCenter(IP,PORT,1)
    while (center[0] > (wide/2+10)) or (center[0] < (wide/2-10)):
        if center==(0,0):
            center=detection.GetCenter(IP,PORT,1)
            print center
            continue
        if center[0] > (wide/2+10):
            moveto.move(0,-2,0)
            tts.say("found the bar,check the position")
            print "found the bar,check the x position"
        elif center[0] < (wide/2-10):
            moveto.move(0,2,0)
            tts.say("found the bar,check the position")
            print "found the bar,check the x position"
        center=detection.GetCenter(IP,PORT,1)
        print center
    center=detection.GetCenter(IP,PORT,1)
    while center[0]<320 or center[0]>340 or center[1]>285 or center[1]<220:
        DeltaX=int((330-center[0])/15)
        DeltaY=int((250-center[1])/20)
        moveto.move(DeltaX,DeltaY,0)
    print "ready to grab"
    tts.say("ready to grab")
    grab.grab(IP,PORT)

if __name__ == '__main__':
    IP="169.254.76.111"
    PORT=9559
    naoImage = main(IP, PORT)

