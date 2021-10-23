# Packages needed for tests
import numpy as np
import os
import instapy as ip # The instapy-package with all filter-classes containing the different methods

#Makes the random values consistent between runs
np.random.seed(0)

def test_grayscale_filter_color2gray():
    """
    Checks the grayscale_filter functions in all implementations

    Returns:
        AssertionError: If one of the tests don't go through, returns AssertionError. Else, returns nothing.
    """
    # Generate random 3D array
    a = generate_random_3D_array()

    # Get result from python implementation 
    python_a = ip.python_color_2_gray.grayscale_filter(a)

    # Get result from numpy implementation 
    numpy_a = ip.numpy_color_2_gray.grayscale_filter(a)

    # Get result from numba implementation 
    numba_a = ip.numba_color_2_gray.grayscale_filter(a)

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
    python_a = ip.python_color_2_sepia.sepia_filter(a)

    # Get result from numpy implementation 
    numpy_a = ip.numpy_color_2_sepia.sepia_filter(a)

    # Get result from numba implementation 
    numba_a = ip.numba_color_2_sepia.sepia_filter(a)

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
    # Check if creating image with a file path that doesnt exist results in FileNotFoundError
    try:
        ip.numpy_color_2_gray.grayscale_image("test_images/rain2.jpg")
    except Exception as e:
        assert type(e) == FileNotFoundError

    # Check if creating image with a file that doesnt contain an image results in TypeError 
    try:
        ip.numpy_color_2_gray.grayscale_image("test_images/rain.py")
    except Exception as e:
        assert type(e) == TypeError

    # Check if image gets created in correct place with correct name when not giving output-filename and -path 
    if os.path.exists("test_images/rain_grayscale.jpg"):
        os.remove("test_images/rain_grayscale.jpg")
    a = ip.numpy_color_2_gray.grayscale_image("test_images/rain.jpg")
    assert os.path.exists("test_images/rain_grayscale.jpg")
    # No need to check if the returned value a is correct, as this can be checked in test_grayscale_filter_color2gray as it utilizes the same method for the conversion.

    # Check if image gets created in correct place with correct name when giving output-filename and -path 
    if os.path.exists("test_images/rain_grayscale2.jpg"):
        os.remove("test_images/rain_grayscale2.jpg")
    a = ip.numpy_color_2_gray.grayscale_image("test_images/rain.jpg", "test_images/rain_grayscale2.jpg")
    assert os.path.exists("test_images/rain_grayscale2.jpg")


def test_sepia_image_color2sepia():
    """
    Checks the sepia_image function from NumpyColor2Sepia.

    Returns:
        AssertionError: If one of the tests don't go through, returns AssertionError. Else, returns nothing.
    """
    # Check if creating image with a file that doesnt contain an image results in TypeError 
    try:
        ip.numpy_color_2_sepia.sepia_image("test_images/rain.py")
    except Exception as e:
        assert type(e) == TypeError

    # Check if creating image with a file path that doesnt exist results in FileNotFoundError
    try:
        ip.numpy_color_2_sepia.sepia_image("test_images/rain2.jpg")
    except Exception as e:
        assert type(e) == FileNotFoundError

    # Check if image gets created in correct place with correct name when not giving output-filename and -path 
    if os.path.exists("test_images/rain_sepia.jpg"):
        os.remove("test_images/rain_sepia.jpg")
    a = ip.numpy_color_2_sepia.sepia_image("test_images/rain.jpg")
    assert os.path.exists("test_images/rain_sepia.jpg")
    # No need to check if the returned value a is correct, as this can be checked in test_sepia_filter_color2sepia as it utilizes the same method for the conversion.

    # Check if image gets created in correct place with correct name when giving output-filename and -path 
    if os.path.exists("test_images/rain_sepia2.jpg"):
        os.remove("test_images/rain_sepia2.jpg")
    a = ip.numpy_color_2_sepia.sepia_image("test_images/rain.jpg", "test_images/rain_sepia2.jpg")
    assert os.path.exists("test_images/rain_sepia2.jpg")


def test_report_grayscale_filter_color2gray():
    """
    Tests the report_grayscale_filter-function in all implementations

    Returns:
        AssertionError: If one of the tests don't go through, returns AssertionError. Else, returns nothing.
    """
    # Test the python report_grayscale_filter

    # Check if creating report with image that doesn't exits result in FileNotFoundError
    try:
        ip.python_color_2_gray.report_grayscale_filter("test_images/rain2.jpg", "reports")
    except Exception as e:
        assert type(e) == FileNotFoundError

    # Check if report can be saved normally to reports
    ip.python_color_2_gray.report_grayscale_filter("test_images/rain.jpg", "reports")
    assert os.path.exists("reports/python_report_color2gray.txt")

    # Test the numpy report_grayscale_filter

    # Check if report can be saved normally to reports
    ip.numpy_color_2_gray.report_grayscale_filter("test_images/rain.jpg", "reports")
    assert os.path.exists("reports/numpy_report_color2gray.txt")

    # Check if the runtime can be compared with the runtime from the report for the python-implementation 
    ip.numpy_color_2_gray.report_grayscale_filter("test_images/rain.jpg", "reports", "reports/python_report_color2gray.txt")
    assert os.path.exists("reports/numpy_report_color2gray.txt")


    # Test the numba report_grayscale_filter

    # Check if report can be saved normally to reports
    ip.numba_color_2_gray.report_grayscale_filter("test_images/rain.jpg", "reports")
    assert os.path.exists("reports/numba_report_color2gray.txt")

    # Check if the runtime can be compared with the runtime from the report for the python-implementation and the numpy-implementation
    ip.numba_color_2_gray.report_grayscale_filter("test_images/rain.jpg", "reports", "reports/python_report_color2gray.txt", "reports/numpy_report_color2gray.txt")
    assert os.path.exists("reports/numba_report_color2gray.txt")


def test_report_sepia_filter_color2sepia():
    """
    Tests the report_sepia_filter-function in all implementations

    Returns:
        AssertionError: If one of the tests don't go through, returns AssertionError. Else, returns nothing.
    """
    # Test the python report_sepia_filter

    # Check if creating report with image that doesn't exits result in FileNotFoundError
    try:
        ip.python_color_2_sepia.report_sepia_filter("test_images/rain2.jpg", "reports")
    except Exception as e:
        assert type(e) == FileNotFoundError
    # Check if report can be saved normally to reports
    ip.python_color_2_sepia.report_sepia_filter("test_images/rain.jpg", "reports")
    assert os.path.exists("reports/python_report_color2sepia.txt")

    # Test the numpy report_sepia_filter

    # Check if report can be saved normally to reports
    ip.numpy_color_2_sepia.report_sepia_filter("test_images/rain.jpg", "reports")
    assert os.path.exists("reports/numpy_report_color2sepia.txt")

    # Check if the runtime can be compared with the runtime from the report for the python-implementation 
    ip.numpy_color_2_sepia.report_sepia_filter("test_images/rain.jpg", "reports", "reports/python_report_color2sepia.txt")
    assert os.path.exists("reports/numpy_report_color2sepia.txt")

    # Test the numba report_sepia_filter

    # Check if report can be saved normally to reports
    ip.numba_color_2_sepia.report_sepia_filter("test_images/rain.jpg", "reports")
    assert os.path.exists("reports/numba_report_color2sepia.txt")

    # Check if the runtime can be compared with the runtime from the report for the python-implementation and the numpy-implementation
    ip.numba_color_2_sepia.report_sepia_filter("test_images/rain.jpg", "reports", "reports/python_report_color2sepia.txt", "reports/numpy_report_color2sepia.txt")
    assert os.path.exists("reports/numba_report_color2sepia.txt")


def generate_random_3D_array():
    """
    Generate random 3-dimentional array with pixel values chosen between 0 and 255 to be used in the tests. Set "height" and "width" to be 200 and 251 respectively, in order for the tests to be done in a reasonable amount of time 

    Returns:
        numpy integer 3D array: random 3D array
    """
    return np.random.randint(0, 255, size = (200, 251, 3))
