# REX/main.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Import modules directly
import system
import leds_serial
import camera
import visualization
from serialusm2m import AX_GET_pos
from serialusm2m import calage_start
from serialusm2m import Fonction_AX
from serialusm2m import fonction_deplacement2
from serialusm2m import fonction_deplacement
from serialusm2m import fonction_deplacement_ros
from serialusm2m import fonction_PID
from serialusm2m import fonction_Pos_Calage
from serialusm2m import GPIOREADALL
from serialusm2m import _serialusM2M_py_ as serialusM2M_special
from serialusm2m import serialusM2M

class MainNode(Node):
    def __init__(self):
        super().__init__('main_node')
        # Subscribe to 'evitement' topic
        self.subscription = self.create_subscription(
            String,
            'evitement',
            self.evitement_callback,
            10)
        self.subscription  # prevent unused variable warning

    def evitement_callback(self, msg):
        pass  # Empty callback function

    def main_logic(self):
        # Use functions from imported modules
        pass

def main(args=None):
    rclpy.init(args=args)
    node = MainNode()
    node.main_logic()  # Call the main logic
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
