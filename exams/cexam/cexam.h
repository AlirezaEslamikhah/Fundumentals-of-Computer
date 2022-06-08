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

int q1_sum(int a , int b)
{
    return a+b;
}

bool q2_sum(int a , int b ,int*c)
{
    *c = a+b;
    if(*c % 2 ==1)
        return true;
    if (*c % 2 ==0)
        return false;
}

int q3_solve_equation(int a , int b , int c, double*x,double*x2)
{
    int* z = (int*)x;
    int* p = (int*)x2; 
    int delta = (b*b) - 4*(a*c);
    *z = (-b + sqrt(delta)) / 2 ;
    *p = (-b - sqrt(delta)) / 2;
    if (*z == *p)
    {
        return(1,*z,*p);
    }
    if (*z !=0)
    {
        return (2,*z,*p);
    }
    if (*z && *p == 0 )
    {
        return(0,*z,*p);
    }
    
}

void q4_add_equations(int a,int b,int c, int d,int e ,int f,int* x1,int* x2, int* x3)
{
    *x1 = a+d;
    *x2 = b+e;
    *x3 = c+f;
}

int q9_array_copy(int* a , int n , int* b)
{
    for (int i = 0; i < n; i++)
    {
        b[i]=a[i];
    }
    return *b;
}

int q8_fill_array(int* a , int n , int m )
{
    for (int i = 0; i < n; i++)
    {
        a[i]=m;
    }
    return *a;
}

int q5_digit_count(int n )
{
    if (n < 0)
    {
        n = n *(-1);
    }
    if (n<10)
    {
        return(1);
    }
    if (n <100 && n>10)
    {
        return (2);
    }
    if (n>100 && n<1000)
    {
        return (3);
    }
    if (n>1000)
    {
        return(6);
    }
    
}

int q10_max_odd_numbers(int*x,int n)
{
    int bigger = x[0];
    for (int i = 0; i < n; i++)
    {
        if (x[i] > bigger)
        {
            bigger=x[i];
        }
    }
    return bigger;
}

int q11_max_odd_positions(int* x , int n)
{
    int m = 0;
    int bigger = x[1];
    for (int i = 1; i < n; i = i+2)
    {
        if (x[i] > bigger)
        {
            bigger = x[i];
        }
        
    }
    return bigger;
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

// int** q14_matrix_add(int**a,int**b,int n,int m )
// {
//     int**z = (int**)malloc((m*n)*sizeof(int**));
//     for (int i = 0; i < n; i++)
//     {
//         **z=**a;
//         z++;
//         a++;
//     }
//     for (int j = 0; j < m; j++)
//     {
        
//     }
    
// }

