#!/bin/sh
rosservice call /spawn 2 2 0.2 "turtle2" &
rostopic pub /turtle2/cmd_vel geometry_msgs/Twist -r 1 -- '[3.0, 0.0, 0.0]' '[0.0, 0.0, 2.0]'
