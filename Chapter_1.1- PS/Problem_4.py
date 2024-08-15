# Q.Write a python program to print the contents of a directory using the os module. 

import os

# Here we can select the directory of the content I want to list 
directory_path = '/Users/rayya'

# Use the os module to list the directory content
contents = os.listdir(directory_path)

# Here it will print the content of the selected directory
for items in contents:
    print (items)