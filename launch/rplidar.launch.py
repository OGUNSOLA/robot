import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

package_name='rplidar_ros' 
def generate_launch_description():

    # Check if we're told to use sim time
    rplidar = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(package_name),'launch','rplidar_a1_launch.py'
        )])
      )

    # Launch!
    return LaunchDescription([
        rplidar
    ])

