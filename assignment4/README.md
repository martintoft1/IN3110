# Assignment 4
This assignment contains a python-package named instapy, which uses different filters to alter existing images. The filters have pure python implementations, numpy implementations and numba implementations.

## Task 4.1

### Prerequisites

In order to run the code from this task and the following tasks, the user needs to install the packages described in requirements.txt. These packages can be installed from the terminal by first moving to the folder where requirements.txt is located, and then writing

```
python3 -m pip install -r requirements.txt
```

### Functionality 

The different files in this task contains different classes with methods for converting a color-image to a grayscale-image and returning it. The different classes also contain methods for writing a report of the average runtime of a grayscale conversion to a file, which can compare the runtime with the runtime of other conversions

### Usage

To convert a color-image to a grayscale-image and return it the user needs to run the following command on one of the Color2Gray-classes in python

```python
grayscale_filter(image)
```

To write a report of the convertion to a file, the user needs to run the following command on one of the Color2Gray-classes in python

```python
report_grayscale_filter(input_filename, output_directory,  *report_files)
```

where input_filename is the image that is to be converted, output_directory is the path to which the report should be saved, and *report_files is the file-path to the reports of the other implementations that filename is to be compared with. *report_files can be empty.


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
report_sepia_filter(input_filename, output_directory,  *report_files)
```

where input_filename is the image that is to be converted, output_directory is the path to which the report should be saved, and *report_files is the file-path to the reports of the other implementations that filename is to be compared with. *report_files can be empty.


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

where output_filename_image is the new filename and path to the grayscale image. output_filename_image can be empty, and if it is the grayscale image will be saved to the same directory as input_filename_image.

To convert an image to a sepia image and save it to a given location the user needs to run the following command on a NumpyColor2Sepia-object in python

```python
sepia_image(input_filename_image, output_filename_image)
```

where output_filename_image is the new filename and path to the sepia image. output_filename_image can be empty, and if it is the sepia image will be saved to the same directory as input_filename_image.

To run the tests for tasks, the user first needs to install the instapy-package. After doing so, the user needs to move to the tests-folder inside the instapy-package and run the following command

```
pytest
```


## Task 4.4

### Prerequisites

The same as in task 4.1

### Functionality

User-interface-script to use the filter-methods implemented in 4.1, 4.2 and 4.3.

### Usage

To run the script the user must move to the root of the instapy-package, and type

```python
instapy <flags>
```

where <flags> is the different flags that the user can use to use different functionality in the script. Use the flag -h to get all the different flags and their description.