import re

text = input()
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
found = phone_num_regex.findall(text)
print(found[0].group())

