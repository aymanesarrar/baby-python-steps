myCat = {
  'size': 'fat',
  'color': 'gray',
  'disposition': 'loud'
}
myCat.setdefault('hello', 'world')
keys = list(myCat.keys())
values = list(myCat.values())
items = list(myCat.items())
print(keys)
print(values)
print(items)
for i in keys:
  print(i)
for i in values:
  print(i)
for i in items:
  print(i)
print(myCat.get('size', 1))
