
y=input("Enter any 4-digit number: ")

x, y = divmod(int(y), 1000)
print(x)

x, y = divmod(int(y), 100)
print(x)

x, y = divmod(int(y), 10)
print(x)

x, y = divmod(int(y), 1)
print(x)
