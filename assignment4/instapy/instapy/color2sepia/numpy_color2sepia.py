import numpy as np
import instapy as ip

class NumpyColor2Sepia(ip.color_2):
    # 4.2:
    def sepia_filter(self, image):
        """
        Method for converting a image to a sepia image using numpy

        args:
            image (integer 3D array): The image that is to be converted

        returns:
            image (numpy integer 3D array): The sepia image
        """
        sepia_matrix = [[ 0.131, 0.168, 0.189],
                        [ 0.534, 0.686, 0.769],
                        [ 0.272, 0.349, 0.393]] # Sepia filter matrix in BGR order, ordered downwards in the columns in order to allow it to be used with the image in the np.dot()-method to produce the sepia_image

        # Make a numpy-array with same dimensions and data as the image
        image = np.array(image)

        # Make the sepia_image
        # Make sure to avoid an overflow when the sum exceeds 255 (uint8 har a max of 255), while keeping the same ratio between the pixels in the image at the correct value relative to each other. Do this by multiplying all of the sums with 0.718, as the largest possible number is 355 for the red value, and 255 / 355 is 0.718.
        sepia_matrix = np.dot(0.718, sepia_matrix)
        
        # Multiply each color value with the corresponding channel of a pixel with the BGR ordered sepia_matrix
        image = np.dot(image[...,:3], sepia_matrix)

        # Convert to int
        image = image.astype(int)

        return image


    # 4.2:
    def report_sepia_filter(self, input_filename, output_directory,  *report_files):
        """
        Method for automatically writing and saving a report of the sepia_filter-function on a given image with the numpy-implementation

        args:
            input_filename (str): The filename and -path to the image that was used for the filter-function
            output_directory (str): The folder where the report should be saved
            *report_files (tuple): The filenames and -paths to the other reports that this method is to compare runtimes with
        """
        # Get report
        report = self.get_report("sepia", __file__, input_filename, *report_files)

        # Check if report was written without errors
        if type(report) == Exception:
            raise report 

        # Write report to file
        self.save_report(report, "numpy_report_color2sepia.txt", output_directory)
        

    # 4.3:
    def sepia_image(self, input_filename_image, output_filename_image=None):
        """
        Returns a numpy integer 3D array of a sepia image of input_filename_image. If output_filename_image is supplied, the created image is saved to the specified location with the specified name

        Args:
            input_filename_image (str): The filename and -path from which the image was read
            output_filename_image (str): The filename and -path to which the image should be saved

        Returns:
            image (numpy integer 3d array): sepia image of input_filename_image
            FileNotFoundError: If input_filename_image or output_filename_image is not found
            TypeError: If image_filename doesn't contain an image
        """
        # Make image
        image = self.make_image(input_filename_image)
        if type(image) is Exception:
            raise image

        # Make sepia image
        image = self.sepia_filter(image)

        # Save sepia image
        self.save_image("sepia", input_filename_image, output_filename_image, image)

        # Return sepia image
        return image
