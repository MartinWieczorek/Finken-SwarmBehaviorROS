#!/usr/bin/env python
import rospy
import geometry_msgs.msg
import math

copterPos0 = geometry_msgs.msg.Pose2D(0,0,0)
copterPos1 = geometry_msgs.msg.Pose2D(0,0,0)

def calcForce(copterPos0, copterPos1):
    cons = 1
    d=0.2
    diff_x = copterPos1.x - copterPos0.x
    rospy.loginfo("copter0PoseX %f   - copter1PoseX %f   = diff_x %f", copterPos0.x, copterPos1.x, diff_x)
    diff_y = copterPos1.y - copterPos0.y
    rospy.loginfo("copter0PoseY %f   - copter1PoseY %f   = diff_y %f", copterPos0.y, copterPos1.y, diff_y)
    dist = math.sqrt((diff_x*diff_x) + (diff_y*diff_y))

    rospy.loginfo("distance %f  ", dist)

    Fx = -cons*(dist-d) * diff_x
    Fy = -cons*(dist-d) * diff_y
    rospy.loginfo("Fx= %f , Fy= %f", Fx, Fy)

    return [Fx,Fy]
    

def copter0(data):
    global copterPos0
    global copterPos1
    copterPos0 = data
    force = calcForce(copterPos1, copterPos0)
    

def copter1(data):
    global copterPos0
    global copterPos1
    copterPos1 = data
    force = calcForce(copterPos0, copterPos1)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('AttrRep', anonymous=True)

    rospy.Subscriber("copters/0/pose", geometry_msgs.msg.Pose2D, copter0)
    rospy.Subscriber("copters/1/pose", geometry_msgs.msg.Pose2D, copter1)
    #time.sleep(0.5)
	
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


    
    

if __name__ == '__main__':
    listener()
