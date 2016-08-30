#-*-coding:utf-8 -*-

import sys
import config
from naoqi import ALProxy

def move(x,y,angle):
  ## flag=0 left flag=1 right
  motionProxy = config.loadProxy("ALMotion")

  #Set NAO in stiffness On
  # config.StiffnessOn(motionProxy)
  # config.PoseInit(motionProxy)

  #####################
  ## Enable arms control by Walk algorithm
  #####################
  motionProxy.setWalkArmsEnabled(True, True)
  #~ motionProxy.setWalkArmsEnabled(False, False)

  #####################
  ## FOOT CONTACT PROTECTION
  #####################
  #~ motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", False]])
  motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
  X = x*0.01
  Y = y*0.01
  Theta = angle
  motionProxy.post.walkTo(X, Y, Theta)
  # wait is useful because with post walkTo is not blocking function
  motionProxy.waitUntilWalkIsFinished()
