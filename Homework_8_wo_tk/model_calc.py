def parse(first_list):
    parsed_list = first_list.replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/',
                                                                                                               '  / ').split()
    return parsed_list

def bracket_fun(any_str):
    any_list = any_str.split(')')

    any_list = any_list[0].split('(')
    return ''.join((any_list[len(any_list)-1]))
def arifmitic(entered_list):

    i = 0
    while i < len(entered_list):
        if entered_list[i] == '*':
            if entered_list[i+1] == '-':
                entered_list[i+1] = str(entered_list[i+1]) + str(entered_list[i+2])
                del entered_list[i+2]
            entered_list[i - 1] = float(entered_list[i - 1]) * float(entered_list[i + 1])
            del entered_list[i]
            del entered_list[i]
        i += 1

    i = 0
    while i < len(entered_list):
        if entered_list[i] == '/':
            if entered_list[i+1] == '-':
                entered_list[i+1] = str(entered_list[i+1]) + str(entered_list[i+2])
                del entered_list[i+2]
            entered_list[i - 1] = float(entered_list[i - 1]) / float(entered_list[i + 1])
            del entered_list[i]
            del entered_list[i]
        i += 1


    i = 0
    if entered_list[0] == '-':
        entered_list[0] = str(entered_list[0]) + str(entered_list[1])
        del entered_list[1]
    while '-' in entered_list and i < len(entered_list):
        if entered_list[i] == '-' and entered_list[i+1] == '-':
            entered_list[i] = '+'
            del entered_list[i+1]
        if entered_list[i] == '-' and entered_list[i+1] == '+':
            del entered_list[i + 1]
        if entered_list[i] == '-' and entered_list[i - 1] == '+':
            del entered_list[i - 1]
        if entered_list[i] == '-':
            entered_list[i - 1] = float(entered_list[i - 1]) - float(entered_list[i + 1])
            del entered_list[i]
            del entered_list[i]
            i=0
        i += 1

    i = 0
    if entered_list[0] == '+':
        del entered_list[0]
    while i < len(entered_list):
        if entered_list[i] == '+':
            entered_list[i - 1] = float(entered_list[i - 1]) + float(entered_list[i + 1])
            del entered_list[i]
            del entered_list[i]
        i += 1
    return (entered_list[0])