def add_one(some_list):
	s=""
	while len(some_list) > 0:
		s+=str(some_list.pop(0))

	ss=list(str(int(s) + 1))

	return [int(x) for x in ss]



assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")

