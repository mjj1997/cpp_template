cmake_minimum_required(VERSION 3.20)

project(demo VERSION 1.1 LANGUAGES CXX)

option(BUILD_${PROJECT_NAME}_SHARED_LIBS "build shared library" ON)
option(BUILD_${PROJECT_NAME}_STATIC_LIBS "build static library" ON)

option(BUILD_EXAMPLES "build examples" OFF)
option(BUILD_TESTS "build unit tests" OFF)

if(MSVC)
    set(LIBS ${LIBS} winmm iphlpapi ws2_32 dbghelp Kernel32)

    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /MP /D_WIN32_WINNT=0x0601")
else()
    set(LIBS ${LIBS} dl pthread)

    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")
endif()

message(STATUS "CMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}")
message(STATUS "CMAKE_SYSTEM_NAME=${CMAKE_SYSTEM_NAME}")

add_subdirectory(src)

if(BUILD_EXAMPLES)
    add_subdirectory(examples)
endif()

if(BUILD_TESTS)
    add_subdirectory(tests)
endif()

install(FILES "${PROJECT_SOURCE_DIR}/include/demo/demo.h"
        DESTINATION include/demo)

include(InstallRequiredSystemLibraries)
# set(CPACK_RESOURCE_FILE_LICENSE "${PROJECT_SOURCE_DIR}/License.txt")
set(CPACK_PACKAGE_VERSION_MAJOR "${PROJECT_VERSION_MAJOR}")
set(CPACK_PACKAGE_VERSION_MINOR "${PROJECT_VERSION_MINOR}")
set(CPACK_GENERATOR "TGZ")
set(CPACK_SOURCE_GENERATOR "TGZ")
include(CPack)

