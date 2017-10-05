#!/usr/bin/env python

import rospy
import math

from std_msgs.msg import Float64
from math import sin,cos,atan2,sqrt,fabs

#RRArm initial joint positions publisher for joint controllers.
def rrarm_initial_joint_positions_publisher():

	#Initialization of node for controlling joint1 and joint2 positions.
	rospy.init_node('joint_positions_node', anonymous=True)

	#Define publishers for joint1 and joint2 position controller commands.
	joint1publisher = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=10)
	joint2publisher = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=10)

	rate = rospy.Rate(80) #Rate 80 Hz

        while not rospy.is_shutdown():
                #print "Set initial position of the robotic arm\n"
		joint1initial_position = -2.0
		joint2initial_position = 0.5
		#Publish the sine movement to each joint.
		joint1publisher.publish(joint1initial_position)
		joint2publisher.publish(- joint2initial_position)
		rate.sleep() #Sleep for rest of rospy.Rate(80)

#Below code that will continuously run (to stop it press CTRL+C)
if __name__ == '__main__':
	try: rrarm_initial_joint_positions_publisher()
	except rospy.ROSInterruptException: pass
