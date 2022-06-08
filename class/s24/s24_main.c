#include<stdio.h>

int test2()

{
    unsigned int x = 0xffaaff99;
    int nums[10];
    for (int i=0; i<10; i++)
    {
        nums[i] = i;
    }
    int w = nums[3];
    int* pos4th = ((int*) &nums) + 3;
    int s = *pos4th;
    return 0;
}

int test1()
{
    unsigned int x = 0xffaaff11;
    return test2();
}

int s24()
{
    int test[10];
    for (int i=0; i<10; i++)
        test[i] = i;

    int *x = &(test[0]);
    int i = 0; 
    while (i <= 10)
    {
        test[i] =  i ;
        printf("%d", test[i]);
        // x++;
        i++;
    }
}

int main()
{
    unsigned int x = 0xffaaffbb;
    int w = test1();
    printf("done\n");
    int s =  s24();
}
