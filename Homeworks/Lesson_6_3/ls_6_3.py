
'''
999 -> 2 # Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729, Потім 7 * 2 * 9 = 126, потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2
1000 -> 0
423 -> 8
33 -> 9
25 -> 0
1 -> 1
'''

my_variable=input("Введіть ціле число: ")

while len(my_variable)>1:
    tmp_rez=1
    for char in my_variable:
        tmp_rez=tmp_rez*int(char)

    my_variable=str(tmp_rez)

print(my_variable)