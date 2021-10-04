import sys 
sys.path.append("..")
from color2 import Color2
import numpy as np

class NumpyColor2Gray(Color2):
    # 4.1:
    def grayscale_filter(self, image):
        """
        Method for converting a image to a gray image using numpy

        args:
            image (integer 3D array): The image that is to be converted

        returns:
            image (numpy integer 3D array): The grayscale image
        """
        # Make a numpy-array with same dimentions and data as the image
        image = np.array(image)

        # Make the grayscale image
        image = np.dot(image[...,:3], [0.07, 0.72, 0.21])

        # Return the grayscale image
        return image
    

    # 4.1:
    def report_grayscale_filter(self, image_filename, *report_files):
        """
        Method for automatically writing a report of the grayscale_filter-function on a given image with the numpy-implementation

        args:
            image_filename (str): The filename and -path to the image that was used for the filter-function
            *report_files (tuple): The filenames and -paths to the other reports that this method is to compare runtimes with
        """
        # Get report
        report = self.get_report("grayscale", __file__, image_filename, *report_files)

        # Write report to file
        f = open(f"numpy_report_color2gray.txt", "w")
        f.write(report)


    # 4.3:
    def grayscale_image(self, input_filename_image, output_filename_image=None):
        """
        Returns a numpy integer 3D array of a gray image of input_filename_image. If output_filename_image is supplied, the created image is saved to the specified location with the specified name

        Args:
            input_filename_image (str): The filename and -path from which the image was read
            output_filename_image (str): The filename and -path to which the image should be saved

        Returns:
            image (numpy integer 3d array): gray image of input_filename_image
        """
        # Make grayscale image
        image = self.make_image(input_filename_image)
        image = self.grayscale_filter(image)

        # Save grayscale image
        self.save_image("grayscale", input_filename_image, output_filename_image, image)

        # Return grayscale image
        return image