cmake_minimum_required(VERSION 2.8.12)
set(CMAKE_DISABLE_IN_SOURCE_BUILD ON)
set(CMAKE_DISABLE_SOURCE_CHANGES  ON)

include_directories("./")

file(GLOB_RECURSE sources
"./*.cpp"
)

project(cmake_example)

set(CMAKE_CXX_STANDARD 14)

add_subdirectory(pybind11)
add_subdirectory(sub_module)
pybind11_add_module(cmake_example src/main.cpp)
