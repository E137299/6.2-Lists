from main import *

def test_swap_first_and_last():
    assert swap_first_and_last(["cat","dog","goldfish"]) == ["goldfish","dog","cat"]
    assert swap_first_and_last([1,2,3,4,5,6,7,8,9,10]) == [10,2,3,4,5,6,7,8,9,1]

def test_replace_middle_element():
    assert replace_middle_element([1,2,3,4,5]) == [1,2,15,4,5]
    assert replace_middle_element([1,2,3,4,5,6,7,8]) == [1,2,3,4,36,6,7,8]

def test_even_indexed_elements():
    assert even_indexed_element([0,2,4,6,8]) == []
    assert even_indexed_element([23,25,27,40,44,23]) == [40,44]