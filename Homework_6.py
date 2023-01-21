# ИЗ ДЗ №1
# 5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# x1 = float(input('Please, enter coordinats for first point, x: '))
# y1 = float(input('y: '))
# x2 = float(input('Please, enter coordinats for second point, x: '))
# y2 = float(input('y: '))
# distance = round(((x1-x2)**2 + (y1- y2)**2)**0.5, 2)
# print(f'Distanse between these poins is {distance}')

#  НЕПРИЯТНАЯ ЛЯМБДА

# x1 = float(input('Please, enter coordinats for first point, x: '))
# y1 = float(input('y: '))
# x2 = float(input('Please, enter coordinats for second point, x: '))
# y2 = float(input('y: '))
# calc_distance = (lambda a1,b1, a2, b2: round(((a1-a2)**2 + (b1- b2)**2)**0.5, 2))
# print(f'Distanse between these poins is {calc_distance(x1, y1, x2, y2)}')



# ИЗ ДЗ №2

# 2 Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран,
# а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06
# n = int(input('Please, enter any number: '))
# list_of_numbers = []
# sum=0
# for i in range(1, n+1):
#     num=round ((1 + 1/i)**i, 2)
#     list_of_numbers.append(num)
#     sum +=num
# print(f'Для n = {n} -> {list_of_numbers}\n Сумма {sum}')

# MAP И КОМПРЕХЕНШН
# n = int(input('Please, enter any number: '))
# list_of_numbers = [i for i in range(1, n+1)]
# list_of_numbers = list(map(lambda n: (round((1 + 1/n)**n, 2)), list_of_numbers))
# sum = 0
# for i in range(1, len(list_of_numbers)):
#     sum +=list_of_numbers[i]
# print(f'Для n = {n} -> {list_of_numbers}\n Сумма {sum}')


# ИЗ ДЗ №3

# 1. **Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на позиции с нечетным индексом.
# **Пример:[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# def new_random_list_create():
#     my_list = []
#     for i in range(0, 5):
#         import random
#         after_comma = random.randint(0, 99)
#         if after_comma <10:
#             after_comma = (str(after_comma)).rjust(2, '0')
#         else:
#             after_comma = (str(after_comma))
#         my_list.append(float(str(random.randint(0, 99))+'.'+ after_comma))
#     print(my_list)
#     return my_list
# def find_sum_in_list(any_list):
#     sum=0
#     for i in range(1, len(any_list), 2):
#         sum += any_list[i]
#     return sum
# random_list = new_random_list_create()
# print(find_sum_in_list(random_list))
# print(find_sum_in_list([2, 3, 5, 9, 3]))

import random
my_list = [0 for _ in range(0, 5)]
my_list = list(map(lambda x: random.randint(0, 99), my_list))
print(my_list)

def sum_even(list_num):
    sum = 0
    for i in range( len(list_num)):
        if i % 2: sum += int(list_num[i])
    return sum


print(sum_even(my_list))
# def find_sum_in_list(any_list):
#     sum=0
#     for i in range(1, len(any_list), 2):
#         sum += any_list[i]

# random_list = new_random_list_create()
# print(find_sum_in_list(random_list))
# print(find_sum_in_list([2, 3, 5, 9, 3]))