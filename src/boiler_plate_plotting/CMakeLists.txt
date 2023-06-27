cmake_minimum_required(VERSION 3.5)
project(boiler_plate_plotting)

include_directories(include)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(common_interfaces REQUIRED)
find_package(boiler_plate_msg REQUIRED)

# include_directories(include)
add_executable(cpp_rand_gen src/test_pub.cpp)
ament_target_dependencies(cpp_rand_gen rclcpp boiler_plate_msg)

target_include_directories(cpp_rand_gen PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
install(TARGETS
  cpp_rand_gen
  DESTINATION lib/${PROJECT_NAME})

install(PROGRAMS
  scripts/test_plot.py
  scripts/test_pub.py
  DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}/
)

ament_export_include_directories(include)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)

  # # the following line skips the linter which checks for copyrights
  # # uncomment the line when a copyright and license is not present in all source files
  # # set(ament_cmake_copyright_FOUND TRUE)
  # # the following line skips cpplint (only works in a git repo)
  # # uncomment the line when this package is not in a git repo
  # # set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()