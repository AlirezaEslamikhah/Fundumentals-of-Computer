def get_max(nums):
    max = nums[0]
    for n in  nums:
        if n > max:
            max = n 
    return max 
   

def get_sum(nums): 
    sum = 0 
    for n in nums:
        sum = sum + n 
    return sum
   


def get_sum_odd(nums):
    sum = 0
    for n in nums:
        if n % 2 == 1:
            sum = sum + n 
    return sum
                     

