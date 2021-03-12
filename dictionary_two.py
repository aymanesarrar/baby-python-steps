message = input()

count = {}
def __isalpha(char):
  return (char >= 'a' and char <= 'z')
for character in message.lower():
  if (__isalpha(character)):
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)