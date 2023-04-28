# salford_robot
A ROS2 Humble and Gazebo mobile robot 

#Quick launch commands

cd ~/salford_robot

source install/setup.bash

ros2 launch salford_robot display.launch.py

cd ~/salford_robot

source install/setup.bash


ros2 launch nav2_bringup navigation_launch.py

cd ~/salford_robot

source install/setup.bash


ros2 launch slam_toolbox online_async_launch.py

rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/demo/cmd_vel



