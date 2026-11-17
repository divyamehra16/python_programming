# os-module
"""
os.getcwd() --> returns current working directory
os.chdir() --> changes the current working dir
os.listdir() --> list the contents of a dir
os.mkdir() --> creates a new dir
os.remove() --> delete a File
os.path.join() --> joins path components safely accross platforms
"""

import os
print(os.getcwd())
os.chdir("c:/tmp")
print(os.listdir('.'))
os.mkdir('demo/sub',exist_ok=True)  # create nested directories
print(os.path.join('demo','file.txt'))
