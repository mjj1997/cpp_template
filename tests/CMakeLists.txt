find_package(GTest CONFIG REQUIRED)

enable_testing()

set(TEST_SRCS
    test.cpp
)

add_executable(${PROJECT_NAME}_test
    ${TEST_SRCS}
)

target_link_libraries(${PROJECT_NAME}_test PRIVATE
    GTest::gtest_main
    ${PROJECT_NAME}_static
)

include(GoogleTest)
gtest_discover_tests(${PROJECT_NAME}_test)

