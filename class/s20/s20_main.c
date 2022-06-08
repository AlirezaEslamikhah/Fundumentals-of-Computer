#include<stdio.h>
#include<math.h>

int sum(int a, int b)
{
    return a + b;
}

void print_my_number(int x)
{
    printf("Your number is : %d\n", x);
}

void main()
{
    //file = open("test.txt", "a");

    int c;
    c = sum(5, 10);

    for(int i=0; i<10; i++)
        printf("%d", i);

    double n = 25;
    int nm = (int) sqrt(25);
    for(int i=1;i<10;i++)
    {
        for (int j=1; j<20; j++)
        {
            if (i % j == 0)
            {
                printf("%d, %d\n", i, j);
            }
            // else
            //     printf("ali");
            // printf("ali");
                
            
        }
    }

    //print_my_number(c);
    // printf("the number is %d %d", c, 5);
}