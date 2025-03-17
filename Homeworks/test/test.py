def counter(func):
    count = 0  # Лічильник викликів

    def wrapper(*args, **kwargs):
        nonlocal count  # Доступ до змінної у зовнішній функції
        count += 1
        print(f"Функція {func.__name__} викликана {count} раз(и)")
        return func(*args, **kwargs)  # Викликаємо оригінальну функцію

    return wrapper  # Повертаємо обгортку


@counter
def example_function():
    print("Inside the function")


example_function()
example_function()
example_function()