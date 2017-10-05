#!/usr/bin/env python

import rospy
import math

from std_msgs.msg import Float64
from math import sin,cos,atan2,sqrt,fabs

#RRArm joint positions publisher for joint controllers.
def rrarm_joint_positions_publisher():

	#Initialization of node for controlling joint1 and joint2 positions.
	rospy.init_node('joint_positions_node', anonymous=True)

	#Define publishers for joint1 and joint2 position controller commands.
	joint1publisher = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=10)
	joint2publisher = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=10)

	rate = rospy.Rate(100) #Rate 100 Hz

	#While loop to have joints follow the established trajectory, when rospy is not shutdown.
	i = 0
	while not rospy.is_shutdown():

		#Sine and cosine movement
		sine_movement = sin(i/100.)
                cosine_movement = cos(i/100.)

		#Publish the sine movement to each joint.
		joint1publisher.publish(sine_movement)
		joint2publisher.publish(cosine_movement)

		i = i+1

		rate.sleep() #Sleep for rest of rospy.Rate(100)

#Below code that will continuously run (to stop it press CTRL+C)
if __name__ == '__main__':
	try: rrarm_joint_positions_publisher()
	except rospy.ROSInterruptException: pass
