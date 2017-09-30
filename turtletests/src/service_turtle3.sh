#!/bin/sh
rosservice call /spawn 2 2 0.2 "turtle3" &
rostopic pub /turtle3/cmd_vel geometry_msgs/Twist -r 1 -- '[1.0, 0.0, 0.0]' '[0.0, 0.0, -1.0]'
