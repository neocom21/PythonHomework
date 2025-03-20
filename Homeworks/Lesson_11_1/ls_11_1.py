


def prime_generator(end):

    # все четные кроме 2, не являються простыми цифрами
    # так же число не должно делиться на ранее найденные простые числа

    # ... продолжить

    tmp_list=[2]
    yield 2

    for i in range(3, end+1, 2): # исключаем все четные цифры кроме два (два мі уже добавили ранее по умолчанию)
        is_prime = True
        for j in tmp_list:
            if i % j == 0:
                is_prime=False
                break
        if is_prime:
            tmp_list.append(i)
            yield i

'''
    for i in range(3, end+1, 2): # исключаем все четные цифры кроме два (два мі уже добавили ранее по умолчанию)
        is_prime = True
        for j in tmp_list:
            if j * j > i:
                break
            if i % j == 0:
                is_prime=False
                break
        if is_prime:
            tmp_list.append(i)
            yield i

'''

print(list(prime_generator(10)))



# Было


from inspect import isgenerator

gen = prime_generator(1)

assert isgenerator(gen) == True, 'Test0'

assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'

print('Ok')


