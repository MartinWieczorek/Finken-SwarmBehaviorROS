#!/usr/bin/python2
import rospy
from ivy.std_api import *
from std_msgs.msg import String
from geometry_msgs.msg import Pose2D
import time
"""kill_log resides in the upper directory to this script"""
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)
import kill_log

class IvyCalibrationNode:
    def __init__(self):
        self.myKillLog = kill_log.KillLog()
    
    def IvyInitStart(self):
        """ Initializes the Ivy Server and ROS Subscriber

        Should only be called once per session.
        """
        try:
            IvyInit('Calibration Node', '', 0)
        except AssertionError:
            print('Assertion Error in IvyInit(!= none), is there a server already running? Exiting')
            IvyStop()
            raise SystemExit()
        IvyStart()
        try:
            self.initRosSub()
        except rospy.exceptions.ROSInitException as e:
            print('\nInitialization failed due to ROS error, exiting...')
            self.IvyInitStop()
        time.sleep(1)
        print('Ivy Calibration Node ready!')
	# initial value for oldTime
	global oldTime 
	oldTime = rospy.get_rostime()
	global oldX
	oldX = 0
	global oldY
	oldY = 0
	global oldZ
	oldZ = 0


    def IvyInitStop(self):
        """Stops the Ivy Server.
        """
        time.sleep(1)
        IvyStop()


    def handlePos(self, data):
        """ Callback for the ROS subscriber.


        """
        global oldTime
	global oldX
	global oldY
	global oldZ

	# offsets for Latitude = 52.1205 and Longitude = 11.6276 (Rotation across Y and Z)
	offsetX =  0.601406 * data.x - 0.123752 * data.y
	offsetY = -0.201549 * data.x + 0.979478 * data.y
	offsetZ = -0.773103 * data.x + 0.159083 * data.y
	
	rospy.loginfo("Offsets %f, %f, %f", offsetX, offsetY, offsetZ)

	# getting time difference between now and last run
	now = rospy.get_rostime()
	timediff = 0
	if( (now.secs - oldTime.secs) == 0):
		timediff = now.nsecs - oldTime.nsecs
	else:
		timediff = 1000000000 + now.nsecs - oldTime.nsecs
	oldTime = now
	timediff = timediff / 1000000000.0
	
	rospy.loginfo("timediff float %f", timediff)

	# geting difference for X pos and Y pos and Z pos and calculate speed
	
	ecef_xd= (offsetX - oldX) / timediff	
	ecef_yd= (offsetY - oldY) / timediff	
	ecef_zd= (offsetZ - oldZ) / timediff	
	
	rospy.loginfo("Speeds %f, %f, %f", ecef_xd, ecef_yd, ecef_zd)

	oldX = offsetX
	oldY = offsetY
	oldZ = offsetZ


                             #AC_ID, numsv, ecef_x, ecef_y, ecef_z, 					     lat, lon, alt, hmsl, ecef_xd, ecef_yd, ecef_zd, tow, course
        self.IvySendRemoteGPS(1,     0,     384202400 + offsetX, 79186300 + offsetY, 501229700 + offsetZ,      0,   0,   0,   0,  ecef_xd, ecef_yd, ecef_zd,   0,   0)


    def initRosSub(self):
        """ Initializes the ROS subscriber.

        Is automatically called during the Ivy initialization process
        in IvyInitStart().
        """
        try:
            rospy.init_node('poseListener', anonymous=False)
        except KeyboardInterrupt:
            print('\nROS initialization canceled by user')
        except rospy.exceptions.ROSInitException as e:
            print('\nError Initializing ROS:')
            print(str(e))
            raise

        rospy.Subscriber("copters/0/pose", Pose2D, self.handlePos)


    def IvyGetPos(self):
        """Simply returns the position grabbed via ROS to the caller

        """
        try:
            return copterPos
        except NameError as e:
            print("CopterPos not yed defined! (No data from ROS?):")
            print(str(e))

    def IvyGetPosList(self):
        """Returns the position to a list for less dependency with ros
           Returns
           -------
           List
        """
        position = self.IvyGetPos()
        return [position.x, position.y, position.theta]

    def IvySendCalib(self,param_ID, AC_ID, value):
        """Sends the given parameter via Ivy

        AC_ID:      ID of the aricraft to be calibrated
        param_ID:   ID of the parameter to be calibrated
                     phi   = 58 roll
                     theta = 59 pitch
                     psi   = 60 yaw
        value:      value to be set for the parameter !in degrees!
        """
        print("sending calib msg")
        IvySendMsg('dl SETTING %d %d %f' %
                    (AC_ID,
                    param_ID,
                    value
                    ))


    def IvySendKill(self, AC_ID):
        """Sends a kill message to the aircraft

        """
        IvySendMsg('dl KILL %d 1' %
                    (AC_ID
                    ))
        
    def SetInDeadZone(self,inDeadZone):
        self.myKillLog.inDeadZone = inDeadZone

    def IvySendCalParams(self, AC_ID, turn_leds, roll, pitch, yaw):
        IvySendMsg('dl CALPARAMS %d %d %f %f %f' %
                    (AC_ID, turn_leds, roll, pitch, yaw
                    ))

    def IvySendCopterPose(self, AC_ID, posX, posY, theta):
        IvySendMsg('dl COPTERPOSE %d %f %f %f' %
                    (AC_ID, posX, posY, theta
                    ))


    def IvySendRemoteGPS(self, AC_ID, numsv, ecef_x, ecef_y, ecef_z, lat, lon, alt, hmsl, ecef_xd, ecef_yd, ecef_zd, tow, course):
        IvySendMsg('dl REMOTE_GPS %d %d %d %d %d %d %d %d %d %d %d %d %d %d' %
                    (AC_ID, numsv, ecef_x, ecef_y, ecef_z, lat, lon, alt, hmsl, ecef_xd, ecef_yd, ecef_zd, tow, course
                    ))



    def IvySendUnKill(self, AC_ID):
        """Sends an unkill message to the aircraft

        """
        IvySendMsg('dl KILL %d 0' %
                    (AC_ID
                    ))



    def IvySendSwitchBlock(self, AC_ID, block_ID):
        """Sends a message to switch the flight plan

        """
        IvySendMsg('dl BLOCK %d %d' %
                    (block_ID,
                     AC_ID,
                     ))
                     
    def SaveIvyKillLog(self):
        self.myKillLog.saveLog()
