#!/usr/bin/python
import Path_Name
import sys

file = Path_Name.Path_abs(sys.argv[1])
print(file.get_path())
print(file.get_name())