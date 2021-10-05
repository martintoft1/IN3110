# Packages needed for tests
import numpy as np
import os
# The classes with the functions to be tested
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
    # Generate random 3D array
    a = generate_random_3D_array()

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


def test_sepia_filter_color2sepia():
    """
    Checks the sepia_filter functions in all implementations

    Returns:
        AssertionError: If one of the tests don't go through, returns AssertionError. Else, returns nothing.
    """
    # Generate random 3D array
    a = generate_random_3D_array()

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


def test_grayscale_image_color2gray():
    """
    Checks the grayscale_image function from NumpyColor2Gray.

    Returns:
        AssertionError: If one of the tests don't go through, returns AssertionError. Else, returns nothing.
    """
    # Check if creating image with a file that doesnt contain an image results in TypeError 
    try:
        NumpyColor2Gray().grayscale_image("tests/test_images/rain.py")
    except Exception as e:
        assert type(e) == TypeError

    # Check if creating image with a file path that doesnt exist results in FileNotFoundError
    try:
        NumpyColor2Gray().grayscale_image("tests/test_images/rain2.jpg")
    except Exception as e:
        assert type(e) == FileNotFoundError

    # Check if image gets created in correct place with correct name when not giving output-filename and -path 
    if os.path.exists("tests/test_images/rain_grayscale.jpg"):
        os.remove("tests/test_images/rain_grayscale.jpg")
    a = NumpyColor2Gray().grayscale_image("tests/test_images/rain.jpg")
    assert os.path.exists("tests/test_images/rain_grayscale.jpg")
    # No need to check if the returned value a is correct, as this can be checked in test_grayscale_filter_color2gray as it utilizes the same method for the conversion.

    # Check if image gets created in correct place with correct name when giving output-filename and -path 
    if os.path.exists("tests/test_images/rain_grayscale2.jpg"):
        os.remove("tests/test_images/rain_grayscale2.jpg")
    a = NumpyColor2Gray().grayscale_image("tests/test_images/rain.jpg", "tests/test_images/rain_grayscale2.jpg")
    assert os.path.exists("tests/test_images/rain_grayscale2.jpg")


def test_sepia_image_color2sepia():
    """
    Checks the sepia_image function from NumpyColor2Sepia.

    Returns:
        AssertionError: If one of the tests don't go through, returns AssertionError. Else, returns nothing.
    """
    # Check if creating image with a file that doesnt contain an image results in TypeError 
    try:
        NumpyColor2Sepia().sepia_image("tests/test_images/rain.py")
    except Exception as e:
        assert type(e) == TypeError

    # Check if creating image with a file path that doesnt exist results in FileNotFoundError
    try:
        NumpyColor2Sepia().sepia_image("tests/test_images/rain2.jpg")
    except Exception as e:
        assert type(e) == FileNotFoundError

    # Check if image gets created in correct place with correct name when not giving output-filename and -path 
    if os.path.exists("tests/test_images/rain_sepia.jpg"):
        os.remove("tests/test_images/rain_sepia.jpg")
    a = NumpyColor2Sepia().sepia_image("tests/test_images/rain.jpg")
    assert os.path.exists("tests/test_images/rain_sepia.jpg")
    # No need to check if the returned value a is correct, as this can be checked in test_sepia_filter_color2sepia as it utilizes the same method for the conversion.

    # Check if image gets created in correct place with correct name when giving output-filename and -path 
    if os.path.exists("tests/test_images/rain_sepia2.jpg"):
        os.remove("tests/test_images/rain_sepia2.jpg")
    a = NumpyColor2Sepia().sepia_image("tests/test_images/rain.jpg", "tests/test_images/rain_sepia2.jpg")
    assert os.path.exists("tests/test_images/rain_sepia2.jpg")


def test_report_grayscale_filter_color2gray():
    """
    Tests the report_grayscale_filter-function in all implementations

    Returns:
        AssertionError: If one of the tests don't go through, returns AssertionError. Else, returns nothing.
    """
    # Test the python report_grayscale_filter

    # Check if creating report with image that doesn't exits result in FileNotFoundError
    try:
        PythonColor2Gray().report_grayscale_filter("tests/test_images/rain2.jpg", "tests/reports")
    except Exception as e:
        assert type(e) == FileNotFoundError

    # Check if report can be saved normally to reports
    PythonColor2Gray().report_grayscale_filter("tests/test_images/rain.jpg", "tests/reports")
    assert os.path.exists("tests/reports/python_report_color2gray.txt")

    # Test the numpy report_grayscale_filter

    # Check if report can be saved normally to reports
    NumpyColor2Gray().report_grayscale_filter("tests/test_images/rain.jpg", "tests/reports")
    assert os.path.exists("tests/reports/numpy_report_color2gray.txt")

    # Check if the runtime can be compared with the runtime from the report for the python-implementation 
    NumpyColor2Gray().report_grayscale_filter("tests/test_images/rain.jpg", "tests/reports", "tests/reports/python_report_color2gray.txt")
    assert os.path.exists("tests/reports/numpy_report_color2gray.txt")


    # Test the numba report_grayscale_filter

    # Check if report can be saved normally to reports
    NumbaColor2Gray().report_grayscale_filter("tests/test_images/rain.jpg", "tests/reports")
    assert os.path.exists("tests/reports/numba_report_color2gray.txt")

    # Check if the runtime can be compared with the runtime from the report for the python-implementation and the numpy-implementation
    NumbaColor2Gray().report_grayscale_filter("tests/test_images/rain.jpg", "tests/reports", "tests/reports/python_report_color2gray.txt", "tests/reports/numpy_report_color2gray.txt")
    assert os.path.exists("tests/reports/numba_report_color2gray.txt")


def test_report_sepia_filter_color2sepia():
    """
    Tests the report_sepia_filter-function in all implementations

    Returns:
        AssertionError: If one of the tests don't go through, returns AssertionError. Else, returns nothing.
    """
    # Test the python report_sepia_filter

    # Check if creating report with image that doesn't exits result in FileNotFoundError
    try:
        PythonColor2Sepia().report_sepia_filter("tests/test_images/rain2.jpg", "tests/reports")
    except Exception as e:
        assert type(e) == FileNotFoundError
    # Check if report can be saved normally to reports
    PythonColor2Sepia().report_sepia_filter("tests/test_images/rain.jpg", "tests/reports")
    assert os.path.exists("tests/reports/python_report_color2sepia.txt")

    # Test the numpy report_sepia_filter

    # Check if report can be saved normally to reports
    NumpyColor2Sepia().report_sepia_filter("tests/test_images/rain.jpg", "tests/reports")
    assert os.path.exists("tests/reports/numpy_report_color2sepia.txt")

    # Check if the runtime can be compared with the runtime from the report for the python-implementation 
    NumpyColor2Sepia().report_sepia_filter("tests/test_images/rain.jpg", "tests/reports", "tests/reports/python_report_color2sepia.txt")
    assert os.path.exists("tests/reports/numpy_report_color2sepia.txt")

    # Test the numba report_sepia_filter

    # Check if report can be saved normally to reports
    NumbaColor2Sepia().report_sepia_filter("tests/test_images/rain.jpg", "tests/reports")
    assert os.path.exists("tests/reports/numba_report_color2sepia.txt")

    # Check if the runtime can be compared with the runtime from the report for the python-implementation and the numpy-implementation
    NumbaColor2Sepia().report_sepia_filter("tests/test_images/rain.jpg", "tests/reports", "tests/reports/python_report_color2sepia.txt", "tests/reports/numpy_report_color2sepia.txt")
    assert os.path.exists("tests/reports/numba_report_color2sepia.txt")


def generate_random_3D_array():
    """
    Generate random 3-dimentional array with pixel values chosen between 0 and 255 to be used in the tests. Set "height" and "width" to be 200 and 251 respectively, in order for the tests to be done in a reasonable amount of time 

    Returns:
        numpy integer 3D array: random 3D array
    """
    return np.random.randint(0, 255, size = (200, 251, 3))



if __name__ == "__main__":
    print("Running grayscale_filter tests")
    test_grayscale_filter_color2gray()
    print("grayscale_filter tests finished without errors\n")

    print("Running sepia_filter tests")
    test_sepia_filter_color2sepia()
    print("sepia_filter tests finished without errors\n")

    print("Running grayscale_image tests")
    test_grayscale_image_color2gray()
    print("grayscale_image tests finished without errors\n")

    print("Running sepia_image tests")
    test_sepia_image_color2sepia()
    print("sepia_image tests finished without errors\n")

    print("Running report_grayscale_filter tests")
    test_report_grayscale_filter_color2gray()
    print("report_grayscale_filter tests finished without errors\n")

    print("Running report_sepia_filter tests")
    test_report_sepia_filter_color2sepia()
    print("report_sepia_filter tests finished without errors")
