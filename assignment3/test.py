from array import Array 
import sys

def test_Array():
    """
    Runs a bunch of tests on the Array class from array.py. 
    
    All the tests are supposed to run without raising any exceptions, and the method should run all the way through in a reasonable time. 

    If a assert-test fails, the command-line will tell which line the assert failed at
    """
    # Testing initialization 
    try:
        # Try to make array with correct shape and same types - should succeed and finish try-block
        array = Array((4,), 1, 2, 3, 4)
        print("1: Passed")
    except:
        print("1: Failed")
        sys.exit()
    
    try:
        # Try to make array with mix of types - should fail and enter except-block
        array = Array((4,), True, 2.5689, 3, 4)
        print("2: Failed")
        sys.exit()
    except:
        print("2: Passed")

    try:
        # Try to make array with wrong shape and same types - should fail and enter except-block
        array = Array((5,), 1, 2, 3, 4)
        print("3: Failed")
        sys.exit()
    except:
        print("3: Passed")
        
    
    # 
    """
    assert isinstance(array.__getitem__(3), float) 
    print(array.__getitem__(1).__class__)
    assert isinstance(array.__getitem__(1), float) 
    assert array.__getitem__(0) == 1
    assert isinstance(array.__getitem__(3), int) 
    """

def test_Array_initialization():
    pass



test_Array()