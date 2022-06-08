#include<stdbool.h>
#include<math.h>
#include<stdlib.h>


typedef int (*_int_2int_)(int, int);

int get_max(int a, int b)
{
    return a>b?a:b;
}

int get_min(int a, int b)
{
    return a<b?a:b;
}

int get_sum(int a, int b)
{
    return a+b;
}



int q3_solve_equation(int a , int b , int c, double*x,double*x2)
{
    int delta = (b*b) - (4*(a*c));
    *x = (-b + sqrt(delta)) / 2 ;
    *x2 = (-b - sqrt(delta)) / 2;
    if (*x == *x2)
    {
        return(1,*x,*x2);
    }
    if (*x !=0)
    {
        return (2,*x,*x2);
    }
    if (*x && *x2 == 0 )
    {
        return(0,(int)*x,(int)*x2);
    }
    
}



bool q13_matrix_compare(int**x1,int**x2,int n,int m)
{
    for (int i = 0; i <= n; i++)
        for (int j = 0; j <= m; j++)
        {
            if (x1[i][j]==x2[i][j])
            {
                return true;
            }
            else
            {
                return false;
            }
            
        }
}

int** q14_matrix_add(int**a,int**b,int n,int m )
{
    int**z = (int**)malloc((m*n)*sizeof(int**));
    for (int i = 0; i < n; i++)
    {
        **z=*(*a+i);
        z++;
        a++;
    }
    for (int j = 0; j < m; j++)
    {
        **z = *(*b+j);
        z++;
        b++;
    }
    return (z);
}

typedef struct complex_number
{
    double i;
    double r;
}pcn1;

pcn1* q16_add_complex_number(pcn1* x1,pcn1* x2)
{
    (*x1).i=(*x2).i+ (*x1).i;
    (*x1).r=(*x2).r+ (*x1).r;
    return  x1;
}

pcn1* q15_create_complex_number(int x1,int x2)
{
    (pcn1*).i = x1;
    (pcn1*).r = x2;
}

// int q18_aggregate(int*x,int n , (int*)(*func)(int,int))
// {
//     int z = x[1];
//     for (int i = 0; i < n; i++)
//     {
//         *z=(func)(n,m);
//         x[i] = *z;
//     }
//     return *z;
// }

