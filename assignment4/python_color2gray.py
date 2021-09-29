import cv2
import time

def grayscale_filter(filename):
    image = cv2.imread(filename) # Read the image

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

    # Save the grayscale_image
    filename, type = filename.split(".")
    cv2.imwrite(f"{filename}_grayscale.{type}", image)

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
    f = open("python_report_color2gray.txt", "w")
    f.write(f"Timing: python_color2gray\nAverage runtime running python_color2gray after 3 runs: {average} s\nTiming performed using: time.time()\nImage converted: {filename}\nDimensions of image: ({height}, {width}, {channels})")
    

report_grayscale_filter("rain.jpg")