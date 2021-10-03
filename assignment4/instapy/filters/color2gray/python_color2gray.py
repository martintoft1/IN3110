import sys 
sys.path.append("..")
from color2 import Color2
import cv2

class PythonColor2Gray(Color2):
    def grayscale_filter(self, input_filename, output_filename=None):
        image = cv2.imread(input_filename) # Read the image

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

        # Save the grayscale image
        self.save_image("grayscale", input_filename, output_filename, image)

        # Return the grayscale image
        return image


    def report_grayscale_filter(self, filename, *report_files):
        report = self.get_report("grayscale", __file__, filename, *report_files)

        # Write report to file
        f = open(f"python_report_color2gray.txt", "w")
        f.write(report)


if __name__ == "__main__":
    pc2g = PythonColor2Gray()
    pc2g.report_grayscale_filter("/Users/martintoft/Documents/IT2019-2022/2021-2022/IN3110/IN3110-matoft/assignment4/rain.jpg")