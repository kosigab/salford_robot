# salford_robot
A ROS2 Humble and Gazebo mobile robot 

#Quick launch commands

cd ~/salford_robot
source install/setup.bash
ros2 launch salford_robot display.launch.py

cd ~/salford_robot
source install/setup.bash
ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 map odom

cd ~/salford_robot
source install/setup.bash
ros2 launch slam_toolbox online_async_launch.py

cd ~/salford_robot
source install/setup.bash
ros2 launch nav2_bringup navigation_launch.py params_file:=/home/gabriel/salford_robot/config/nav2_params.yaml


ros2 run teleop_twist_keyboard teleop_twist_keyboard

ros2 run teleop_twist_joy teleop_node




