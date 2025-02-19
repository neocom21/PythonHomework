# Данні для тесту

list1 = [0, 1, 7, 2, 4, 8] #> (0 + 7 + 4) * 8 = 88
list2 = [1, 3, 5] #=> 30
list3 = [6] #=> 36
list4 = [] #=> 0

list_my = list1.copy() #  присвоїти необхідний тестовий список listX до змінної list_my

if len(list_my) != 0:
    x = sum(list_my[::2])*list_my[-1]
else:
    x = 0

print(x)