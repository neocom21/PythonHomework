
# Данні для тесту
list1 = [1, 2, 3, 4, 5, 6] #=> [[1, 2, 3], [4, 5, 6]]
list2 = [1, 2, 3] #=> [[1, 2], [3]]
list3 = [1, 2, 3, 4, 5] #=> [[1, 2, 3], [4, 5]]
list4 = [1] #=> [[1], []]
list5 = [] #=> [[], []]

list_result =[]

list_my=list(list1) #  присвоїти необхідний тестовий список listX до змінної list_my

seredina = (len(list_my) + 1) // 2

list_result.append(list_my[:seredina])
list_result.append(list_my[seredina:])

print(list_result)


