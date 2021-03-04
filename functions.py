import random

computer_number = random.randint(1,100)
mohawala = 0
print('dkhl ra9mk wl3b m3aya hh')
while True :
  yourNumber = input()
  if yourNumber == computer_number :
    print('you win')
    print('l9itih f ' + str(mohawala) + ' mohawalat hh')
    break
  elif yourNumber < computer_number :
    print('my number is bigger than yours try again')
    mohawala = mohawala + 1
  elif yourNumber > computer_number :
    print('your number is bigger than mine try again')
    mohawala = mohawala + 1