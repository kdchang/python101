import random

def fight(ch):
  c_choice = random.randint(0, 2) # 0 - 2 (0, 1, 2 隨機數)
  print(c_choice)
  if ch == 0:
    print('你派了妙蛙種子')
    if c_choice == 0:
      print('對方派出妙蛙種子，平分秋色！')
    elif c_choice == 1:
      print('對方派出小火龍，屬性相剋，你輸了！')
    elif c_choice == 2:
      print('對方派出傑尼龜，你贏了！')
  elif ch == 1:
    print('你派了小火龍')
    if c_choice == 0:
      print('對方派出妙蛙種子，耶，你贏了！')
    elif c_choice == 1:
      print('對方派出小火龍，平分秋色！')
    elif c_choice == 2:
      print('對方派出傑尼龜，屬性相剋，你輸了！')
  elif ch == 2:
    print('你派了傑尼龜')
    if c_choice == 0:
      print('對方派出妙蛙種子，屬性相剋，你輸了！')
    elif c_choice == 1:
      print('對方派出小火龍，耶，你贏了！')
    elif c_choice == 2:
      print('對方派出傑尼龜，平分秋色！')

def start():
  return int(input('請選擇是否進行對戰 XDDB？ 0.開始對戰 1. 走為上策'))
  
command = start()
print('outer', command)

while command != 1:
  choice = int(input('請問你要派哪隻神奇寶貝呢？0. 妙蛙種子 1.小火龍 2. 傑尼龜'))
  fight(choice)
  command = start()
    
print('遊戲結束')

