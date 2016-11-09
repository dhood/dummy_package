cmake_minimum_required(VERSION 3.5)

project(dummy_package)

find_package(ament_cmake_nose REQUIRED)

ament_add_nose_test(test_timeout
    test/test_timeout.py
    TIMEOUT 5)

find_package(ament_cmake REQUIRED)
message(
  "\n====================\n"
  "CMake install prefix: ${CMAKE_INSTALL_PREFIX}"
  "\n====================\n"
  )
ament_index_register_resource("test_resource"
    CONTENT_FILE resource.txt
)
ament_package()
