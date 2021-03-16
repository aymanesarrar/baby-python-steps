hello_file = open('test_two.txt', 'a')
# there are also shelf files that looks like dictionaries but on files
# The shelve module can store python values in a binary file
# shelve.open() returns a dictionary like shelf value
while True:
  str = input()
  hello_file.write(str + '\n')
  print('wanna continue ?')
  choice = int(input())
  if choice == 0:
    break

hello_file.close()
