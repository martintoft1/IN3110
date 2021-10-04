import numpy as np
# Import the classes with the functions to be tested
from filters import PythonColor2Gray
from filters import NumpyColor2Gray
from filters import NumbaColor2Gray
from filters import PythonColor2Sepia
from filters import NumpyColor2Sepia
from filters import NumbaColor2Sepia

def test_grayscale_filter_color2gray():
    """
    Checks the grayscale_filter functions in all implementations

    Returns:
        AssertionError: If one of the tests don't go through, returns AssertionError. Else, returns nothing.
    """
    # Generate random 3-dimentional array with pixel values chosen between 0 and 255. Set "height" and "width" to be 200 and 251 respectively, in order for the tests to be done in a reasonable amount of time 
    a = np.random.randint(0, 255, size = (200, 251, 3))

    # Get result from python implementation 
    python_a = PythonColor2Gray().grayscale_filter(a)

    # Get result from numpy implementation 
    numpy_a = NumpyColor2Gray().grayscale_filter(a)

    # Get result from numba implementation 
    numba_a = NumbaColor2Gray().grayscale_filter(a)

    # Compare results by checking a random index in the grayscale images against the expected value (the weighted average)
    # Find random index
    i = np.random.randint(0, 199)
    j = np.random.randint(0, 254)
    k = np.random.randint(0, 2)
    # Get expected value
    weighted_average = int(a[i][j][0] * 0.07 + a[i][j][1] * 0.72 + a[i][j][2] * 0.21) 
    # Compare
    assert python_a[i][j][k] == weighted_average
    assert numpy_a[i][j] == weighted_average #Only has one value instead of 3 describing each pixel, but yields the same image as result
    assert numba_a[i][j][k] == weighted_average


def test_grayscale_image_color2gray():
    
    pass



def test_sepia_filter_color2sepia():
    """
    Checks the sepia_filter functions in all implementations

    Returns:
        AssertionError: If one of the tests don't go through, returns AssertionError. Else, returns nothing.
    """
    # Generate random 3-dimentional array with pixel values chosen between 0 and 255. Set "height" and "width" to be 200 and 251 respectively, in order for the tests to be done in a reasonable amount of time 
    a = np.random.randint(0, 255, size = (200, 251, 3))

    # Get result from python implementation 
    python_a = PythonColor2Sepia().sepia_filter(a)

    # Get result from numpy implementation 
    numpy_a = NumpyColor2Sepia().sepia_filter(a)

    # Get result from numba implementation 
    numba_a = NumbaColor2Sepia().sepia_filter(a)

    # Compare results by checking a random index in the sepia images against the expected value (the weighted average)
    # Find random index
    i = np.random.randint(0, 199)
    j = np.random.randint(0, 254)
    k = np.random.randint(0, 2)
    # Get expected value
    sepia_matrix = [[ 0.131, 0.534, 0.272],
                        [ 0.168, 0.686, 0.349],
                        [ 0.189, 0.769, 0.393]] # Sepia filter matrix in BGR order
    weighted_average = int((a[i][j][0] * sepia_matrix[k][0] + a[i][j][1] * sepia_matrix[k][1] + a[i][j][2] * sepia_matrix[k][2]) * 0.718)
    # Compare
    assert python_a[i][j][k] == weighted_average
    assert numpy_a[i][j][k] == weighted_average
    assert numba_a[i][j][k] == weighted_average


test_grayscale_filter_color2gray()
test_sepia_filter_color2sepia()