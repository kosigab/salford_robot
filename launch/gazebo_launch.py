import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

def generate_launch_description():
    gazebo_pkg_share_directory = get_package_share_directory('gazebo_ros')
    basic_mobile_robot_share_directory = get_package_share_directory('basic_mobile_robot')
    world_file_path = os.path.join(basic_mobile_robot_share_directory, 'worlds', 'basic_mobile_bot_world', 'third_world.sdf')

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so', '-s', 'libgazebo_ros_init.so', world_file_path],
            output='screen'
        )
    ])