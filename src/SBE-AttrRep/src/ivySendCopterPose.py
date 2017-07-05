#!/usr/bin/env python
import rospy
import geometry_msgs.msg
import math
from IvyCalibrationNode import *
from ivy.std_api import *


comm=IvyCalibrationNode()
comm.IvyInitStart()

try:
    while True:
        #do nothing
        pass
        #print('test')
except KeyboardInterrupt:
    print('\nROS initialization canceled by user')

comm.IvyInitStop()



