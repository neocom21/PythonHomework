
'''
0 -> 0 днів, 00:00:00
224930 -> 2 дні, 14:28:50
466289 -> 5 днів, 09:31:29
950400 -> 11 днів, 00:00:00
1209600 -> 14 днів, 00:00:00
1900800 - > 22 дні, 00:00:00
8639999 -> 99 днів, 23:59:59
22493 -> 0 днів, 06:14:53
7948799 -> 91 день, 23:59:59
'''

my_variable=input("Введіть число (>=0 та <8640000) (кількість секунд): ")

kol_day, ostatok = divmod(int(my_variable), 24*60*60)

kol_god, ostatok = divmod(ostatok, 60*60)

kol_hvil, kol_sek = divmod(ostatok, 60)

# Слово "день" підбирається на основі кількості днів,
if str(kol_day)[-1:]=='1':
    den_text = "день"
elif str(kol_day)[-1:]>='2' and str(kol_day)[-1:]<='4':
    den_text = "дні"
else:
    den_text = "днів"

print(f"{my_variable} -> {kol_day} {den_text}, {kol_god:02}:{kol_hvil:02}:{kol_sek:02}")

