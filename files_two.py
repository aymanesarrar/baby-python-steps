hello_file =  open('test.txt')
# you can only use read or readlines
# print(hello_file.readlines())
# w write mode
# a append mode
str = list(hello_file.read())


count = 0
for i in str:
  if i == 'a':
    count = count + 1

print(count)
hello_file.close()