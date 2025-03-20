def prime_generator(end):

    # усі парні числа, крім 2, не є простими числами


    tmp_list = [2]
    yield 2

    for i in range(3, end+1, 2):  # виключаємо всі парні числа, крім двійки (двійку вже додали спочатку)
        is_prime = True
        for j in tmp_list:

            # Доданий код за рекомендаціями для скорочення кількості перевірок
            if j * j > i:  # якщо i складене, то його можна розкласти на два множники
                break
            # =====================

            if i % j == 0: # також число не повинно ділитися на раніше знайдені прості числа
                is_prime = False
                break

        if is_prime:
            tmp_list.append(i)
            yield i


# print(list(prime_generator(80)))

from inspect import isgenerator

gen = prime_generator(1)

assert isgenerator(gen) == True, 'Test0'

assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'

print('Ok')



