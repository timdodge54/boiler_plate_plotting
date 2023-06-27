#! /usr/bin/env python3

import threading

import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np
import rclpy
from rclpy.callback_groups import CallbackGroup
from rclpy.executors import Executor
from boiler_plate_msg.msg import Data
from rclpy.subscription import Subscription
from rclpy.node import Node


class Plotter_Node(Node):
    """Example Node for showing how to use matplotlib within ros 2 node

    Attributes:
        fig: Figure object for matplotlib
        ax: Axes object for matplotlib
        x: x values for matplotlib
        y: y values for matplotlib
        lock: lock for threading
        _sub: Subscriber for node
    """

    def __init__(self):
        """Initialize."""
        super().__init__("example_node")
        # Initialize figure and axes and save to class
        self.fig, self.ax = plt.subplots()
        # create Thread lock to prevent multiaccess threading errors
        self._lock = threading.Lock()
        # create initial values to plot
        self.x: list[float] = []
        self.y: list[float] = []
        # create subscriber
        self.cbg: CallbackGroup = rclpy.callback_groups.MutuallyExclusiveCallbackGroup()
        self._sub: Subscription = self.create_subscription(
            Data, "data_msg", self._callback, 10, callback_group=self.cbg
        )

    def _callback(self, msg: Data):
        """Add msg data to objects data members.

        Args:
            msg: message from subscriber
                Message format
                ----------------
                float64 x
                float64 y
        """
        # lock thread
        with self._lock:
            # update values
            self.x = list(msg.x)
            self.y = list(msg.y)
            self.get_logger().debug(f"Heard msg: {self.x[-1]}")

    def plt_func(self, _):
        """Add data to axis.

        Args:
            _ : Dummy variable that is required for matplotlib animation.

        Returns:
            Axes object for matplotlib
        """
        # lock thread
        with self._lock:
            self.ax.clear()
            x = np.array(self.x)
            y = np.array(self.y)
            self.ax.plot(x, y)
            return self.ax

    def _plt(self):
        """Animate using matplotlib animation."""
        self.ani = anim.FuncAnimation(self.fig, self.plt_func, interval=1000)
        plt.show()


def _main(args=None):
    """Initialize Main."""
    rclpy.init(args=args)
    node = Plotter_Node()
    executor: Executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(node)
    thread = threading.Thread(target=executor.spin, daemon=True)
    thread.start()
    node._plt()


if __name__ == "__main__":
    try:
        _main()
    except KeyboardInterrupt:
        rclpy.shutdown()
