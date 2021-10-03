import sys 
sys.path.append("..")
from color2 import Color2
import cv2

class PythonColor2Sepia(Color2):
    def sepia_filter(self, input_filename, output_filename=None):
        image = cv2.imread(input_filename) # Read the image

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
        self.save_image("sepia", input_filename, output_filename, image)

        return image

    def report_sepia_filter(self, filename, *report_files):
        report = self.get_report("sepia", __file__, filename, *report_files)

        # Write report to file
        f = open(f"python_report_color2sepia.txt", "w")
        f.write(report)

if __name__ == "__main__":
    pc2s = PythonColor2Sepia()
    pc2s.report_sepia_filter("/Users/martintoft/Documents/IT2019-2022/2021-2022/IN3110/IN3110-matoft/assignment4/rain.jpg")