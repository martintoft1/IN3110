## Task 3.1: Array

### Functionality

Can create an object of the Array-class. This Array can be used to store values of same type in a 1D list. The Array-class has a bunch of magic methods. The methods allows the user to get elements from a specific index in the Array. The methods also allows the user to get the length of the Array, a string-presentation of the Array, and to print out the Array. Furthermore the methods allows the user to add a number or an array to an array, to subtract a number or an array from an array, to multiplicate a number or an array from an array, or the other way around. The methods also allows the user to check if two arrays match, i.e. if they are of the same shape and contains the same elements at the same spots, as well as allowing the user to check for each element in an array if the element is equal to a number or an element from the same index in another array. Lastly, the methods allows the user to find the smallest element in the array.

### Usage 

To get the element from a specific index in an array the user needs to run the following command in python

```python
array.get(index)
```

To get the length of an array the user needs to run the following command in python

```python
len(array)
```

To get the string-representation of an array the user needs to run the following command in python

```python
str(array)
```

To print out the string-representation of an array the user needs to run the following command in python

```python
print(array)
```

To add a number or an array to an array, the user needs to run the following command in python

```python
array = array + other
```

this also works the other way around with the command

```python
array = other + array
```

To subtract a number or an array from an array, the user needs to run the following command in python

```python
array = array - other
```

this also works the other way around with the command

```python
array = other - array
```

To multiplicate a number or an array with an array, the user needs to run the following command in python

```python
array = array * other
```

this also works the other way around with the command

```python
array = other * array
```

To check if array is equal to array2 the user needs to run the following command in python

```python
array == array2
```

To check if the elements in array is equal to another number or array the user needs to run the following command in python

```python
array.is_equal(other)
```

## Task 3.2: Unit Tests

### Functionality 

Tests all the functionality from 3.1

### Usage

To run the tests the user needs to run the following command from the command-line

```python
python3 test_Array.py
```