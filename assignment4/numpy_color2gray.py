import cv2
import time
import numpy as np

def grayscale_filter(filename):
    image = cv2.imread(filename) # Read the image

    height = image.shape[0] # Read the height of the image
    width = image.shape[1] # Read the width of the image

    # Make a numpy-array with same dimentions and data as the image
    grayscale_image = np.array(image)

    # Make the grayscale_image
    grayscale_image = np.dot(grayscale_image[...,:3], [0.07, 0.72, 0.21])

    # Save the grayscale_image
    filename, type = filename.split(".")
    cv2.imwrite(f"{filename}_grayscale.{type}", grayscale_image)


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
    f = open("numpy_report_color2gray.txt", "w")
    python_speedup = calculate_speedup_grayscale_filter(float(average))
    f.write(f"Timing: numpy_color2gray\nAverage runtime running numpy_color2gray after 3 runs: {average} s\nAverage runtime running of numpy_color2gray is {python_speedup} times faster than python_color2gray\nTiming performed using: time.time()\nImage converted: {filename}\nDimensions of image: ({height}, {width}, {channels})")


def calculate_speedup_grayscale_filter(numpy_time):
    """
    Finds average runtime of python_color2gray, calculates and returns speedup
    
    """
    # Find average runtime of python_color2gray
    f = open("python_report_color2gray.txt")
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
    speedup = python_time / numpy_time
    speedup = "{:.3f}".format(speedup) # 3 decimals
    return speedup