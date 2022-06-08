#include <stdio.h>
#include <stdbool.h>
char concat( const char* buff1,const char* buff2,char* buff3,int size1,int size2,int size3)
{
    int i = 0 ;
    char* pch = (&(buff1[0]));
    for (i=0; i<size1 && *pch !=0;i++)
    {
        buff3[i] = *pch;
        *pch++;
    }
    // printf("%s\n",buff3);
    char* pth = &(buff2[0]); 
    for (i=size1;i<(size1+size2) && *pth!=0 ;i++)
    {
        buff3[i] = *pth;
        *pth++;
        
    }
    printf("%s\n",buff3);
}

int  main(int argc, char const *argv[])
{
    const char a[3] = "oos";
    const char b[5] = "mamad";
    char c[8];
    int d = 3;
    int e = 5;
    int f = 8 ;


    char w;
    w = concat(&(a[0]),&(b[0]),&(c[0]),d,e,f);
    return 0 ;
}