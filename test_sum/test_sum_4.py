def my_add_function(x,y):
    return x + y

def test_summer():
    res = my_add_function(5, 3)
    assert res != None
    assert res == 8
