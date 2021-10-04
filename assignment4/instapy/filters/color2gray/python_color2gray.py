import sys 
sys.path.append("..")
from color2 import Color2

class PythonColor2Gray(Color2):
    # 4.1:
    def grayscale_filter(self, image):
        """
        Pure python method for converting a image to a gray image

        args:
            image (integer 3D array): The image that is to be converted

        returns:
            image (integer 3D array): The grayscale image
        """
        height = image.shape[0] # Read the height of the image
        width = image.shape[1] # Read the width of the image

        # Make the grayscale image
        for i in range(height):
            for j in range(width):
                # Summarize the weight of the blue, green and red channel, respectively (OpenCV uses BGR, while many other image handling libraries uses RGB)
                weighted_average = int(image[i][j][0] * 0.07 + image[i][j][1] * 0.72 + image[i][j][2] * 0.21) 
                # Apply the weight to the pixel in grayscale_image
                for k in range(3):
                    image[i][j][k] = weighted_average

        # Return the grayscale image
        return image


    # 4.1:
    def report_grayscale_filter(self, filename, *report_files):
        """
        Method for automatically writing a report of the grayscale_filter-function on a given image with the python-implementation

        args:
            image_filename (str): The filename and -path to the image that was used for the filter-function
            *report_files (tuple): The filenames and -paths to the other reports that this method is to compare runtimes with
        """
        report = self.get_report("grayscale", __file__, filename, *report_files)

        # Write report to file
        f = open(f"python_report_color2gray.txt", "w")
        f.write(report)



if __name__ == "__main__":
    pc2g = PythonColor2Gray()
    pc2g.report_grayscale_filter("/Users/martintoft/Documents/IT2019-2022/2021-2022/IN3110/IN3110-matoft/assignment4/rain.jpg")