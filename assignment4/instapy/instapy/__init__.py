# Import classes with methods that are to be used in the package
# Numba
from numba import jit
numba_jit = jit

# Class with common filter methods
from instapy.color2 import Color2
color_2 = Color2

# Python gray filter
from .color2gray.python_color2gray import PythonColor2Gray
python_color_2_gray = PythonColor2Gray()

# Numpy gray filter
from .color2gray.numpy_color2gray import NumpyColor2Gray
numpy_color_2_gray = NumpyColor2Gray()

# Numba gray filter
from .color2gray.numba_color2gray import NumbaColor2Gray
numba_color_2_gray = NumbaColor2Gray()

# Python sepia filter
from .color2sepia.python_color2sepia import PythonColor2Sepia
python_color_2_sepia = PythonColor2Sepia()

# Numpy sepia filter
from .color2sepia.numpy_color2sepia import NumpyColor2Sepia
numpy_color_2_sepia = NumpyColor2Sepia()

# Numba sepia filter
from .color2sepia.numba_color2sepia import NumbaColor2Sepia
numba_color_2_sepia = NumbaColor2Sepia()