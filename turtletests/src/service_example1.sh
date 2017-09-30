#!/bin/bash
roscore &
sleep 1 &&
rosrun turtlesim turtlesim_node &
rostopic pub /turtle1/cmd_vel geometry_msgs/Twist -r 1 -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, -1.8]' &
sleep 1 &&
gnome-terminal -x ./service_turtle2.sh &
sleep 1 &&
gnome-terminal -x ./service_turtle3.sh 
