import cv2
import time
from numba import jit

@jit
def make_sepia_filter(image):
    height = image.shape[0] # Read the height of the image
    width = image.shape[1] # Read the width of the image

    sepia_matrix = [[ 0.131, 0.534, 0.272],
                    [ 0.168, 0.686, 0.349],
                    [ 0.189, 0.769, 0.393]] # Sepia filter matrix in BGR order
    
    # Make the sepia_image
    for i in range(height):
        for j in range(width):
            # Multiply each color value with the corresponding channel of a pixel with the BGR ordered sepia_matrix
            # Make sure to avoid an overflow when the sum exceeds 255 (uint8 har a max of 255), while keeping the same ratio between the pixels in the image at the correct value relative to each other. Do this by multiplying all of the sums with 0.718, as the largest possible number is 355 for the red value, and 255 / 355 is 0.718.
            for k in range(3):
                image[i][j][k] = (image[i][j][0] * sepia_matrix[k][0] + image[i][j][1] * sepia_matrix[k][1] + image[i][j][2] * sepia_matrix[k][2]) * 0.718

def sepia_filter(filename):
    image = cv2.imread(filename) # Read the image

    make_sepia_filter(image)
    
    # Save the sepia_image
    filename, type = filename.split(".")
    cv2.imwrite(f"{filename}_sepia.{type}", image)

def report_sepia_filter(filename):
    image = cv2.imread(filename) # Read the image

    height = image.shape[0] # Read the height of the image
    width = image.shape[1] # Read the width of the image
    channels = 3

    # Track average runtime after running sepia_filter  3 times
    average = 0
    for i in range(3):
        start = time.time()
        sepia_filter(filename)
        end = time.time()
        average += (end - start)
    average = average / 3 
    average = "{:.3f}".format(average)

    # Write info and runtime to file
    f = open("numba_report_color2sepia.txt", "w")

    python_speedup = calculate_speedup_sepia_filter(float(average), "python_report_color2sepia.txt")
    numpy_speedup = calculate_speedup_sepia_filter(float(average), "numpy_report_color2sepia.txt")

    f.write(f"Timing: numba_color2sepia\nAverage runtime running numba_color2sepia after 3 runs: {average} s\nAverage runtime running of numba_color2sepia is {python_speedup} times faster than python_color2sepia\nAverage runtime running of numba_color2sepia is {numpy_speedup} times faster than numpy_color2sepia\nTiming performed using: time.time()\nImage converted: {filename}\nDimensions of image: ({height}, {width}, {channels})\n\nAdvantages of using Numba instead of Numpy: Much easier to use, fully automated.\nDisadvantages of using Numba instead of Numpy: Harder to debug")

def calculate_speedup_sepia_filter(time, filename):
    """
    Finds average runtime of python_color2sepia and numpy_color2sepia, then calculates and returns speedup
    
    """
    # Find average runtime of python_color2sepia
    f = open(filename)
    next = 0
    python_time = ""
    cont = 1
    for line in f:
        if not cont:
            break
        for word in line.split():
            if next == 1:
                python_time = word
                cont = 0
                break
            elif word == "runs:":
                next = 1
    python_time = float(python_time)
    
    # Calculate and return speedup
    speedup = python_time / time
    speedup = "{:.3f}".format(speedup) # 3 decimals
    return speedup

report_sepia_filter("rain.jpg")