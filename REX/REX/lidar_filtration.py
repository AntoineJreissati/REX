import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class LidarFiltrationNode(Node):
    def __init__(self):
        super().__init__('lidar_filtration_node')
        self.publisher_ = self.create_publisher(String, 'evitement', 10)
        # Set the refresh rate to 100 Hz
        timer_period = 0.01  # seconds
        self.timer = self.create_timer(timer_period, self.publish_evitement)

    def publish_evitement(self):
        msg = String()
        # msg.data = '...'  # Add data if needed
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing evitement message at 100 Hz')

    def filtrage():
        pass
    
    def boxing():
        pass

    def obstacle():
        pass

def main(args=None):
    rclpy.init(args=args)
    node = LidarFiltrationNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()