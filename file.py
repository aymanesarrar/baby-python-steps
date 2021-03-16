import os
# works like pwd command
print(os.getcwd())
# listing files inside a directory
print(os.listdir('/mnt/c/Users/hp/Desktop/react-projects'))
os.makedirs('hello')
# os.path.abspath() returns an absolute path form of the path passed to it
# os.path.relpath() returns the relative path between two paths passed to it
# os.makedirs() can make folders
# os.path.getsize() returns a file's size
# os.listdir() returns a list of strings of filenames
# os.path.exists() returns true if the filename passed to it exists
# os.path.isfile() and os.path.isdir() returns true if the filename passed is a directory or it's a file