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
        pass
    except:
        print("Initialization 1: Failed")
        sys.exit()
    
    try:
        # Try to make array with int and float - should fail and enter except-block
        array = Array((4,), 1, 2.5689, 3, 4)
        print("Initialization 2: Failed")
        sys.exit()
    except:
        pass

    try:
        # Try to make array with int and bool - should fail and enter except-block
        array = Array((4,), 1, True, 3, 4)
        print("Initialization 3: Failed")
        sys.exit()
    except:
        pass

    try:
        # Try to make array with wrong shape and same types - should fail and enter except-block
        array = Array((5,), 1, 2, 3, 4)
        print("Initialization 4: Failed")
        sys.exit()
    except:
        pass
        
    
    # Testing get-function 
    array = Array((4,), 1, 2, 3, 4) # Test-array
    try:
        # Try to get first value - should succeed and finish try-block
        assert array[0] == 1
        pass
    except:
        print("Get 1: Failed")

    try:
        # Try to get fifth value - should fail and enter except-block
        a = array[5]
        print("Get 2: Failed")
    except:
        pass

    
    # Testing str-function
    try:
        # Try to compare str-value of array with expected value - should succeed and finish try-block
        assert str(array) == "[1, 2, 3, 4]"
        pass
    except:
        print("Str 1: Failed")

    
    # Testing print-function
    print(array) #Should be [1, 2, 3, 4]

    
    # Testing len-function
    try:
        # Try to compare len-value of array with expected value - should succeed and finish try-block
        assert len(array) == 4
        pass
    except:
        print("Len 1: Failed")
    

    # Testing add-function
    try:
        # Try to add arrays of same type and shape - should succeed and finish try-block
        array2 = Array((4,), 1, 1, 1, 1)
        array += array2
        pass
    except:
        print("Add 1: Failed")

    try:
        # Try to add arrays of different types - should fail and enter except-block
        array2 = Array((4,), 1.00, 2.00, 3.00, 4.00)
        array += array2
        print("Add 2: Failed")
    except:
        pass

    try:
        # Compare result of adding arrays with expected result - should succeed and finish try-block
        array = Array((2,), 1, 2)
        array2 = Array((2,), 3, 4)
        array += array2
        assert str(array) == "[4, 6]"
        pass
    except:
        print("Add 3: Failed")
    
    try:
        # Compare result of adding array and number with expected result - should succeed and finish try-block
        array = Array((2,), 1, 2)
        number = 3
        array += number
        assert str(array) == "[4, 5]"
        pass
    except:
        print("Add 4: Failed")

    
    # Testing radd-function
    try:
        # Try adding number and array - should succeed and finish try-block
        array = Array((2,), 1, 2)
        number = 3
        array = number + array
        assert str(array) == "[4, 5]"
        pass
    except:
        print("Radd 1: Failed")

    
    # Testing sub-function
    array = Array((4,), 1, 2, 3, 4)
    try:
        # Try to subtract arrays of same type and shape - should succeed and finish try-block
        array2 = Array((4,), 1, 1, 1, 1)
        array -= array2
        pass
    except:
        print("Sub 1: Failed")

    try:
        # Try to subtract arrays of different types - should fail and enter except-block
        array2 = Array((4,), 1.00, 2.00, 3.00, 4.00)
        array -= array2
        print("Sub 2: Failed")
    except:
        pass

    try:
        # Compare result of subtracting arrays with expected result - should succeed and finish try-block
        array = Array((2,), 1, 2)
        array2 = Array((2,), 3, 4)
        array = array2 - array
        assert str(array) == "[2, 2]"
        pass
    except:
        print("Sub 3: Failed")
    
    try:
        # Compare result of subtracting array and number with expected result - should succeed and finish try-block
        array = Array((2,), 1, 2)
        number = 3
        array -= number
        assert str(array) == "[-2, -1]"
        pass
    except:
        print("Sub 4: Failed")
    

    # Testing rsub-function
    try:
        # Try subtracting number and array - should succeed and finish try-block
        array = Array((2,), 1, 2)
        number = 3
        array = number - array
        assert str(array) == "[-2, -1]"
        pass
    except:
        print("Rsub 1: Failed")

    
    # Testing mul-function
    array = Array((4,), 1, 2, 3, 4)
    try:
        # Try to multiplicate arrays of same type and shape - should succeed and finish try-block
        array2 = Array((4,), 1, 1, 1, 1)
        array *= array2
        pass
    except:
        print("Mul 1: Failed")

    try:
        # Try to multiplicate arrays of different types - should fail and enter except-block
        array2 = Array((4,), 1.00, 2.00, 3.00, 4.00)
        array *= array2
        print("Mul 2: Failed")
    except:
        pass

    try:
        # Compare result of multiplicating arrays with expected result - should succeed and finish try-block
        array = Array((2,), 1, 2)
        array2 = Array((2,), 3, 4)
        array = array2 * array
        assert str(array) == "[3, 8]"
        pass
    except:
        print("Mul 3: Failed")
    
    try:
        # Compare result of multiplicating array and number with expected result - should succeed and finish try-block
        array = Array((2,), 1, 2)
        number = 3
        array *= number
        assert str(array) == "[3, 6]"
        pass
    except:
        print("Mul 4: Failed")


    # Testing rmul-function
    try:
        # Try subtracting number and array - should succeed and finish try-block
        array = Array((2,), 1, 2)
        number = 3
        array = number * array
        assert str(array) == "[3, 6]"
        pass
    except:
        print("Rmul 1: Failed")


    # Testing eq-function
    array = Array((4,), 1, 2, 3, 4)
    try:
        # Try to check if arrays of same type and shape with same elements are equal - should succeed and finish try-block
        array2 = Array((4,), 1, 2, 3, 4)
        assert array == array2
        pass
    except:
        print("Eq 1: Failed")

    try:
        # Try to check if arrays of different types are equal - should fail and enter except-block
        array2 = Array((4,), 1.00, 2.00, 3.00, 4.00)
        assert array == array2
        print("Eq 2: Failed")
    except:
        pass
    
    try:
        # Try to check if an array and a number is equal - should fail and enter except-block
        array = Array((1,), 1)
        number = 1
        assert array == number
        print("Eq 3: Failed")
    except:
        pass

    
    # Testing is_equal-function
    array = Array((4,), 1, 2, 3, 4)
    try:
        # Check if is_equal works - should succeed and finish try-block
        array2 = Array((4,), 1, 2, 4, 4)
        equal = array.is_equal(array2)
        pass
    except:
        print("Is_equal 1: Failed")

    try:
        # Compare value of is_equal with two arrays with expected value - should succeed and finish try-block
        array2 = Array((4,), 1, 2, 4, 4)
        equal = array.is_equal(array2)
        assert str(equal) == "[True, True, False, True]"
        pass
    except:
        print("Is_equal 2: Failed")

    try:
        # Try to compare arrays of different types with is_equal, and see if it results in TypeError - should succeed and finish try-block
        array2 = Array((4,), 1.00, 2.00, 3.00, 4.00)
        equal = array.is_equal(array2)
        assert equal == NotImplemented
        pass
    except:
        print("Is_equal 3: Failed")
    
    try:
        # Try to check if is_equal works with an array and a number - should succeed and finish try-block
        array = Array((3,), 1, 2, 3)
        number = 1
        equal = array.is_equal(number)
        assert str(equal) == "[True, False, False]"
        pass
    except:
        print("Is_equal 4: Failed")

    
    # Testing min_element-function
    array = Array((4,), 1, 2, 3, 4)
    try:
        # Check if min works - should succeed and finish try-block
        array.min_element()
        pass
    except:
        print("Min_element 1: Failed")

    array = Array((4,), -1, 0, 1, 4)
    try:
        # Compare value of min with expected value - should succeed and finish try-block
        assert array.min_element() == -1
        pass
    except:
        print("Min_element 2: Failed")


# Run tests
test_Array()