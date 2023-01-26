from tkinter import *
def launch():
    line = input('Введите, пожалуйста, выражение:')
    flag = False
    if '+' in line or '-' in line or '*' in line or '/' in line: flag = True
    if not flag:
        while flag:
            line = input('Введите выражение с использованием арифметических символов (+,-,*,/):')
    return line
def bracket(any_line: str):

    any_list =[]
    for i in range(len(any_line)):
        any_list.append(any_line[i])

    count1 = 0
    count2 = 0
    for i in range(len(any_list)):
        if any_list[i] == '(':
            count1 += 1
        if any_list[i] == ')':
            count2 += 1

    for k in range(len(any_list)//2):
        pos2 = 0
        pos1 = 0
        for i in range(len(any_list)):
            if any_list[i] == ')':
                pos2 = i
                any_list[i] = '-'
                break
        for i in range(0, pos2):
            if any_list[i] == '(':
                pos1 = i
        any_list[pos1] = '+'

    if count1 != count2:
        line = input('Введите выражение с равным количеством открывающих и закрывающих скобок:')
        # s_root = Tk()
        # lab = Label(width=20, bg='black', fg='white')
        # lab['text'] = 'Введите выражение с равным количеством открывающих и закрывающих скобок:'
        # s_root.mainloop()
        return line
    else:
        return any_line

def div_by_zero(list_before_arifmtic: list):
    for i in range(len(list_before_arifmtic)):
        if list_before_arifmtic[i] == '/' and list_before_arifmtic[i+1] == '0':
            return True

def error_warning(number: int):
    errors_list = ['Данное выражение не может быть вычислено, деление на ноль не возможно.\nВведите, пожалуйста, другое выражение.', '', '']
    print(errors_list[number])


def show_result(res):
    print(res)
    print(round(float(''.join(res)), 2))



