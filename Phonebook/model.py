phone_book = []
path = 'phone_book.txt'

def get_phone_book():
    global phone_book
    return phone_book
def open_file():
    global phone_book
    global path
    with open(path, 'r', encoding = 'UTF-8') as data:
        file = data.readlines()
    for contact in file:
        global phone_book
        phone_book.append(contact.strip().split(';'))


def safe_file():
    global phone_book
    global path
    pb_str = []
    for contact in phone_book:
        pb_str.append(';'.join(contact))
    with open(path, 'w', encoding = 'UTF-8') as data:
        data.write('\n'.join(pb_str))

def add_new_contact(new_contact: list):
    global phone_book
    phone_book.append(new_contact)

def search_contact(find: str):
    global phone_book
    result = []
    for contact in phone_book:
        for field in contact:
            if find in field:
                result.append(contact)
                break
    return result

def delete_contact(deleted_str: str):
    global phone_book
    result = []
    for contact in phone_book:
        for field in contact:
            phone_book.remove(contact)
            break
    return result
def change_contact(change):
    global phone_book
    for i in range(len(phone_book)):
        for j in range(len(phone_book[i])):
            if change[0] in phone_book[i][j]:
                if change[1] == '1':
                    phone_book[i][0] = change[2]
                if change[1] == '2':
                    phone_book[i][1] = change[2]
                if change[1] == '3':
                    phone_book[i][2] = change[2]

def how_many_contacts(find: str):
    global phone_book
    result = []
    count = 0
    for contact in phone_book:
        for field in contact:
            if find in field:
                count += 1

    return count



