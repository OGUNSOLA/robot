import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node



def generate_launch_description():


    package_name='rplidar_ros'

    rplidar = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rplidar_a1_launch.py'
                )]), launch_arguments={'serial_port': '/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0','frame_id': 'laser_frame','angle_compensate': True,'scan_mode': 'Standard'}.items()
    )

    # Launch them all!
    return LaunchDescription([
        rplidar,
    ])
