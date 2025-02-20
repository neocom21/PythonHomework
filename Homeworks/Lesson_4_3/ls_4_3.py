

import random

my_list = [random.randint(1,10) for i in range(random.randint(3, 10))]

print(my_list, end=' == ')

list_result =[]

list_result.extend(my_list[:2])
list_result.extend(my_list[-1:])

print(list_result)