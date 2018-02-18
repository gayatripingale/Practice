"""
The Python Standard Library is organised into parts called modules. 
Many modules are simply Python files, like the Python scripts you've already used and written. 
In order to be able to use the code contained in a module 
we must import it, either in the interactive interpreter or in a Python script of our own.

Every module in the standard library is lowercased.

The syntax for importing a module is simply 
import package_name.
E.g.
in order to use the factorial function, we can call it, 
starting with the module name math, then a dot (.) 
and then the function name factorial().


"""

import math
print(math.factorial(3))
print(math.exp(3))