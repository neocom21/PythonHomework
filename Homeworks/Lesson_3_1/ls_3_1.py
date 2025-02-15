num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))
my_operator = input("Введіть оператор (+,-,*,/): ")

if my_operator == "+":
    print(f"Результат (+): {num1+num2}")
elif my_operator == "-":
    print(f"Результат (-): {num1-num2}")
elif my_operator == "*":
    print(f"Результат (*): {num1*num2}")
elif my_operator == "/":
    if num2 != 0:
        print(f"Результат (/): {num1/num2}")
    else:
        print("Помилка! На 0 ділити не можна")
else:
    print("Помилка! Введений оператора не існує")