import re

text = input()
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
found = phone_num_regex.findall(text)
print(found)
text = input()
bat = re.compile(r'Bat(man|mobile|copter|bat|women)')
mo = bat.search(text)
print(mo.group())


