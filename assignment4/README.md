## Task 4.1

### Prerequisites

In order to run the code from this task and the following tasks, the user needs to install the packages described in requirements.txt. These packages can be installed from the terminal by first moving to the folder where requirements.txt is located, and then writing

```
python3 -m pip install -r requirements.txt
```

### Functionality 

The different files in this task contains different classes with methods for converting a color-image to a grayscale-image. The different classes also contain methods for writing a report of the average runtime of a grayscale conversion to a file, which can compare the runtime with the runtime of other conversions

### Usage

To convert a color-image to a grayscale-image the user needs to run the following command on one of the Color2Gray-classes in python

```python
grayscale_filter(image)
```

To write a report of the convertion to a file, the user needs to run the following command on one of the Color2Gray-classes in python

```python
report_grayscale_filter(filename, *report_files)
```

where *report_files is the file-path to the reports of the other implementations that filename is to be compared with. *report_files can be empty.


## Task 4.2

### Prerequisites

The same as in task 4.1

### Functionality 

The same as in task 4.1, only that they convert images from a color-image to a sepia-image.

### Usage

To convert a color-image to a sepia-image the user needs to run the following command on one of the Color2Sepia-classes in python

```python
sepia_filter(image)
```

To write a report of the convertion to a file, the user needs to run the following command on one of the Color2Sepia-classes in python

```python
report_sepia_filter(filename, *report_files)
```

where *report_files is the file-path to the reports of the other implementations that filename is to be compared with. *report_files can be empty.


## Task 4.3

### Prerequisites

The same as in task 4.1

### Functionality

Package for the methods implemented in task 4.1 and 4.2. Also contains methods to convert and save an image to a grayscale image to a given location, and the same for sepia image. Lastly contains tests for the functionality implemented in 4.1, 4.2, and this task (4.3). 

### Usage

To install the package the user needs to move to the root directory (instapy) in the terminal and run the following command

```
pip3 install .
```

To convert an image to a grayscale image and save it to a given location the user needs to run the following command on a NumpyColor2Gray-object in python

```python
grayscale_image(input_filename_image, output_filename_image)
```

where output_filename_image is the new filename and path to the grayscale image. output_filename_image can be empty, and if it is the grayscale image will be saved to instapy/filters/tests/test_images.

To convert an image to a sepia image and save it to a given location the user needs to run the following command on a NumpyColor2Sepia-object in python

```python
sepia_image(input_filename_image, output_filename_image)
```

where output_filename_image is the new filename and path to the sepia image. output_filename_image can be empty, and if it is the sepia image will be saved to instapy/filters/tests/test_images.

To run the tests for task 4.1 and 4.2, the user first needs to install the instapy-package. After doing so, the user needs to move to the root-directory of the package and run the following command

```
python3 -m tests.test_instapy.py
```