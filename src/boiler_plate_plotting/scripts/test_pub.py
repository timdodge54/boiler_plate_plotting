#! /usr/bin/env python3
import time

import rclpy
import rclpy.callback_groups
from rclpy.publisher import Publisher
import numpy as np
from boiler_plate_msg.msg import Data
from rclpy.node import Node


class TestPub(Node):
    def __init__(self) -> None:
        super().__init__("test_pub")
        self.cbg = rclpy.callback_groups.MutuallyExclusiveCallbackGroup()
        self.pub: Publisher = self.create_publisher(
            Data, "data_msg", 10, callback_group=self.cbg
        )
        self.x: list[float] = []
        self.y: list[float] = []
        time.sleep(5)
        self.timer = self.create_timer(
            1, callback_group=self.cbg, callback=self.gen_rand
        )

    def gen_rand(self):
        new_add_x = np.random.uniform(0, 50)
        new_add_y = np.random.uniform(0, 20)
        self.x.append(new_add_x)
        self.y.append(new_add_y)
        self.get_logger().info("Publishing ...")
        msg = Data()
        msg.x = sorted(self.x)
        msg.y = sorted(self.y)
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = TestPub()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
