import random


def random_numbers(start, end, num):
    random_list = []
    for _ in range(num):
        random_list.append(random.randint(start, end))
    return random_list

# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y