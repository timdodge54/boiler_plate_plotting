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
    rand_gen = Node(
        package="boiler_plate_plotting",
        executable="cpp_rand_gen",
        name="rand_gen",
        output="screen",
        emulate_tty=True,
    )

    ld = LaunchDescription()
    ld.add_action(rand_gen)
    ld.add_action(test_plotter)
    return ld
