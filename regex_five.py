import re


def __rotate_13(str):
  str = list(str)
  for char in range(len(str)):
    if (str[char] >= 'a' and str[char] <= 'm') or (str[char] >= 'A' and str[char] <= 'M'):
      str[char] = chr(ord(str[char]) + 13)
    elif (str[char] >= 'n' and str[char] <= 'z') or (str[char] >= 'N' and str[char] <= 'Z'):
      str[char] = chr(ord(str[char]) - 13)
  return ''.join(str)
# there is a way to increment a character in python like c
# char = 'M'
# char = ch(ord(char) + 1)
# char == 'N'
#  ord return the ascii value of the corresponding character
# ch converts it again into character
names_regex = re.compile(r'Agent \w+')
match = names_regex.findall('Agent Alice gave the secret documents to Agent Bob')
print(match)
print(names_regex.sub('HELLO','Agent Alice gave the secret documents to Agent Bob'))
