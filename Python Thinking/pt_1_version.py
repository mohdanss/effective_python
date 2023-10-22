"""
You can figure out the version of Python you’re using at runtime by inspecting values
in the sys built-in module.
"""

import sys

print(sys.version_info)
print(sys.version)
print(sys.platform)

"""
Things to Remember:
- There are two major versions of Python still in active use: Python 2 and Python 3.
- There are multiple popular runtimes for Python: 
    + CPython, Jython, IronPython, PyPy, etc.
- Be sure that the command-line for running Python on your system is the version you expect it to be.
- Prefer Python 3 for your next project because that is the primary focus of the Python community.
"""
