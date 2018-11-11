#!/usr/bin/python
import sys
import os
class Path_abs():
	def __init__(self,file):
		self.file=file
	def get_path(self):
		path= os.path.dirname(self.file)
		return path
	def get_name(self):
		name = os.path.basename(self.file)
		return name