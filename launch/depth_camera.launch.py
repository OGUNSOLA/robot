import os

from launch import LaunchDescription
from launch_ros.actions import Node

 
def generate_launch_description():
    
    return LaunchDescription([

        Node(
            package='realsense2_camera',
            executable='realsense2_camera_node',
            output='screen',
            namespace='camera',
            parameters=[{
                'camera_frame_id': 'camera_link_optical',
                }]
    )
    ])