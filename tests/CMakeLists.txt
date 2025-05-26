find_package(GTest CONFIG REQUIRED)

enable_testing()

set(TEST_SRCS
    test.cpp
)

add_executable(ROOT_UNIT_TEST
    ${TEST_SRCS}
)

target_link_libraries(ROOT_UNIT_TEST PRIVATE
    GTest::gtest_main
    ${PROJECT_NAME}_static
)

include(GoogleTest)
gtest_discover_tests(ROOT_UNIT_TEST)

