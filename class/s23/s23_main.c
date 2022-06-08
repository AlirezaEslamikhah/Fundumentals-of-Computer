#include<stdio.h>
#include<stdbool.h>

void is_bit_on (int num,int bit ,bool * is_bit_on)
{
    if (num >> (bit-1)) & 1 == 1
    {
        is_bit_on = true;
    } 

}

int get_max(int a , int b )
{    
    if (a > b )
        return a ;
    return b ; 
}

void swap(int a , int b )
{
    a = b 
    b = a 
}

int main()
{
    int a1 = 5;
    int b1 = 4;
    printf(" %d , %d \n" , a1 , b1 );
    swap(a1,b1);
    printf("%d,%d\n" ,a1,b1);


}