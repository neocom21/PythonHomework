
def add_one(some_list):
    s = "".join(str(el) for el in some_list)
    ss = list(str(int(s) + 1))
    return [int(x) for x in ss]

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")

