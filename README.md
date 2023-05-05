# salford_robot
A ROS2 Humble and Gazebo mobile robot 

#Dependency
1. Ubuntu 22.04
2. ROS2 Humble
	1. slam_toolbox
	2. nav2_bringup
	3. Xacro
	4. Joint state publisher
	5. Teleop twist
3. Gazebo
4. RViz2
5. Python 3.10

#Quick launch commands
After cloning the project in your /home directory...

#in one terminal
cd ~/salford_robot
source install/setup.bash
colcon build
ros2 launch salford_robot display.launch.py

#in one terminal
cd ~/salford_robot
source install/setup.bash
ros2 launch slam_toolbox online_async_launch.py

#in one terminal
cd ~/salford_robot
source install/setup.bash
ros2 launch nav2_bringup navigation_launch.py params_file:=/home/gabriel/salford_robot/config/nav2_params.yaml

#in another terminal
source /opt/ros/humble/setup.bash
ros2 launch nav2_bringup bringup_launch.py use_sim_time:=True autostart:=True map:=/home/gabriel/map.yaml

#in one terminal
ros2 run teleop_twist_keyboard teleop_twist_keyboard
//or
ros2 run teleop_twist_joy teleop_node

#To navigate to point (x, y, z) with orientation w, open another terminal
ros2 topic pub /goal_pose geometry_msgs/PoseStamped "{header: {stamp: {sec: 0}, frame_id: 'map'}, pose: {position: {x: 0.2, y: 3.0, z: 0.0}, orientation: {w: 1.0}}}"

#To save a SLAM map, open another terminal after your scan
source /opt/ros/galactic/setup.bash
ros2 run nav2_map_server map_saver_cli -f ~/map




