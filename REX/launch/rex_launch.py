# launch/rex_launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='REX',
            executable='main',
            output='screen'),
        Node(
            package='REX',
            executable='puces_sensors',
            output='screen'),
        Node(
            package='REX',
            executable='lidar_filtration',
            output='screen'),
        Node(
            package='REX',
            executable='fonction_deplacement_ros',
            output='screen'),
    ])