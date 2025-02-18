
'''Важливо! Потрібно створити рішення, яке обробляє 3 випадки - список порожній,
у списку парна кількість елементів і в списку непарна кількість елементів.'''

# Данні для тесту
list1 = [1, 2, 3, 4, 5, 6] #=> [[1, 2, 3], [4, 5, 6]]
list2 = [1, 2, 3] #=> [[1, 2], [3]]
list3 = [1, 2, 3, 4, 5] #=> [[1, 2, 3], [4, 5]]
list4 = [1] #=> [[1], []]
list5 = [] #=> [[], []]

list_result =[]

list_my=list4 #  присвоїти необхідний тестовий список listX до змінної list_my

seredina = (len(list_my))//2


if len(list_my)==0:
    list_result.append(list_my)
    list_result.append(list_my)

elif len(list_my)%2 == 0:
    list_result.append(list_my[:seredina])
    list_result.append(list_my[seredina:])
else:
    list_result.append(list_my[:seredina+1])
    list_result.append(list_my[seredina+1:])

print(list_result)


