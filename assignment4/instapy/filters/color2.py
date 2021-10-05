import cv2
import time
import os
import imghdr 

"""
Contains all the common methods that the different filter-implementations use
"""
class Color2():
    # 4:
    def make_image(self, image_filename):
        """
        Makes image from a file path

        Args:
            image_filename (str): The filename and -path to the image

        Returns:
            image (3D array): The image from the described file-path
            FileNotFoundError: If image_filename is not found
            TypeError: If image_filename doesn't contain an image
        """
        # Check if image-file exists
        if not os.path.exists(image_filename):
            raise FileNotFoundError(image_filename)
        else:
            if imghdr.what(image_filename) == None:
                raise TypeError(image_filename)

        # Read image from file
        image = cv2.imread(image_filename)

        return image


    # 4.3:
    def save_image(self, filter, input_filename_image, output_filename_image, image):
        """
        Saves an image to the current directory, or to an other directory with an other name if its given

        Args:
            filter (str): The filter that was used to convert the image
            input_filename_image (str): The filename and -path from which the image was read
            output_filename_image (str): The filename and -path to which the image should be saved
            image (3D array): The image that should be saved
        """
        # Check if input imagefile and -path exists
        if not os.path.exists(input_filename_image):
            raise FileNotFoundError(input_filename_image)

        if output_filename_image: # Change save location of the filtered image, then save it
            # Get path and filename
            path_bits = output_filename_image.split("/")
            len_bits = len(path_bits)
            new_path = path_bits[0]
            for i in range(1, len_bits-1):
                new_path += "/"+path_bits[i]

            # Check if output imagepath exists
            if not os.path.exists(new_path):
                raise FileNotFoundError(new_path)

            # Save old path
            old_path = os.getcwd() 

            # Change save location
            os.chdir(new_path) 

            # Save the filter image
            filename = path_bits[len_bits-1]
            cv2.imwrite(filename, image)

            # Go back to old path
            os.chdir(old_path)

        else: # Save the filter image
            input_filename_image, type = input_filename_image.split(".")
            cv2.imwrite(f"{input_filename_image}_{filter}.{type}", image)


    # 4.1 and 4.2:
    def get_report(self, filter, implementation, image_filename, *report_files):
        """
        Creates a string containing a report of an image-conversion, along with a comparison of runtimes if compared to other reports

        Args:
            filter (str): The filter that was used to convert the image
            implementation (str): The name of the file that executed the method report-method (the unique "implementation" of the filter-method, e.g. "python_color2gray.py").
            image_filename (str): The filename and -path to the image
            *report_files (tuple): The filenames and -paths to the other reports that this report is to compare runtimes with

        Returns:
            report (str): The report
            FileNotFoundError: If image_filename is not found
        """
        # Read the image and check if it was read correctly
        image = self.make_image(image_filename) 
        if type(image) == Exception:
            raise image

        height = image.shape[0] # Read the height of the image
        width = image.shape[1] # Read the width of the image
        channels = 3

        # Track average runtime after running filter 3 times
        average = self.calculate_average_time(filter, image, 3)

        # Get filename from implementation
        implementation_filename = os.path.basename(implementation)

        # Report-string
        report = f"Timing: {implementation_filename}\nImage converted: {image_filename}\nDimensions of image: ({height}, {width}, {channels})\nAverage runtime running {implementation_filename} after 3 runs: {average} s\nTiming performed using: time.time()"

        # Add speedup to report-string if compared with any other files
        if report_files:
            for file in report_files:
                # Calculate speedup
                speedup = self.calculate_speedup_filter(float(average), file)

                # Check for exceptions
                if type(speedup) == Exception:
                    raise speedup

                # Add speedup-string
                bits = file.split("/")
                other_file = ""
                if type(bits) == list:
                    other_file = bits[len(bits)-1]
                else:
                    other_file = bits
                imp, x, algo = other_file.split("_")
                report += f"\nAverage runtime running of {implementation_filename} is {speedup} times faster than {imp}_{algo}"
        
        return report
                

    # 4.1 and 4.2:
    def calculate_average_time(self, filter, image, runs):
        """
        Tracks average runtime after running filter for a given amount of runs

        Args:
            filter (str): The filter that was used to convert the image
            image (3D array): The image that is to be converted using filter
            runs (int): The amount of runs of filter-function before calculating average runtime
            

        Returns:
            average (float): The average runtime in seconds with three decimals
        """
        average = 0

        for i in range(runs):
            if filter == "grayscale":
                start = time.time()
                self.grayscale_filter(image)
                end = time.time()
                average += (end - start)
            elif filter == "sepia":
                start = time.time()
                self.sepia_filter(image)
                end = time.time()
                average += (end - start)

        average = average / runs
        average = "{:.4f}".format(average)

        return average


    # 4.1 and 4.2:
    def calculate_speedup_filter(self, time, report_filename):
        """
        Calculates and returns the speedup from the filter-implementation that called the method to the filter-implementation from the report

        Args:
            time (float): The average runtime of the filter-implementation that called the method
            report_filename (str): The filename and -path of the report that the method is to find average runtime of and calculate speedup thereafter
        
        Returns:
            speedup (float): The speedup from the filter-implementation that called the method to the filter-implementation from the report
            FileNotFoundError: If report_filename is not found
        """
        # Check if report-file and -path exists
        if not os.path.exists(report_filename):
            raise FileNotFoundError(report_filename)

        # Find average runtime of other filter-implementation
        f = open(report_filename)
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
        
        # Calculate speedup
        speedup = other_time / time
        speedup = "{:.4f}".format(speedup) # 4 decimals

        # Return speedup
        return speedup

    
    # 4.1 and 4.2:
    def save_report(self, report, output_filename, output_directory):
        """
        Saves report with given name to given directory

        Args:
            report (str): The report that is to be saved to file
            output_filename (str): The name of the file that is to be saved
            output_directory (str): The path where the file is to be saved
        
        Returns:
            FileNotFoundError: If output_directory is not found
        """
        # Check if output-directory exists
        if not os.path.exists(output_directory):
            raise FileNotFoundError(output_directory)
        
        # Save old path
        old_path = os.getcwd() 

        # Change save-location
        os.chdir(output_directory) 

        # Write report to file
        f = open(output_filename, "w")
        f.write(report)

        # Go back to old path
        os.chdir(old_path)