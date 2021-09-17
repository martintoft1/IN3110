import sys

class Array:

    def __init__(self, shape, *values):
        """
        
        Initialize an array of 1-dimensionality. Elements can only be of type:
        - int
        - float
        - bool
        
        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).

        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either numeric or boolean.

        Raises:
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """
        # Read shape
        self._length = shape[0]

        # Check if length is the same as the length of values
        if not self._length == len(values):
            raise ValueError("Number of values does not fit with the shape")

        # Read array
        self._array = [0] * self._length
        for i in range(self._length):
            self._array[i] = values[i]
        
        # Check if the values are of valid type
        isInt=0
        isFloat=0
        isBool=0
        for val in self._array:
            if isinstance(val, bool):
                if not isBool:
                    isBool=1
                    if isFloat or isInt:
                        raise ValueError("Not all values are of the same type") 
            elif isinstance(val, int):
                if not isInt:
                    isInt=1
                    if isFloat or isBool:
                        raise ValueError("Not all values are of the same type") 
            elif isinstance(val, float):
                if not isFloat:
                    isFloat=1
                    if isInt or isBool:
                        raise ValueError("Not all values are of the same type") 
            else:
                raise ValueError("Not all values are of accepted types") 

    def __getitem__(self, item):
        """Returns value of item in array.
            Args:
                item (int): Index of value to return.
            Returns:
                value: Value of the given item.
        """
        return self._array[item]

    def __str__(self):
        """Returns a nicely printable string representation of the array.

        Returns:
            str: A string representation of the array.

        """
        str="["
        if self._length > 0:
            str+=f"{self._array[0]}"
        for i in range(1, self._length):
            str+=f", {self._array[i]}"
        str+="]"
        return str


    def __len__(self):
        """Returns the length of the array.

        Returns:
            int: The length of the array.

        """
        return self._length


    def __add__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        if self.same_type(other):
            newElements = list()
            if isinstance(other, Array):
                lenOther = len(other)
                if (self._length == lenOther):
                    for i in range(self._length):
                        newElements.append(self._array[i] + other[i])
                else:
                    return NotImplemented
            else:
                for i in range(self._length):
                    newElements.append(self._array[i] + other)
            return Array((self._length,), *tuple(newElements))
        else:
            return NotImplemented


    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        return self.__add__(other)

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.

        Returns:
            Array: the difference as a new array.

        """
        if self.same_type(other):
            newElements = list()
            if isinstance(other, Array):
                lenOther = len(other)
                if (self._length == lenOther):
                    for i in range(self._length):
                        newElements.append(self._array[i] - other[i])
                else:
                    return NotImplemented
            else:
                for i in range(self._length):
                    newElements.append(self._array[i] - other)
            return Array((self._length,), *tuple(newElements))
        else:
            return NotImplemented

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number being subtracted from.

        Returns:
            Array: the difference as a new array.

        """
        return self.__sub__(other)

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        if self.same_type(other):
            newElements = list()
            if isinstance(other, Array):
                lenOther = len(other)
                if (self._length == lenOther):
                    for i in range(self._length):
                        newElements.append(self._array[i] * other[i])
                else:
                    return NotImplemented
            else:
                for i in range(self._length):
                    newElements.append(self._array[i] * other)
            return Array((self._length,), *tuple(newElements))
        else:
            return NotImplemented

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.

        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.

        Args:
            other (Array): The array to compare with this array.

        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.

        """
        if self.same_type(other):
            if isinstance(other, Array):
                lenOther = len(other)
                if (self._length == lenOther):
                    for i in range(self._length):
                        if not self._array[i] == other[i]:
                            return False
                    return True
        return False

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.

        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.

        Args:
            other (Array, float, int): The array or number to compare with this array.

        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.

        Raises:
            ValueError: if the shape of self and other are not equal.
            NotImplemented: if the types of self and other are not equal.

        """
        if self.same_type(other):
            newElements = list()
            if isinstance(other, Array):
                lenOther = len(other)
                if (self._length == lenOther):
                    for i in range(self._length):
                        if self._array[i] == other[i]:
                            newElements.append(True)
                        else:
                            newElements.append(False)
                else:
                    return ValueError
            else:
                for i in range(self._length):
                    if self._array[i] == other:
                        newElements.append(True)
                    else:
                        newElements.append(False)
            return Array((self._length,), *tuple(newElements))
        elif isinstance(other, Array):
            if isinstance(other[0], bool) or isinstance(other[0], int) or isinstance(other[0], float):
                return NotImplemented
        else:
            return TypeError
            
    
    def min_element(self):
        """Returns the smallest value of the array.

        Only needs to work for type int and float (not boolean).

        Returns:
            float: The value of the smallest element in the array.

        """
        if self._length > 0:
            if isinstance(self._array[0], int) or isinstance(self._array, float):
                smallest = self._array[0]
                for i in range(1, self._length):
                    if self._array[i] < smallest:
                        smallest = self._array[i]
                return smallest
            else:
                return TypeError
        else:
            return 0

    def same_type(self, other):
        """Checks if type of values in Array is equal to type of values in another Array or number.

        Args:
            other (Array, float, int): The array or number to check if has the same type as this array.

        Returns:
            A Boolean with True if the values are of same type, or False if the values are not of same type.

        """
        if self._length != 0: 
            if (isinstance(other, Array)):
                if len(other) > 0:
                    if self._array[0].__class__ == other[0].__class__: # Arrays must consist of same types, so if class of first elements is equal then so are the rest
                        if (isinstance(self._array[0], bool) and not isinstance(other[0], bool)) or (not isinstance(self._array[0], bool) and isinstance(other[0], bool)): # Special case, must check because bool is subtype of int
                            return False
                    else:
                        return False
        
            elif isinstance(other, bool):
                if not isinstance(self._array[0], bool):
                    return False
            
            elif isinstance(other, int):
                if not isinstance(self._array[0], int):
                    return False
            
            elif isinstance(other, float):
                if not isinstance(self._array[0], float):
                    return False

            else:
                return False
    
        return True