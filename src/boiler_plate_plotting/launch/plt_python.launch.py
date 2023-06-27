from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    test_plotter = Node(
        package="boiler_plate_plotting",
        executable="test_plot.py",
        name="test_plotter",
        output="screen",
        emulate_tty=True,
    )
    test_pub = Node(
        package="boiler_plate_plotting",
        executable="test_pub.py",
        name="test_pub",
        output="screen",
        emulate_tty=True,
    )

    ld = LaunchDescription()
    ld.add_action(test_pub)
    ld.add_action(test_plotter)
    return ld
