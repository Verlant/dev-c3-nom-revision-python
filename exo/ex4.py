import random


def generate_random_number_list():
    numbers = []
    for i in range(0, int(random.random() * 100)):
        numbers.append(int(random.random() * 100))
    return numbers


def find_min_in_number_list(numbers):
    min = numbers[0]
    for n in numbers:
        if n < min:
            min = n
    return min


def find_max_in_number_list(numbers):
    max = 0
    for n in numbers:
        if n > max:
            max = n
    return max


def calcul_average_in_number_list(numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum / len(numbers)


numbers = generate_random_number_list()
print("list :", numbers)
print("min :", find_min_in_number_list(numbers))
print("max :", find_max_in_number_list(numbers))
print("average :", calcul_average_in_number_list(numbers))
