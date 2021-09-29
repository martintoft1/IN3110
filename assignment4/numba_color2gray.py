import cv2
import time
from numba import jit

def grayscale_filter(filename):
    image = cv2.imread(filename) # Read the image

    grayscale_image = make_grayscale_filter(image)

    # Save the grayscale_image
    filename, type = filename.split(".")
    cv2.imwrite(f"{filename}_grayscale.{type}", grayscale_image)

@jit
def make_grayscale_filter(image):
    height = image.shape[0] # Read the height of the image
    width = image.shape[1] # Read the width of the image

    # Make the grayscale_image
    for i in range(height):
        for j in range(width):
            # Summarize the weight of the blue, green and red channel, respectively (OpenCV uses BGR, while many other image handling libraries uses RGB)
            weighted_average = int(image[i][j][0] * 0.07 + image[i][j][1] * 0.72 + image[i][j][2] * 0.21) 
            # Apply the weight to the pixel in grayscale_image
            for k in range(3):
                image[i][j][k] = weighted_average
    return image

def report_grayscale_filter(filename):
    image = cv2.imread(filename) # Read the image

    height = image.shape[0] # Read the height of the image
    width = image.shape[1] # Read the width of the image
    channels = 3

    # Track average runtime after running grayscale_filter  3 times
    average = 0
    for i in range(3):
        start = time.time()
        grayscale_filter(filename)
        end = time.time()
        average += (end - start)
    average = average / 3 
    average = "{:.3f}".format(average)

    # Write info and runtime to file
    f = open("numba_report_color2gray.txt", "w")

    python_speedup = calculate_speedup_grayscale_filter(float(average), "python_report_color2gray.txt")
    numpy_speedup = calculate_speedup_grayscale_filter(float(average), "numpy_report_color2gray.txt")

    f.write(f"Timing: numba_color2gray\nAverage runtime running numba_color2gray after 3 runs: {average} s\nAverage runtime running of numba_color2gray is {python_speedup} times faster than python_color2gray\nAverage runtime running of numba_color2gray is {numpy_speedup} times faster than numpy_color2gray\nTiming performed using: time.time()\nImage converted: {filename}\nDimensions of image: ({height}, {width}, {channels})\n\nAdvantages of using Numba instead of Numpy: Much easier to use, fully automated.\nDisadvantages of using Numba instead of Numpy: Harder to debug")


def calculate_speedup_grayscale_filter(numpy_time, filename):
    """
    Finds average runtime of python_color2gray and numpy_color2gray, calculates and returns speedup
    
    """
    # Find average runtime of other color2gray-implementation
    f = open(filename)
    next = 0
    other_time = ""
    cont = 1
    for line in f:
        if not cont:
            break
        for word in line.split():
            if next == 1:
                other_time = word
                cont = 0
                break
            elif word == "runs:":
                next = 1
    other_time = float(other_time)
    
    # Calculate and return speedup
    speedup = other_time / numpy_time
    speedup = "{:.3f}".format(speedup) # 3 decimals
    return speedup
    

report_grayscale_filter("rain.jpg")