import sys 
sys.path.append("..")
from color2 import Color2
import cv2
import numpy as np

class NumpyColor2Gray(Color2):
    def grayscale_filter(self, input_filename, output_filename=None):
        image = cv2.imread(input_filename) # Read the image

        # Make a numpy-array with same dimentions and data as the image
        image = np.array(image)

        # Make the grayscale image
        image = np.dot(image[...,:3], [0.07, 0.72, 0.21])

        # Save the image
        self.save_image("grayscale", input_filename, output_filename, image) 

        # Return the grayscale image
        return image
    

    def report_grayscale_filter(self, filename, *report_files):
        report = self.get_report("grayscale", __file__, filename, *report_files)

        # Write report to file
        f = open(f"numpy_report_color2gray.txt", "w")
        f.write(report)


if __name__ == "__main__":
    nc2g = NumpyColor2Gray()
    nc2g.report_grayscale_filter("/Users/martintoft/Documents/IT2019-2022/2021-2022/IN3110/IN3110-matoft/assignment4/rain.jpg", "/Users/martintoft/Documents/IT2019-2022/2021-2022/IN3110/IN3110-matoft/assignment4/python_report_color2gray.txt")