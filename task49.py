from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []


def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")


def search(all_data):
    who = input("enter name or surname: ")
    found = list(filter(lambda el: who in el or who in el == who, all_data))
    if found:
        print(*found)
    else:
        print('empty data')


def change():
    global all_data
    who = input("enter name or surname: ")
    found = list(filter(lambda el: who in el or who in el == who, all_data))
    if len(found) == 1:
        text = str(found[0]).split()
        result = ""
        if found:
            temp = input(f'Are you sure you want change number {text[0]}? enter yes/no: ')
            if temp == 'yes':
                for j in range(1, len(text)):
                    answer = input(f'do you want to change {text[j]} entry? enter yes/no: ')
                    match answer:
                        case "yes":
                            result += input(f"Enter new empty: ") + " "
                        case "no":
                            result += str(text[j]) + " "
                        case _:
                            result += str(text[j]) + " "

            all_data = list(set(all_data).difference(set(found)))
            with open(file_base, "w", encoding="utf-8") as f:
                for i in range(len(all_data)):
                    f.write(f"{all_data[i]}\n")
            with open(file_base, "a", encoding="utf-8") as f:
                f.write(f"{text[0]} {result}\n")

        else:
            print('empty data')
    else:
        print('refine search criteria')
        change()

def delete():
    global all_data
    who = input("enter name or surname: ")
    found = list(filter(lambda el: who in el or who in el == who, all_data))
    if len(found)==1:
        if found:
            temp = input('Are you sure you want delete? enter yes/no: ')
            if temp == 'yes':
                all_data = list(set(all_data).difference(set(found)))

                with open(file_base, "w", encoding="utf-8") as f:
                    for i in range(len(all_data)):
                        f.write(f"{all_data[i]}\n")
        else:
            print('empty data')
    else:
        print('refine search criteria')
        delete()


def add_new_contact():
    global last_id
    array = ["surname", "name", "patronymic", "phone_number"]
    string = ""
    for i in array:
        string += input(f"Enter {i} ") + " "
    last_id += 1

    with open(file_base, "a", encoding="utf-8") as f:
        f.write(f"{last_id} {string}\n")


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search(all_data)
            case "4":
                change()
            case "5":
                delete()
            case "6":
                pass
            case "7":
                play = False
            case _:
                print("Try again!\n")


main_menu()
