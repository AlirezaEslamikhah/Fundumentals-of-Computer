#include<stdbool.h>
#include<math.h>
#include<stdlib.h>


typedef bool (*__cmp_fn__)(int,int);

bool is_bigger(int a, int b)
{
    return a>b;
}

bool is_smaller(int a, int b)
{
    return a<b;
}

int q1_get_max(int a ,int b ,int c)
{
    int bigger=a;
    if (b>bigger)
    {
        bigger = b;
    }
    if (c > bigger)
    {
        bigger =c;
    }
    return bigger;
}

bool q2_is_right_angled(int a,int b,int c)
{
    int w =q1_get_max(a,b,c);
    if (pow(a,2)==pow(b,2)+pow(c,2)||pow(b,2)==pow(a,2)+pow(c,2)||pow(c,2)==pow(b,2)+pow(a,2))
    {
        return true;
    }
    else
    {
        return false;
    }
    
    
}

int q3_array_fsum(int* a ,int* b , int*c , int n )
{
    int sum =0 ;
    for (int i = 0; i < n; i++)
    {
        sum = sum + ((a[i]*b[i])+ c[i]);
    }
    return sum;
}



int str_len(char* buff)
{
    int sum = 0 ;
    while (*buff!=0)
    {
        sum = sum + 1;
        buff++;
    }
    return sum;
}
void q4_string_shuffle(char* str)
{
    char tmp;
    for (int i = 0; i < str_len(str); i= i+2)
    {
        tmp = str[i];
        str[i]=str[i+1];
        str[i+1]=tmp;
    }
    
}

void q6_sort(int* a , int* b , int *c , int* d)
{
    int tmp;
    int cmd;
    int fc;
    int pc;
    int pk;
    int ck;
    int rk;

    // if (*b>*a>*c>*d)
    // {
    //     tmp = *a;
    //     *a = *b ;
    //     *b = tmp;
    // }
    // if (*c>*b>*a>*d)
    // {
    //     cmd = *a;
    //     *a=*c;
    //     *c = cmd;
    // }
    // if (*d>*c>*b>*a)
    // {
    //     fc= *a;
    //     *a = *d;
    //     *d = fc;
    //     pc = *b;
    //     *b = *c;
    //     *c = pc;
    // }
    if (*a>*c>*b>*d)
    {
        pk = *c;
        *c = *b ;
        *b = pk;
    }
    if (*b>*d>*c>*a)
    {
        ck = *d;
        *d = *a;
        *a = ck;
        fc = *a;
        rk = *b;
        *b = fc;
        *a= rk;


    }
}

// int q5_last_index_of(char* s ,char* z)
// {

// }