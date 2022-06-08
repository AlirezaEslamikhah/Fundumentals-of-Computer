#include<stdio.h>

// int sterlen (char*x , int size )
// {
//     x[size];
//     int sum = 0 ;
//     int i = 0;
//     // char* pch = (&(x[0]));
//     for (i=0;i < size;i++)
//     {
//         sum = sum + 1;
        
//     }
//     printf("%d",sum);
// }

char* reverse (char*x , int size )
{
    // x[size];
    char buff[size + 1];
    // char *pch = (&(x[0]));
    for (int i = 0 ; i< (size) ;i++)
    {
        buff[size - i - 1] = x[i];
        // x[i] = buff[size -i-1];
    }
    return(buff);
}



int main()
{
    // int w = sterlen("alireza",7);
    char* q = reverse("test",4);
    printf("%s",&q);
    return 0;
}