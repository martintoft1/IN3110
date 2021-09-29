## Task 4.1

### Prerequisites

In order to run the code from this task, the user needs to install the packages described in requirements.txt. These packages can be installed from the terminal by first moving to the folder where requirements.txt is located, and then writing

```
python3 -m pip install -r requirements.txt
```

### Functionality 

The different files in this task contains different methods for converting a color-image to a grayscale-image. The different files also contain methods for writing a report of the average runtime of a conversion to a file, while some of the methods also write if the runtime for the given conversion is faster or slower than one or more of the other conversions. 

### Usage

To convert a color-image to a grayscale-image the user needs to run the following command in python

```python
grayscale_filter(filename)
```

To write a report of the convertion to a file, the user needs to run the following command in python

```python
report_grayscale_filter(filename)
```

which should first be run in the python-version, then the numpy-version, and lastly in the numba-version, in order to get the correct speedup.


## Task 4.2

### Prerequisites

The same as in task 4.1

### Functionality 

The same as in task 4.1, only that they convert images from a color-image to a sepia-image.

### Usage

To convert a color-image to a sepia-image the user needs to run the following command in python

```python
sepia_filter(filename)
```

To write a report of the convertion to a file, the user needs to run the following command in python

```python
report_sepia_filter(filename)
```

which should first be run in the python-version, then the numpy-version, and lastly in the numba-version, in order to get the correct speedup.
