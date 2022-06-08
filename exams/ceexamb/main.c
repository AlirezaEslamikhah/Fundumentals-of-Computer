#include<stdio.h>
int q2_sum(int a , int b ,int*c)
{
    *c = a+b;
    return *c;
}

int main()
{
    int s =0;
    q2_sum(7,5,&s);
    printf("%d",s);
    return 0;
}

