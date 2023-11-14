from main import *

def test_swap_first_and_last():
    assert swap_first_and_last(["cat","dog","goldfish"]) == ["goldfish","dog","cat"]
    assert swap_first_and_last([1,2,3,4,5,6,7,8,9,10]) == [10,2,3,4,5,6,7,8,9,1]

def test_replace_middle_element():
    assert replace_middle_element([1,2,3,4,5]) == [1,2,15,4,5]
    assert replace_middle_element([1,2,3,4,5,6,7,8]) == [1,2,3,4,36,6,7,8]

def test_even_indexed_elements():
    assert even_indexed_elements([0,2,4,6,8]) == []
    assert even_indexed_elements([23,25,27,40,44,23]) == [40,44]

def test_reverse_subset():
    assert reverse_subset([1,2,3,4,5,6,7,8,9,10]) == [1,2,6,5,4,3,7,8,9,10]
    assert reverse_subset(["Austin","Buda","Georgetown","Cedar Park","Manor","Elgin","Round Rock","Leander"]) == ["Austin","Buda", "Elgin","Manor","Cedar Park","Georgetown","Round Rock","Leander"]

def test_replace_negative_numbers():
    assert replace_negative_numbers([-1,0,1]) == [1,0,1]
    assert replace_negative_numbers([-10,-1,0,1,-22]) == [10,1,0,1,22]

def test_rotate_list_left():
    assert rotate_list_left([1,2,3,4,5],1) == [2,3,4,5,1]
    assert rotate_list_left(["a","b","c","d","e","f"],3) == ["d","e","f","a","b","c"]

def test_rotate_list_right():
    assert rotate_list_left([1,2,3,4,5],1) --> [5,1,2,3,4]
    assert rotate_list_left(["a","b","c","d","e","f"],3) --> ["d","e","f","a","b","c"]