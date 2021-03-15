import re


email = re.compile(r'\w+@\w+\.\w+')
str = '''
monopole@yahoo.com
jmmuller@outlook.com
seasweb@me.com
bsikdar@me.com
stern@hotmail.com
wojciech@msn.com
wiseb@mac.com
smcnabb@comcast.net
benanov@msn.com
mcsporran@optonline.net
sinclair@gmail.com
geoffr@outlook.com
'''
match = email.findall(str)
print(match)