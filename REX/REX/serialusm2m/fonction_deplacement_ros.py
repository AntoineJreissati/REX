import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class DeplacementNode(Node):
    def __init__(self):
        super().__init__('deplacement_node')
        self.publisher_ = self.create_publisher(String, 'position', 10)
        # Empty initialization

    def publish_position(self):
        msg = String()
        # msg.data = '...'  # Add data if needed
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DeplacementNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()