#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"


int strlen(const char* pch, int size)
{

}

TEST_CASE( "String Length", "[string]" ) {
    REQUIRE(strlen("ali", 4) == 3)

    char buf[10] = "hossein";
    REQUIRE(strlen(buf, 10) == 7)
}