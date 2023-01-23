import view
import model
def start():
    choice = ''
    while choice != 8:
        choice = view.main_menu()
        match choice:
            case '1':
                model.open_file()
                view.message_opened()
            case '2':
                model.safe_file()
                view.message_safed()
            case '3':
                view.show_contacts(model.get_phone_book())
            case '4':
                new_contact = list(view.create_new_contact())
                model.add_new_contact(new_contact)
                view.message_added(new_contact)
            case '5':
                deleted_str = view.delete_contact()
                result = model.delete_contact(deleted_str)
                view.message_deleted()
            case '6':
                global new_change
                result = view.what_are_going_to_change_dear()
                finding_item = model.search_contact(result[0])
                view.show_contacts(finding_item)
                how_many = model.how_many_contacts(result[0])
                if how_many == 0:
                    view.message_found_nothig()
                    view.main_menu()
                elif how_many == 1:
                    model.change_contact(result)
                    view.message_changed()
                elif how_many > 1:
                    view.message_too_much()
                    view.main_menu()

            case '7':
                find = view.find_contact()
                result = model.search_contact(find)
                view.show_contacts(result)
            case _:
                if choice == '8':
                    break
                else:
                    view.input_error()