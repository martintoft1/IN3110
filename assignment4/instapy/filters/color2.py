import cv2
import time
import os

# Class that contains all the common methods that the different filter-implementations use
class Color2():
    def save_image(self, filter, input_filename, output_filename, image):
        if output_filename: # Change save location of the filtered image, then save it
            # Get path and filename
            path_bits = output_filename.split("/")
            len_bits = len(path_bits)
            path = ""
            for i in range(len_bits-1):
                path += "/"+path_bits[i]
            # Change save location
            os.chdir(path) 
            # Save the filter image
            filename = path_bits[len_bits-1]
            cv2.imwrite(filename, image)

        else: # Save the filter image
            input_filename, type = input_filename.split(".")
            cv2.imwrite(f"{input_filename}_{filter}.{type}", image)


    def get_report(self, filter, implementation, filename, *report_files):
        image = cv2.imread(filename) # Read the image

        height = image.shape[0] # Read the height of the image
        width = image.shape[1] # Read the width of the image
        channels = 3

        # Track average runtime after running filter 3 times
        average = self.calculate_average_time(filter, filename, 3)

        # Report-string
        report = f"Timing: {implementation}\nImage converted: {filename}\nDimensions of image: ({height}, {width}, {channels})\nAverage runtime running {implementation} after 3 runs: {average} s\nTiming performed using: time.time()"

        # Add speedup to report-string if compared with any other files
        if report_files:
            for file in report_files:
                speedup = self.calculate_speedup_filter(float(average), file)
                bits = file.split("/")
                other_file = ""
                if type(bits) == list:
                    other_file = bits[len(bits)-1]
                else:
                    other_file = bits
                imp, x, algo = other_file.split("_")
                report += f"\nAverage runtime running of {implementation} is {speedup} times faster than {imp}_{algo}"
        
        return report
                

    def calculate_average_time(self, filter, input_filename, runs):
        # Track average runtime after running filter for x runs
        average = 0
        for i in range(runs):
            if filter == "grayscale":
                start = time.time()
                self.grayscale_filter(input_filename)
                end = time.time()
                average += (end - start)
            elif filter == "sepia":
                start = time.time()
                self.sepia_filter(input_filename)
                end = time.time()
                average += (end - start)
        average = average / runs
        average = "{:.3f}".format(average)
        return average


    def calculate_speedup_filter(self, time, input_filename):
        """
        Finds average runtime of one of the filter implementations, then calculates and returns speedup
        
        """
        # Find average runtime of other filter-implementation
        f = open(input_filename)
        next = 0
        other_time = ""
        cont = 1
        for line in f:
            if not cont:
                break
            for word in line.split():
                if next == 1:
                    other_time = word
                    cont = 0
                    break
                elif word == "runs:":
                    next = 1
        other_time = float(other_time)
        
        # Calculate and return speedup
        speedup = other_time / time
        speedup = "{:.3f}".format(speedup) # 3 decimals
        return speedup