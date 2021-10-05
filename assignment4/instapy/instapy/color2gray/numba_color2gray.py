import instapy as ip

class NumbaColor2Gray(ip.color_2):
    # 4.1:
    def grayscale_filter(self, image):
        """
        Method for converting a image to a gray image using numba

        args:
            image (integer 3D array): The image that is to be converted

        returns:
            image (integer 3D array): The grayscale image
        """
        # Make the grayscale image
        image = self.make_grayscale_filter(image) 

        # Return the grayscale image
        return image


    # 4.1:
    @staticmethod
    @ip.numba_jit
    def make_grayscale_filter(image):
        """
        The actual method that utilizes numba to create a gray image from an image

        args:
            image (integer 3D array): The image that is to be converted

        returns:
            image (integer 3D array): The grayscale image
        """
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


    # 4.1:
    def report_grayscale_filter(self, input_filename, output_directory,  *report_files):
        """
        Method for automatically writing and saving a report of the grayscale_filter-function on a given image with the numba-implementation

        args:
            input_filename (str): The filename and -path to the image that was used for the filter-function
            output_directory (str): The folder where the report should be saved
            *report_files (tuple): The filenames and -paths to the other reports that this method is to compare runtimes with
        """
        # Get report
        report = self.get_report("grayscale", __file__, input_filename, *report_files)

        # Check if report was written without errors
        if type(report) == Exception:
            raise report 

        # Write report to file
        self.save_report(report, "numba_report_color2gray.txt", output_directory)