import os
# works like pwd command
print(os.getcwd())
# listing files inside a directory
print(os.listdir('/mnt/c/Users/hp/Desktop/react-projects/REACT/crash/python_training'))
# os.chdir() will change the current working directory
# os.path.abspath() returns an absolute path form of the path passed to it
# os.path.relpath() returns the relative path between two paths passed to it
# os.makedirs() can make folders
# os.path.getsize() returns a file's size
# os.listdir() returns a list of strings of filenames
# os.path.exists() returns true if the filename passed to it exists
# os.path.isfile() and os.path.isdir() returns true if the filename passed is a directory or it's a file

files = os.listdir('/mnt/c/Users/hp/Desktop/react-projects/REACT/crash/python_training')
result = 0
for i in files:
  result = result + os.path.getsize(i)
print(result)