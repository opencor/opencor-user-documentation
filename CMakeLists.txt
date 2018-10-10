cmake_minimum_required(VERSION 3.11)

# Project definition

project(UserDocumentation
    LANGUAGES NONE
)

# Some in-house CMake macros

include(${CMAKE_SOURCE_DIR}/cmake/common.cmake)

# Build the user documentation for OpenCOR

build_documentation(user 54 96 146)
