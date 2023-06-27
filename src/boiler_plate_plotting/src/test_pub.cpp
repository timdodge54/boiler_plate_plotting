#include "boiler_plate_plotting/test_pub.hpp"
int main(int argc, char** argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<TestPub>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}