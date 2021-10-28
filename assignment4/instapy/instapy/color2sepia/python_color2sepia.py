import instapy as ip

class PythonColor2Sepia(ip.color_2):
    # 4.2:
    def sepia_filter(self, image):
        """
        Pure python method for converting a image to a sepia image

        args:
            image (integer 3D array): The image that is to be converted

        returns:
            sepia_image (integer 3D array): The sepia image
        """
        height = image.shape[0] # Read the height of the image
        width = image.shape[1] # Read the width of the image

        sepia_matrix = [[ 0.131, 0.534, 0.272],
                        [ 0.168, 0.686, 0.349],
                        [ 0.189, 0.769, 0.393]] # Sepia filter matrix in BGR order


        sepia_image = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append([0, 0, 0])
            sepia_image.append(row)

        # Make the sepia_image
        for i in range(height):
            for j in range(width):
                # Multiply each color value with the corresponding channel of a pixel with the BGR ordered sepia_matrix
                # Make sure to avoid an overflow when the sum exceeds 255 (uint8 har a max of 255), while keeping the same ratio between the pixels in the image at the correct value relative to each other. Do this by multiplying all of the sums with 0.718, as the largest possible number is 355 for the red value, and 255 / 355 is 0.718.
                for k in range(3):
                    sepia_image[i][j][k] = int((image[i][j][0] * sepia_matrix[k][0] + image[i][j][1] * sepia_matrix[k][1] + image[i][j][2] * sepia_matrix[k][2]) * 0.718)

        return sepia_image


    # 4.2:
    def report_sepia_filter(self, input_filename, output_directory,  *report_files):
        """
        Method for automatically writing and saving a report of the sepia_filter-function on a given image with the python-implementation

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
        self.save_report(report, "python_report_color2sepia.txt", output_directory)
