import mathfunctions2

def test_get_max():
    nums = [1,5,10,0,15,12]
    assert mathfunctions2.get_max(nums) == 15


    nums = [-100,50,10,0,15,12]
    assert mathfunctions2.get_max(nums) == 50



def test_get_sum():
    nums = [1,5,10,0,15,12]
    assert mathfunctions2.get_sum(nums) == 43


    nums = [-100,50,10,0,15,12]
    assert mathfunctions2.get_sum(nums) == -13

def test_get_sum_odd():
    nums = [1,5,10,0,15,12]
    assert mathfunctions2.get_sum_odd(nums) == 21


    nums = [-100,50,10,0,15,12]
    assert mathfunctions2.get_sum_odd(nums) == 15

