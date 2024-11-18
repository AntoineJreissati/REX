# REX/puces_sensors.py
import rclpy
from rclpy.node import Node

class SensorsNode(Node):
    def __init__(self):
        super().__init__('sensors_node')
        self.timer = self.create_timer(0.01, self.timer_callback)  # 100Hz refresh rate

    def timer_callback(self):
        capture()
          

    def init_ser(port,baudrate,timeout):
        pass

    def get_data():
        pass

    def standerdise():
        pass

    def Update_DB():
        pass

    def capture():
        std_data=standerdise(get_data())
        Update_DB()


def main(args=None):
    rclpy.init(args=args)
    node = SensorsNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()