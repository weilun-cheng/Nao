# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([5.8, 9.4, 12.2])
keys.append([-0.17, -0.162396, -0.162396])

names.append("HeadYaw")
times.append([5.8, 9.4, 12.2])
keys.append([0, 0, 0])

names.append("LAnklePitch")
times.append([5.8, 9.4, 12.2])
keys.append([0.09, 0.0859743, 0.0859743])

names.append("LAnkleRoll")
times.append([5.8, 9.4, 12.2])
keys.append([-0.13, -0.124185, -0.124185])

names.append("LElbowRoll")
times.append([5.8, 9.4, 12.2, 18.8])
keys.append([-0.400387, -0.0376942, -0.0376942, -1.22522])

names.append("LElbowYaw")
times.append([5.8, 9.4, 12.2, 18.8])
keys.append([-1.18954, -2.08039, -2.08039, -0.785398])

names.append("LHand")
times.append([5.8, 9.4, 12.2, 18.8])
keys.append([0.3, 0.3, 0.3, 0.18])

names.append("LHipPitch")
times.append([5.8, 9.4, 12.2])
keys.append([0.13, 0.124185, 0.124185])

names.append("LHipRoll")
times.append([5.8, 9.4, 12.2])
keys.append([0.1, 0.095527, 0.095527])

names.append("LHipYawPitch")
times.append([5.8, 9.4, 12.2])
keys.append([-0.17, -0.162396, -0.162396])

names.append("LKneePitch")
times.append([5.8, 9.4, 12.2])
keys.append([-0.09, -0.09, -0.09])

names.append("LShoulderPitch")
times.append([5.8, 9.4, 12.2])
keys.append([1.46967, 0.973191, 0.969954])

names.append("LShoulderRoll")
times.append([5.8, 9.4, 12.2, 18.8])
keys.append([1.31692, 1.31472, 0.829967, 0.298451])

names.append("LWristYaw")
times.append([5.8, 9.4, 12.2, 18.8])
keys.append([0.1, 0.0994865, 0.0994865, -0.528835])

names.append("RAnklePitch")
times.append([5.8, 9.4, 12.2])
keys.append([0.09, 0.0859743, 0.0859743])

names.append("RAnkleRoll")
times.append([5.8, 9.4, 12.2])
keys.append([0.13, 0.124185, 0.124185])

names.append("RElbowRoll")
times.append([5.8, 9.4, 12.2, 18.8])
keys.append([0.400159, 0.0376942, 0.0406713, 1.22522])

names.append("RElbowYaw")
times.append([5.8, 9.4, 12.2, 18.8])
keys.append([1.18272, 2.08264, 2.08264, 0.785398])

names.append("RHand")
times.append([5.8, 9.4, 12.2, 18.8])
keys.append([0.3, 0.3, 0.3, 0.18])

names.append("RHipPitch")
times.append([5.8, 9.4, 12.2])
keys.append([0.13, 0.124185, 0.124185])

names.append("RHipRoll")
times.append([5.8, 9.4, 12.2])
keys.append([-0.1, -0.095527, -0.095527])

names.append("RHipYawPitch")
times.append([5.8, 9.4, 12.2])
keys.append([-0.17, -0.162396, -0.162396])

names.append("RKneePitch")
times.append([5.8, 9.4, 12.2])
keys.append([-0.09, -0.09, -0.09])

names.append("RShoulderPitch")
times.append([5.8, 9.4, 12.2])
keys.append([1.51135, 0.973191, 0.982637])

names.append("RShoulderRoll")
times.append([5.8, 9.4, 12.2, 18.8])
keys.append([-1.31692, -1.31472, -0.829967, -0.298451])

names.append("RWristYaw")
times.append([5.8, 9.4, 12.2, 18.8])
keys.append([0.1, 0.0994865, 0.0994865, 0.528835])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion","169.254.76.111",9559)
  motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
  print err
