spam = []
new_item = input()
spam.append(new_item)
count = 0
# a loop for adding items to the array
while True:
  choice = 'n'

  new_item = input()
  spam.append(new_item)
  if count % 5 == 0:
    print('wanna stop ?')
    choice = input()
  if str(choice) == 'y':
    break
  count += 1;
print('do you wanna delete something ?')
choice = input()
if choice == 'y':
 print('what do you want to delete')
 delete = input()
 try:
   spam.remove(delete)
 except:
    print(f'there is no item with the name {delete}')
print(f'the length of the list is {len(spam)}')
print(spam)