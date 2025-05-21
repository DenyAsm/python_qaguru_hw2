# Сложение двух чисел
def add(a, b):
    return a + b

result = add(100, 50)
print(result)


# Функция, которая возвращает максимальное из трёх чисел
def max_of_three(a, b, c):
    return max(a, b, c)

print(max_of_three(100, 55, 83))  # 10


# Проверка, является ли число четным
def is_even(number):
    return number % 2 == 0

print(is_even(100))  # True
print(is_even(77))  # False


# Функция, которая выводит элементы списка
def print_list(items):
    for item in items:
        print(item)

print_list(['Python', 'Selenium', 'Playwright'])