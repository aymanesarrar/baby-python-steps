print('enter a paragraph');
paragraph = input()
letter_one = input()
letter_two = input()
paragraph = list(paragraph)
for i in range(len(paragraph)):
  if (paragraph[i] == letter_one):
    paragraph[i] = letter_two
print(''.join(paragraph))
