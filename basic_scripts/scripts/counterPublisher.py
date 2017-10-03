#!/usr/bin/env python
## Simple talker demo that published std_msgs/Strings messages
## to the 'counterTopic' topic

import rospy
from std_msgs.msg import String

def counterPublisher():
    pub = rospy.Publisher('counterTopic', String, queue_size=100)
    rospy.init_node('counterPublisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    counter = 0
    counter_str = ""
    
    while not rospy.is_shutdown():
        counter_str = ""+str(counter)+":"
        publisher_str = "%s %s" % (counter_str, rospy.get_time())
        rospy.loginfo(publisher_str)
        pub.publish(publisher_str)
        counter += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        counterPublisher()
    except rospy.ROSInterruptException:
        pass
