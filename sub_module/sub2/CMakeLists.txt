cmake_minimum_required(VERSION 2.8.12)
project(cmake_example_sub)

pybind11_add_module(cmake_example_sub src/main.cpp)

