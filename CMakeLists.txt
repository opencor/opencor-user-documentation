cmake_minimum_required(VERSION 3.11)

# Project definition

project(UserDocumentation
    LANGUAGES NONE
)

# Retrieve the theme repository

include(FetchContent)

set(SPHINX_THEME_DIR ${CMAKE_BINARY_DIR}/theme)

FetchContent_Declare(sphinx-theme
    GIT_REPOSITORY
        https://github.com/opencor/sphinx-theme
    GIT_SHALLOW
    SOURCE_DIR
        ${SPHINX_THEME_DIR}
)

FetchContent_MakeAvailable(sphinx-theme)

# Build the user documentation for OpenCOR

include(${SPHINX_THEME_DIR}/cmake/common.cmake)

build_documentation(user 54 96 146)

if(NOT PYTHON_EXECUTABLE)
    set(PYTHON_EXECUTABLE ${Python_EXECUTABLE})
endif()

add_custom_command(TARGET Sphinx POST_BUILD
                   COMMAND ${PYTHON_EXECUTABLE} "${CMAKE_BINARY_DIR}/theme/cmake/appendfile.py"
                                                "${CMAKE_BINARY_DIR}/html/_static/theme.css"
                                                "${CMAKE_SOURCE_DIR}/styles/opencor.css"
                   COMMAND ${PYTHON_EXECUTABLE} "${CMAKE_BINARY_DIR}/theme/cmake/appendfile.py"
                                                "${CMAKE_BINARY_DIR}/html/_static/pygments.css"
                                                "${CMAKE_SOURCE_DIR}/styles/cellmlText.css")
