import random

computer_number = random.randint(1,100)
mohawala = 0
tries = 5
print('dkhl ra9mk wl3b m3aya hh')
print('bghiti sahla wla s3iba ? hh')
print('khask dkhl 1 (sahla) wla 2 (s3iba) bach yjik misaj')
sahla = 1
s3iba = 2
so3oba = input()

if so3oba == 1 :
  print('nta wa9ila kaytshab lik lhayat sahla l had daraja')
  while True :
    yourNumber = input()
    if int(yourNumber) == computer_number :
      print('you win')
      print('l9itih f ' + str(mohawala) + ' mohawalat hh')
      break
    elif int(yourNumber) < computer_number :
      print('my number is bigger than yours try again')
      mohawala = mohawala + 1
    elif int(yourNumber) > computer_number :
      print('your number is bigger than mine try again')
      mohawala = mohawala + 1
else :
  while tries > 0 :
    yourNumber = input()
    if int(yourNumber) == computer_number :
      print('you win')
      print('l9itih f ' + str(tries) + ' mohawalat hh')
      break
    elif int(yourNumber) < computer_number :
      print('my number is bigger than yours try again')
      tries = tries - 1
    elif int(yourNumber) > computer_number :
      print('your number is bigger than mine try again')
      tries = tries - 1
  print('khsrti azbi wtf wch hmar')