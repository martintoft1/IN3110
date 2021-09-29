import cv2
import time

def sepia_filter(filename):
    image = cv2.imread(filename) # Read the image

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
    f = open("python_report_color2sepia.txt", "w")
    f.write(f"Timing: python_color2sepia\nAverage runtime running python_color2sepia after 3 runs: {average} s\nTiming performed using: time.time()\nImage converted: {filename}\nDimensions of image: ({height}, {width}, {channels})")

report_sepia_filter("rain.jpg")