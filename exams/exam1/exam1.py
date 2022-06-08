def q1_add(x,y):
    return x + y

def q2_print_add(x,y):
    print(x+y)

def q3_print_square(a,x):
    b = str(a)
    print(x * (b))
    for i in range (x-2):
        print((b) , " " * (x-4) , (b))
    print(x * (b))




def q4_sum_odd_squares(x,y):
    sum = 0 
    for i in range (x,y):
        if i % 2 !=0:
            sum = sum + (i**2)
    return sum

def q5_sum_value_squares(x):
    sum = 0 
    for i in x :
        sum = sum + (i**2)
    return sum

def q6_sum_num_indices(x,y):
    sum = 0 
    for i in y :
        sum = sum + x[i]
    return sum 

# def q7_get_new_fib_array(x,y,z):
#     a = [x,y]
#     for i in range (1,z):
#         b = a[i-1] * (a[i] - a[i-1])
#         #c = str(a[i])"*"str(a[i])"-"str(a[i-1])
#         a.append(b)
# #q7_get_new_fib_array(2,3,4)