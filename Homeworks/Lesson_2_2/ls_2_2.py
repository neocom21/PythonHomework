
y= input("Enter any 5-digit number: ")

x1, y = divmod(int(y), 10000)

x2, y = divmod(int(y), 1000)

x3, y = divmod(int(y), 100)

x4, y = divmod(int(y), 10)

print(y)
print(x4)
print(x3)
print(x2)
print(x1)
