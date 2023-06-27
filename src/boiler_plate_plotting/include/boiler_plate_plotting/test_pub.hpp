#ifndef TestPub_hpp
#define TestPub_hpp
#include <vector>
#include <algorithm>
#include <bits/stdc++.h>
#include <random>
#include <chrono>
#include "rclcpp/rclcpp.hpp"
#include "boiler_plate_msg/msg/data.hpp"
class TestPub : public rclcpp::Node
{
public:
  rclcpp::Publisher<boiler_plate_msg::msg::Data>::SharedPtr data_pub;
  std::vector<double> x;
  std::vector<double> y;
  rclcpp::TimerBase::SharedPtr timer;
  std::default_random_engine re;
  TestPub() : Node("Test_Pub")
  {
    RCLCPP_INFO(this->get_logger(), "Test Publisher node has been created.");
    this->data_pub= this->create_publisher<boiler_plate_msg::msg::Data>("data_msg", 10);
    timer = this->create_wall_timer(std::chrono::seconds(5), std::bind(&TestPub::add_val, this));
  }
  void add_val()
  {
      RCLCPP_INFO(this->get_logger(), "Adding Value");
      std::uniform_real_distribution<double> x_gen(0, 500.0);
      std::uniform_real_distribution<double> y_gen(0, 200.0);
      // create random start time
      float x_val = x_gen(re);
      float y_val = y_gen(re);
      this->x.push_back(x_val);
      this->y.push_back(y_val);
      std::sort(x.begin(), x.end());
      std::sort(y.begin(), y.end());
      boiler_plate_msg::msg::Data msg;
      msg.x = this->x;
      msg.y = this->y;
      this->data_pub->publish(msg);
  }
};
#endif  // TestPub_hpp
