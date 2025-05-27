#include "demo/demo.h"

#include <gtest/gtest.h>

TEST(ProjectBasicTest, Test1)
{
    hello();

    EXPECT_STRNE("hello", "world");
    EXPECT_EQ(7 * 6, 42);
}
