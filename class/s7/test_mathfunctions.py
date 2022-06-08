import mathfunctions

def test_is_odd():
    assert mathfunctions.is_odd(5) == True
    assert mathfunctions.is_odd(8) == False
    assert mathfunctions.is_odd(0) == False 

def test_sum():
    result = mathfunctions.sum(5,2,1,7)    
    assert result == 15