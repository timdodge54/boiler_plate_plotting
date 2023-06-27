# Boiler Plate Plotting Package

This repo containts boiler plate code for plotting contininuly updating information in matplotlib. This can be used for infomation dashboards, simulation data, ... etc. The ros msg is as layout is as follows.

```
float64[] x
float64[] y
```

If the data wants to be expanded into higher dimensions more datafields can be added to the ros_msg located at `boiler_plate_msg/msg/Data.msg`.
An example of modified data fields adding dimensions would be

```
float64[] x_1
float64[] x_2
float64[] y
```

The msg file currently contains 64 bit floating numbers. If a user for example the user wanted 32 bit integers the msg file could be as follows

```
int32[] x
int32[] y
```

This Data.msg is published over the `data_msg` topic.

The code for plotting that plots the original msg file is as follows.

```python3
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
            self.get_logger().info(f"Heard msg: {self.x[-1]}")

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

```

For the modified first modified ros msg the code would be as follows.

```python3
    def __init__(self):
        """Initialize."""
        super().__init__("example_node")
        # Initialize figure and axes and save to class
        self.fig, self.ax = plt.subplots()
        # create Thread lock to prevent multiaccess threading errors
        self._lock = threading.Lock()
        # create initial values to plot
        self.x_1: list[float] = []
        self.x_2: list[float] = []
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
            self.x_1 = list(msg.x)
            self.x_2 = list(msg.x)
            self.y = list(msg.y)
            self.get_logger().info(f"Heard msg: {self.x[-1]}")

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
            x_1 = np.array(self.x)
            x_1 = np.array(self.x)
            y = np.array(self.y)
            self.ax.plot(x_1, y)
            self.ax.plot(x_2, y)
            return self.ax

```

For the third case the technically the original code is correct but there is just the typing is incorrect this code fixes that.

```python3
    def __init__(self):
        """Initialize."""
        super().__init__("example_node")
        # Initialize figure and axes and save to class
        self.fig, self.ax = plt.subplots()
        # create Thread lock to prevent multiaccess threading errors
        self._lock = threading.Lock()
        # create initial values to plot
        self.x: list[int] = []
        self.y: list[int] = []
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
                int32 x
                int32 y
        """
        # lock thread
        with self._lock:
            # update values
            self.x = list(msg.x)
            self.y = list(msg.y)
            self.get_logger().info(f"Heard msg: {self.x[-1]}")

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

```

There are python and cpp files example files for publishing to the data located in the boiler_plate_plotting package.

To launch the example python file and plotting run the following commands.

```bash
ros2 launch boiler_plate_plotting plt_python.launch.py
```

To launch the example cpp file and plotting run the following commands.

```bash
ros2 launch boiler_plate_plotting plt_cpp.launch.py
```
