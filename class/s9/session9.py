import matplotlib.pyplot as plt
import math

def get_x(minx , maxx , step):
    x_range = []
    current_x = minx

    while current_x <= maxx:
        x_range.append(current_x)
        current_x = current_x + step
    return x_range

def get_x2(range_x):
    y_range = []
    for x in range_x:
         y_range.append(x**2)        
    return y_range

def get_cosx(range_x):
    y_range = []
    for x in range_x:
        y_range.append(math.cos(x))
    return y_range

def factorial(n):
    mul = 1 
    for i in range (1 , n + 1):
        mul = mul * i 
    return mul
    
def taylorcosx(x,n):
    sum = 0
    sign = 1
    for i in range(n):
        w = 2 * i 
        sum = sum + sign * (x**w) / factorial(w)
        
        sign = sign * -1

    return sum   

def get_taylorcosx(range_x,n):
    y_range = []
    for x in range_x:
        y_range.append(taylorcosx(x , n))
    return y_range

if __name__ == '__main__':
    x = get_x (-3.14 , 3.14 , 0.1)
    y_cos = get_cosx(x)
    plt.plot (x , y_cos)
    plt.show()
    for i in range(1, 5):
        y_tcos = get_taylorcosx(x, i)
        plt.plot(x, y_tcos)
    plt.show()


