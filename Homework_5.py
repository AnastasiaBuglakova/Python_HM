# 1 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданноеколичество конфет.Играют два игрока, делая ход друг после друга.Первый ход
# определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'


# import random
# candy_quantity = int(input('Please, enter quantity of candy for start, number more tnan 60:'))
# flag_bot = False
# # Кидаем жребий, чтобы узнать кто начинает
# starting_gamer = random.choice(['you', 'Bot'])
# print(f'{starting_gamer} will start')
#
# if starting_gamer == 'Bot':
#     if candy_quantity % 29:
#         bot_step = candy_quantity % 29
#     else: bot_step = 1
#     candy_quantity = candy_quantity - bot_step
#     print(f'Bot took {bot_step} candies, rest is {candy_quantity}')
# your_step = 0
#
# while candy_quantity > 0:
#
#     # мой ход
#     your_step = int(input('Please, enter quantity of candy, you would like to take (less than 28):'))
#     if your_step not in [i for i in range(1, 29)]:
#         print('Please, enter right number:')
#     candy_quantity = candy_quantity - your_step
#     print(f'You took {your_step} candies, rest is {candy_quantity}')
#     if candy_quantity == 0:
#         print (f"Rest is in your's hands, YOU have won")
#         break
#
#     # ход бота
#     if candy_quantity % 29:
#         bot_step = candy_quantity % 29
#     else:
#         bot_step = random.randint(1, 29)
#     candy_quantity = candy_quantity - bot_step
#     print(f'Bot took {bot_step} candies, rest is {candy_quantity}')
#     if candy_quantity == 0:
#         print(f"Rest is in bot's hands, bot has won")
#         break






# 2 Создайте программу для игры в 'Крестики-нолики' НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

import random
dict_x = {i:i for i in range(1,10)}
def show_X_0(dict_X_0):
    for i in range(0,9,3):
        print(f'| {dict_X_0[1+i]} | {dict_X_0[2+i]} | {dict_X_0[3+i]} |')

# cоздадим библиотеку победы
str = 'X'
def event(dict_x, gamer):
    win = False
#  ищу комбиранции с центра
    if dict_x[5] == gamer and dict_x[1] == gamer and dict_x[9] == gamer: win = True
    if dict_x[5] == gamer and dict_x[2] == gamer and dict_x[8] == gamer: win = True
    if dict_x[5] == gamer and dict_x[4] == gamer and dict_x[6] == gamer: win = True
    if dict_x[5] == gamer and dict_x[7] == gamer and dict_x[3] == gamer: win = True
# ищу комбиранции боковые
    if dict_x[2] == gamer and dict_x[1] == gamer and dict_x[3] == gamer: win = True
    if dict_x[4] == gamer and dict_x[1] == gamer and dict_x[7] == gamer: win = True
    if dict_x[8] == gamer and dict_x[7] == gamer and dict_x[9] == gamer: win = True
    if dict_x[6] == gamer and dict_x[3] == gamer and dict_x[9] == gamer: win = True
    if win:
        return win

count = 0
# Кидаем жребий, чтобы узнать кто начинает
starting_gamer = random.choice(['X', '0'])
print(starting_gamer)
if starting_gamer == '0':
    # шаг бота вписываем 0 на поле 5
    bot_pos = 5
    dict_x[5] = '0'
    show_X_0(dict_x)
    count += 1
    print(f'шаг #{count} 0 на позицию: {bot_pos}')

while count < 10:

    # мой шаг___________________________________________________________________________________________________
    pos = int(input('Введите позицию (целое число от 1 до 9 включительно):'))
    if pos not in [i for i in range(1,10)]:
        while pos not in [i for i in range(1, 10)]:
            print('Выбери, пожалуйста, целое число от 1 до 9 включительно')
            pos = int(input('Введите позицию:'))
    if dict_x[pos] != pos:
        while dict_x[pos] != pos:
            print('Выбери, пожалуйста, свободное поле')
            pos = int(input('Введите позицию:'))
    dict_x[pos] = 'X'

    # после каждого шага:
    # 1 показываю поле,
    # 2 ув. счетчик
    # 3 вывожу информацию о сделанном ходе в тексте
    # 4 проверяю была ли победа
    show_X_0(dict_x)
    count +=1
    print(f'шаг #{count} X на позицию: {pos}\n')

    if count == 9:
        print(f'Ничья!!!!\nИгра окончена.')
        break

    if event(dict_x, 'X'):
        print(f'Игрок #X выиграл!!!!\nИгра окончена.')
        break

    # шаг бота______________________________________________________________________________

    # ходит вторым, Х уже занял одно место
    if count == 1:
        if dict_x[5] == 5:
            bot_pos = 5
            dict_x[bot_pos] = '0'

        else:
            bot_pos = 1
            dict_x[bot_pos] = '0'

    # ходил первым, Х уже занял одно место и 0 на позиции 5 или 1
    elif count == 2:
        if dict_x[1] == 1:
            bot_pos = 1
            dict_x[1] = '0'
        else:
            dict_x[3] = '0'
            bot_pos = 3


    # шаг 3 и более, значит у нас как минимум 2 икса и 1 ноль уже стоит (и место его либо 5 либо 1),
    elif count > 2 and count < 9:
        # первым делом ищем выигрышную позицию для 0
        # создаю копию словаря игрового поля
        j = 1
        flag = False
        while j < 10 and not flag:
            checking_dict = dict_x.copy()
            if checking_dict[j] == j:
                checking_dict[j] = '0'
                if event(checking_dict, '0'):
                    dict_x[j] = '0'
                    bot_pos = j
                    flag = True
            j += 1

        #  если 0 еще не может выиграть, то должен блокирнуть выигрыш Х
        if not flag:
            j = 1
            while j < 10 and not flag:
                checking_dict = dict_x.copy()
                if checking_dict[j] == j:
                    checking_dict[j] = 'X'
                    if event(checking_dict, 'X'):
                        dict_x[j] = '0'
                        bot_pos = j
                        flag = True


                j +=1

        # если нет победных сочетаний ни для 0 ни для Х, бот занимает место  в потенциально выигрышной линии (где есть 0 и нет Х)
        if not flag:
            if dict_x[5] == '0':
                # диагонали
                if dict_x[1] != 'X' and dict_x[9] != 'X':
                    dict_x[9] = '0'
                    bot_pos = 9
                    flag = True

                elif dict_x[3] != 'X' and dict_x[7] != 'X':
                    dict_x[7] = '0'
                    bot_pos = 7
                    flag = True

            # линия 123
            elif (dict_x[1] == '0' or dict_x[2] == '0' or dict_x[3] == '0') and dict_x[1] != 'X' and dict_x[2] != 'X' and dict_x[3] != 'X':
                if dict_x[1] == '0' or dict_x[2] == '0':
                    dict_x[3] = '0'
                    bot_pos = 3
                    flag = True

                else:
                    dict_x[1] = '0'
                    bot_pos = 1
                    flag = True


            # столбец 147
            elif (dict_x[1] == '0' or dict_x[4] == '0' or dict_x[7] == '0') and dict_x[1] != 'X' and dict_x[4] != 'X' and dict_x[7] != 'X':
                if (dict_x[1] == '0' or dict_x[4] == '0') and dict_x[7] == 7:
                    dict_x[7] = '0'
                    bot_pos = 7
                    flag = True

                elif dict_x[1] == 1:
                    dict_x[1] = '0'
                    bot_pos = 1
                    flag = True

                else:
                    dict_x[7] = '0'
                    bot_pos = 7
                    flag = True


            # столбец 369
            elif (dict_x[3] == '0' or dict_x[6] == '0' or dict_x[9] == '0') and dict_x[3] != 'X' and dict_x[6] != 'X' and dict_x[9] != 'X':
                if dict_x[3] == '0' or dict_x[6] == '0':
                    dict_x[9] = '0'
                    bot_pos = 9
                    flag = True

                else:
                    dict_x[3] = '0'
                    bot_pos = 3
                    flag = True


            # линия 789
            elif (dict_x[7] == '0' or dict_x[8] == '0' or dict_x[9] == '0') and dict_x[7] != 'X' and dict_x[8] != 'X' and dict_x[9] != 'X':
                if dict_x[7] == '0' or dict_x[8] == '0':
                    dict_x[9] = '0'
                    bot_pos = 9
                    flag = True

                else:
                    dict_x[7] = '0'
                    bot_pos = 7
                    flag = True


        # если не осталось возможносити выиграть занимаем первое попавшееся место:
        if not flag:
            k = 1
            while k < 10 and not flag:
                if dict_x[k] == k:
                    dict_x[k] = '0'
                    bot_pos = k
                    flag = True

                k += 1



        # после каждого шага:
        # 1 показываю поле,
        # 2 ув. счетчик
        # 3 вывожу информацию о сделанном ходе в тексте
        # 4 проверяю была ли победа
    show_X_0(dict_x)
    count +=1
    if count == 9:
        print(f'Ничья!!!!\nИгра окончена.')
        break
    print(f'шаг #{count} 0 на позицию: {bot_pos}\n')
    if event(dict_x, '0'):
            print(f'Игрок #0 выиграл!!!!\nИгра окончена.')
            break





# 3 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5 a3b4c
# 5 a3b4c -> aaaaabbbcccc

#  пакую
# input_str = 'yaabbbccccarr'
# print(input_str)
#
# count = 0
# last_letter = ''
# new_str =''
# for i in range(len(input_str)):
#     if count > 0 and input_str[0] != last_letter:
#         new_str += str(count) + last_letter
#         count = 0
#
#     count +=1
#     last_letter = input_str[0]
#     input_str = input_str[1:] + '^'
#     print(input_str,'--->' , new_str)
#
# new_str += str(count) + last_letter
# print(input_str,'--->' , new_str)

#  распаковываю
# second_str = ''
# new_str = '1y12a3b4c1a2r'
# print(new_str)
# temp_str = ''
# last_symbol = ''
# unpack_str =''
# for i in range(len(new_str)):
#     if i > 0 and last_symbol.isdigit():
#         temp_str += last_symbol
#         print(temp_str)
#     elif i > 0 and not last_symbol.isdigit():
#         unpack_str += int(temp_str) * last_symbol
#         temp_str = ''
#         print('+',unpack_str)
#
#     last_symbol = new_str[0]
#     new_str = new_str[1:] + '^'
#     print(new_str,'--->' , unpack_str)
#
# unpack_str += int(temp_str)*last_symbol
# print(unpack_str)