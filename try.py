print('how many cats do you have ?')
numver_of_cats = input()

try:
  if int(numver_of_cats) >= 2:
    print(f"{numver_of_cats} ?? that is a lot of cats")
  else:
    print(f"{numver_of_cats} ?? that is not a lot of cats")
except:
  print('this is not a number')
