# REX/setup.py
from setuptools import setup, find_packages

package_name = 'REX'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(),  # Automatically find packages and sub-packages
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/rex_launch.py']),
    ],
    install_requires=[
        'setuptools',
        'pyserial',
        'matplotlib',
        # 'time' and 'math' are built-in modules and do not need to be installed
    ],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your.email@example.com',
    description='REX ROS 2 package for robot control',
    license='License Declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'main = main:main',
            'puces_sensors = puces_sensors:main',
            'lidar_filtration = lidar_filtration:main',
            'fonction_deplacement_ros = serialusm2m.fonction_deplacement_ros:main',
        ],
    },
)

