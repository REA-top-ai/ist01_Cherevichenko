cmake_minimum_required(VERSION 3.31.6)
project(bitmap)
set(CMAKE_CXX_STANDARD 23)
add_executable(bitmap main.cpp

        include/errors.h
        include/file_loader.h
        include/images/pixel.h
        include/images/bmp_header.h
        include/images/bitmap.h

        src/file_loader.cpp
        src/images/pixel.cpp
        src/images/bmp_header.cpp
        src/images/bitmap.cpp
)
