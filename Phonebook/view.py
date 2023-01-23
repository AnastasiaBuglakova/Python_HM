commands = ['Открыть файл',
            'Сохранить файл',
            'Показать все контакты',
            'Создать контакт',
            'Удалить контакт',
            'Изменить контакты',
            'Найти контакт',
            'Выход из программы']

def main_menu() -> int:
    print('Главное меню:')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}.{item}')
    choice = (input('Выберите пункт меню:'))
    return choice


def show_contacts(phone_list: list):
    if len(phone_list) < 1:
        print('Телефонная книга пуста или не открыта')
    else:
        for i,contact in enumerate(phone_list, 1):
            print(f'\t{i}.{contact[0]:27}\t {contact[1]:13}\t{contact[2]:20}\n')


def input_error():
    print('Ошибка ввода. Введите, пожалуйста, номер пункта меню от 1 до 8:')

def create_new_contact():
    name = input("Введите имя и фамилию: ")
    phone = input("Введите телефон: ")
    comment = input("Введите комментарий: ")
    return name, phone, comment
def what_are_going_to_change_dear():
    new_change = []
    new_change.append(input("Введите контакт, который необходимо изменить:"))
    pos = ''
    while pos != '1' and pos != '2' and pos != '3':
        pos = input("Введите 1 - если надо поменять имя, 2 - номер, 3 - комментарий:")
    new_change.append(pos)
    new_change.append(input("Введите, пожалуйста, новое значение:"))
    return new_change
def delete_contact():
    deleted_str = input('Введите контакт, который желаете удалить:')
def find_contact():
    find = input('Введите искомый элемент:')
    return find
def message_deleted(result):
    print(f'Контакт {result} был удален')

def message_changed():
    print('Контакт был изменен')

def message_added(new_contact):
    print(f'Контакт {new_contact} был добавлен')

def message_safed():
    print('Телефонный справочник сохранен')

def message_opened():
    print('Телефонный справочник открыт')

def message_found_nothig():
    print('Такого элемента в справочнике не найдено, уточните поиск, пожалуйста')

def message_too_much():
    print('С таким значением найдено несколько контактов, уточните запрос, пожалуйста')
