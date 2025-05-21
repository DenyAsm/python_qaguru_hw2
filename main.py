# Сложение двух чисел
def add(a, b):
    return a + b

result = add(1000, 50)
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

# Скрипт определяет функцию, которая принимает имя и возраст пользователя,
# а затем выводит персональное приветствие и говорит, сколько лет будет через 5 лет.

def greet_and_predict(name, age):
    print(f"Привет, {name}!")
    future_age = age + 5
    print(f"Через 5 лет тебе будет {future_age} лет.")

user_name = input("Как тебя зовут? ")
user_age = int(input("Сколько тебе лет? "))

greet_and_predict(user_name, user_age)
