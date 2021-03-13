import re

bat = re.compile(r'Bat(wo)?man')
mo = bat.search('the adventures of Batwoman')
phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# the ? character means that it should appears 0 or once
# the * means match 0 or more times
# the + means match 1 or more
# you can specify the number of times between curly braces {}
# {at least, at most}
mo = phone_regex.search('this is my phone number 555-555-5555')
print(mo.group())
bat_regex = re.compile(r'Bat(wo)*man')
mo = bat_regex.search('The adventures of  Batwowowowoman')
print(mo.group())
phone = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
mo = phone.search('555-5555')
print(mo.group())