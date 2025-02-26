
import string

my_ascii=string.ascii_letters

print("\nДовідково ascii_letters: "+ my_ascii+'\n')

my_variable=input("Ведіть через дефіс дві літери (наприклад: s-H): ")

x1 = my_ascii.index(my_variable[:1])
x2 = my_ascii.index(my_variable[-1:])

print(my_ascii[x1:x2+1])
