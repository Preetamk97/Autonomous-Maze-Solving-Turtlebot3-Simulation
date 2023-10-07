cmake_minimum_required(VERSION 3.8)
project(autonomous_tb3)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# Adding the below 2 dependencies to configure the packaqe to work with Python codes.
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)
# Adding the below dependency so that we can use nav_msgs message types in our package code.
find_package(nav_msgs REQUIRED)


# Bringing "scripts" folder under the radar of CMakeLists.txt file
ament_python_install_package(script)

# Adding python scripts of this package to the CMakeLists.txt records.
install(PROGRAMS
  script/occupancy_grid_pub.py
  script/entity_spawner.py
  script/maze_solver.py
  DESTINATION lib/${PROJECT_NAME}
)

install (DIRECTORY config DESTINATION share/${PROJECT_NAME}/)
install (DIRECTORY launch DESTINATION share/${PROJECT_NAME}/)
install (DIRECTORY worlds DESTINATION share/${PROJECT_NAME}/)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
