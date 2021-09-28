## Task 4.1

### Prerequisites

In order to run the code from this task, the user needs to install the packages described in requirements.txt. These packages can be installed from the terminal by first moving to the folder in which the requirements.txt is located, and then writing

```
python3 -m pip install -r requirements.txt
```

### Functionality 

The different files in this task contains different methods for converting a color-image to a grayscale-image. The different files also contain methods for writing a report the average runtime of a conversion to a file, while some of the methods also write if the runtime for the given conversion is faster or slower than one or more of the other conversions. 

### Usage

To convert a color-image to a grayscale-image the user needs to run the following command in python

```python
grayscale_filter(filename)
```

To write a report of the convertion to a file, the user needs to run the following command in python

```python
track_runtime_grayscale_filter(filename)
```