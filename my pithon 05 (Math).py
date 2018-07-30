# Ask Python to print sqrt(25) on line 3.
import math
print math.sqrt(25)

from math import sqrt
print sqrt(16)

# Ask Python to print sqrt(25) on line 10.
from math import *
print sqrt(25)

# Листинг модуля math
import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!