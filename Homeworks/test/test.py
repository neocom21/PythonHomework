def linear_search(arr, target):
    # Ваш код тут

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


# Перевірка
linear_search([64, 34, 25, 12, 22, 11, 90], 22)

