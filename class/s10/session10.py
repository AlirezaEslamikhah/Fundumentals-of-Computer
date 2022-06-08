def swap (nums , x , y):
    temp = nums[x]
    nums[x] = nums[y]
    nums [y] = temp
  
def reverse (numbers):
        t = len(numbers)
        for i in range(int(t/2)):
            swap(numbers, i, t-i-1) 
        return numbers

def find_max (nums , from_pos , to_pos):
    max_pos = from_pos
    for i in range(from_pos+1 , to_pos+1):
        if nums[i] > nums [max_pos] :
            max_pos = i 
    return max_pos

def sort(numbers):
    l = len(numbers)
    for i in range(l):
        max_pos = find_max(numbers, i, l-1)
        swap(numbers, i, max_pos)
    return numbers

def find_prime_factors(numbers):
    x = []
    for i in range (2, numbers + 1):
        
            if numbers % i !== 0:
                x.append(i)
    for z in x :
        if numbers % x[z] == 0 :
             return x[z]
    







    