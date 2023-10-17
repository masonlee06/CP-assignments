from fib import flatten_list_r
def test_flatten():
    input_list = [1, [2, 3, 4], 5, [6, 7], 8]
    assert flatten_list_r(input_list) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_flatten_02():
    input_list = [1, [2, 3], 4]
    assert flatten_list_r(input_list) == [1, 2, 3, 4, 5]