'''
# 資料結構
1. list：串列，若有大量資料可以使用，避免宣告過多變數, len, *n, min, append, reverse
2. tuple：元組，結構與串列相同，但值和個數都不能改變，效能較佳
3. set：集合，不重複 set([1, 3, 4, 5, 4, 1])
4. dict：字典，使用 key-value  len, clear, copy, get, items, keys, values
'''

# student = {
#   'name': 'Tony',
#   'age': 20
# }

# print(student.get('namFe', 'YES'))

'''
# 迴圈
1. for：固定次數
for else, break, continue
2. while：不確定次數
'''

students = ['Amy', 'Leo', 'Jack']

# for student in students:
#   print(student)
  
# result = 0

# while(result < 10):
#   result += 1 # result = result + 1
#   print(result)

'''
# 函式
將程式拆解成一個個小單元，方便維護和分工。函式是一種抽象，對流程的抽象

自建函式


def function_name(*args):
  return args

1. 全域變數
2. 區域變數

global

內建函式
len(x)、round(x) range(x)
'''




'''
Class 類別
當某些狀態與功能需要黏在一起時使用類別
類別就像一個鬆餅機一樣可以基於鬆餅類別（class）製作出一個個鬆餅實例（instance）

類別一般會定義 data attribute, data method

繼承

妙蛙種子
小火龍
傑尼龜

bulbasaur
charmander
squirtle

class Pokemon:
  def __init__(self, name):
    self.name = name
    
  def eat(self):
    print('yani yami')

class Charmander(Pokemon):
    def __init__(self, name):
      self.name = name
    def fire(self):
      print('fire!!!')
    
bulbasaur = Pokemon('妙蛙種子')
bulbasaur.eat()
print(bulbasaur.name)

squirtle = Pokemon('傑尼龜')
squirtle.eat()
print(squirtle.name)

class Charmander(Pokemon):
  def __init__(self, name):
    super().__init__(name)
  def fire(self):
    print('fire!!!')  
    
charmander = Charmander('小火龍')
charmander.fire()
print(charmander.name) 
'''

class Pokemon:
  def __init__(self, name):
    self.name = name
  def eat(self):
    print('yami yami')


bulbasaur = Pokemon('妙蛙種子') 
bulbasaur.eat()
print(bulbasaur.name)

squirtle = Pokemon('傑尼龜')
squirtle.eat()
print(squirtle.name)

   
