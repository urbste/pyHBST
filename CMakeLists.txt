cmake_minimum_required(VERSION 3.5)

project(pyhbst LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 14 CACHE STRING "C++ version selection")  # or 11, 14, 17, 20
set(CMAKE_CXX_STANDARD_REQUIRED ON)  # optional, ensure standard is supported
set(CMAKE_CXX_EXTENSIONS OFF)  # optional, keep compiler extensions off
set(BUILD_WITH_MARCH_NATIVE OFF CACHE BOOL "Enable architecture-aware optimization (-march=native)")

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O2")
set(CMAKE_CXX_FLAGS "${CMAKE_C_FLAGS} -O2")
if(BUILD_WITH_MARCH_NATIVE)
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -mtune=native -march=native")
    set(CMAKE_CXX_FLAGS "${CMAKE_C_FLAGS} -mtune=native -march=native")
    message(STATUS "Architecture-aware optimization (-march=native): ENABLED")
else()
    message(STATUS "Architecture-aware optimization (-march=native): DISABLED")
endif()

option(PYTHON_BUILD "Turn python build on" ON)

add_subdirectory(extern/pybind11)
set(PY_ALL_HEADER_FILES
    srrg_hbst/types/binary_match.hpp
    srrg_hbst/types/binary_matchable.hpp
    srrg_hbst/types/binary_node.hpp
    srrg_hbst/types/binary_tree.hpp)

pybind11_add_module(pyhbst pyhbst.cc ${PY_ALL_HEADER_FILES})

target_compile_definitions(pyhbst PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
