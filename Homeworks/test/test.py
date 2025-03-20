def prime_generator(end):
    primes = [2]
    yield 2  # Первое простое число

    for i in range(3, end + 1, 2):  # Проверяем только нечётные числа
        for j in primes:
            if j * j > i:  # Если j больше sqrt(i) → дальше проверять не нужно
                break
            if i % j == 0:  # Если i делится на j → не простое
                break
        else:  # Если `break` не сработал на делении, то число простое
            primes.append(i)
            yield i

print(list(prime_generator(10)))

