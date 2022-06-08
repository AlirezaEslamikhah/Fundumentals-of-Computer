def q7_get_new_fib_array(x,y,z):
    a = [x,y]
    for i in range (2,z):
        b = a[i-2] * a[i-1] - 2 
        b0 = str a[i-2],*,str a[i-1],"-2" 
        a.append(b0)
    return a 


print(q7_get_new_fib_array(2,3,4))