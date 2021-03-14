import re

# ^ begins with
# $ ends with
# . anything except newline
# .* match anything
# you can match literally everything by passing another argument to the compile function re.DOTALL
str = '<to serve human> for dinner>'
non_greedy = re.compile(r'<(.*?)>')
match = non_greedy.findall(str)
print(match)
greedy = re.compile(r'<(.*)>')
match = greedy.findall(str)
print(match)