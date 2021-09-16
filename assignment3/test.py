from array import Array 

def test_Array():
    """
    Runs a bunch of tests on the Array class from array.py. 
    
    All the tests are supposed to run without raising any exceptions, and the method should run all the way through in a reasonable time. 

    If a assert-test fails, the command-line will tell which line the assert failed at
    """
    #Try initializing different arrays to see if they are initialized correctly
    array = Array((4,), 1, 2, 3, 4)
    assert array.__getitem__(0) == 1

    array = Array((5,), 1, 2, 3, 4.00)
    assert isinstance(array.__getitem__(3), float) 
    print(array.__getitem__(1).__class__)
    assert isinstance(array.__getitem__(1), float) 

    

def test_Array_initialization():
    pass



test_Array()