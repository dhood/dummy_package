cmake_minimum_required(VERSION 2.8.3)

project(dummy_package)

find_package(ament_cmake_nose REQUIRED)

ament_add_nose_test(test_timeout
    test/test_timeout.py
    TIMEOUT 5)
