 #!/bin/bash

mkdir -p catkin_ws/src
cd catkin_ws/src
catkin_init_workspace
#catkin_create_pkg minecraft_bot std_msgs rospy roscpp
ln -s ../../minecraft_bot/ minecraft_bot
mkdir -p minecraft_bot/include/minecraft_bot/
cd ..
catkin_make
