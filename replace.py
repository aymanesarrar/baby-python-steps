print('enter a paragraph')
paragraph = input()
# letter_one = input()
# letter_two = input()
def _replace(paragraph, letter_one, letter_two):
  paragraph = list(paragraph)
  for i in range(len(paragraph)):
    if (paragraph[i] == letter_one):
      paragraph[i] = letter_two
  return ''.join(paragraph)
def _reverse(str):
  return ''.join(list(reversed(str)))

str = _reverse(paragraph)
print(str)
