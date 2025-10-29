import rclpy, math
from rclpy.node import Node
from sensor_msgs.msg import JointState
import time

class MoveDemo(Node):
    def __init__(self):
        super().__init__('move_demo')
        self.pub = self.create_publisher(JointState, 'joint_states', 10)
        self.timer = self.create_timer(0.1, self.timer_cb)
        self.t0 = time.time()

        # 6-DOF Antar arm joint names
        names = ['J_1_Base_Stol',
                 'J_2_Stol_Plecho_1',
                 'J_3_Plecho_1_and_2',
                 'J_4_Plecho_2_and_3',
                 'J_5_Plecho_3_and_4',
                 'J_6_Plecho_4_Kist']
        self.msg = JointState()
        self.msg.name = names
        self.msg.position = [0.0] * 6

    def timer_cb(self):
        t = time.time() - self.t0
        self.msg.position = [
            math.sin(t)          * 0.8,   # J1
            math.sin(2*t)        * 0.6,   # J2
            math.sin(3*t)        * 0.5,   # J3
            math.sin(4*t)        * 0.4,   # J4
            math.sin(5*t)        * 0.3,   # J5
            math.sin(6*t)        * 0.2    # J6
        ]
        self.msg.header.stamp = self.get_clock().now().to_msg()
        self.pub.publish(self.msg)

def main():
    rclpy.init()
    node = MoveDemo()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
