# Данні для тесту
list1 = [12, 3, 4, 10] # => [10, 12, 3, 4]
list2 = [1]#  => [1]
list3 = [] # => []
list4 = [12, 3, 4, 10, 8] #  => [8, 12, 3, 4, 10

list_my=list4 #  присвоїти необхідний тестовий список listX до змінної list_my

if len(list_my)!=1 and len(list_my)!=0:
    x = list_my.pop()
    list_my.insert(0,x)

print(list_my)

