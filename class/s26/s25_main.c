#include <stdio.h>
#include <stdbool.h>


bool concat(
    char* pch1, int size1, 
    char* pch2, int size2, 
    char* pchTarget, int targetsize)
    




int main(int argc, char const *argv[])
{
    const int t = 4;
    const char buff1[10] = "Ali";
    const char buff2[10] = "Mojdeh";

    char buff3[20];

    bool success = contcat(&(buff1[0]), 10, &(buff2[0]), 10, &(buff3[0]), 20);
    if (! success)
        printf("Error\n");

//    char* pchTarget = &(buff3[0]);

    char* pch = &(buff1[0]);
    int idx = 0;
    while(*pch != 0)
    {
        buff3[idx] = *pch;
        // *pchTarget = *pch;
        idx++;
        // pchTarget++;
        pch++;
    }

    buff3[idx] = ' ';
    idx++;

    pch = &(buff2[0]);    
    while (*pch != 0)
    {
        buff3[idx] = *pch;
        idx++;
        pch++;
    }
    printf("%s\n", buff3);
    buff3[idx] = 0;
    printf("%s\n", buff3);

    // printf("%c\n", buff[0]);
    // printf("%s\n", buff);
    return 0;
}
