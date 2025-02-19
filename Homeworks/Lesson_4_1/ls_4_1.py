# Данні для тесту

list1 = [0, 1, 0, 12, 3] #-> [1, 12, 3, 0, 0]
list2 = [0] #-> [0]
list3 = [1, 0, 13, 0, 0, 0, 5] #-> [1, 13, 5, 0, 0, 0, 0]
list4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] #-> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

list_my=list4.copy() #  присвоїти необхідний тестовий список listX до змінної list_my

list_0=[]

while list_my.count(0)>0:
    list_my.remove(0)
    list_0.append(0)

list_my.extend(list_0)

print(list_my)
