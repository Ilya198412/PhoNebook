import model, view


def main_menu():
    '''Функция по выводу меню в консоль. цикл while выводит на печать пункты меню (без привязки к функциям)  и просит на ввод 
       цифру с номером меню
       Вторая часть match case - выбранный пункт меню обрабатывается, в каждом case есть ссылка на функцию.   '''
    while True:
        print('\nГлавное меню')
        print('0. Показать все контакты') 
        print('1. Открыть файл с контактами') # - 
        print('2. Записать файл с контактами') 
        print('3. Добавить контакт')
        print('4. Изменить контакт')
        print('5. Удалить контакт')
        print('6. Поиск по контактам') # -
        print('8. Выйти из программы') 
        choiсe = int(input('Выберите пункт:'))
        match(choiсe):
            case 0:
                print('\nКонтакты телефонной книги: \n')
                open_file()
            case 1:
                open_contacts()
                print('\nФайл с контактами\n') 
            case 2:
                save_contact()
                print('\nФайл записан\n')
            case 3:
                add_contact()
                # print('\nКонтакт добавлен\n') 
                print('\n0. Для отмены сохранения контакта') # -
                print('1. Для сохранения контакта\n') # -
                # print('Для сохранения изменений в телефонной книге, нужно выбрать пункт 2 в меню.')
                choiсe1 = int(input('Выберите пункт:'))
                match(choiсe1):
                    case 1:
                        print('Контакт сохранен!\n')
                        save_contact()
                        open_contacts()
                    case 0:
                       print('Контакт не сохранен!\n') 
                       open_contacts()
            case 4:
                change_contact()
                print('\n0. Для отмены изменений контакта') # -
                print('1. Для сохранения изменений контакта\n')
                choiсe1 = int(input('Выберите пункт:'))
                match(choiсe1):
                    case 1:
                        print('Контакт изменен!\n')
                        save_contact()
                        open_contacts()
                    case 0:
                       print('Контакт не изменен!\n') 
                       open_contacts()
            case 5:
                remove_contact()
                print('\n0. Для отмены удаления контакта') # -
                print('1. Для окончательного удаления контакта\n') # -
                choiсe1 = int(input('Выберите пункт:'))
                match(choiсe1):
                    case 1:
                        print('Контакт удален!\n')
                        save_contact()
                        open_contacts()
                    case 0:
                       print('Контакт не удален!\n') 
                       open_contacts()
            case 6:
                print('Найдены совпадения : \n')
                search_contact()
                open_contacts()
            case 8:
                break
            case _:
                print("Такого пункта меню не существует: выберите от 0 до 8")

def start():
    ''' фукция запуска программы через терминал(запускается через main). используется 2 функции open_file() b через модуль view
        выводится наша телефонная книга на печать'''
    print('Телефонная книга:')
    open_file()
    # view.printPhoneBook()
    main_menu()

def open_file():
    ''' функция обращается к файлу где записана телефонная книга(book.txt) и считывает оттуда все контакты, выводит в терминал.
        в модуле model лежит переменная path-она содержит имя файла с телефонной книгой '''
    with open(model.path, "r", encoding="UTF-8") as data:
        contacts_list = data.read().split("\n")
        model.phonebook = contacts_list
        
        view.printPhoneBook()


def save_contact():
    ''' функция записи изменений в телефонную книгу. '''
    with open(model.path, "w", encoding="UTF-8") as data:
        data.write(('\n'.join(model.phonebook)))


def add_contact():
    '''функция для добавления контакта. при помощи append наш новый контакт добавляется в конец списка '''
    name = input('Введите имя ')
    surname = input('Введите фамилию ')
    last_name = input('Введите отчество ')
    number = input('Введите телефон ')
    contact = f'{name}; {surname}; {last_name}; {number};';''
    model.phonebook.append(contact)
    
    view.printPhoneBook()

def remove_contact():
    '''функция удаления контакта. pop - удаляет контакт выбранный пользователем через консоль ввода. переменная choise'''
    choice = int(input('Введите номер элемента для удаления: '))
    model.phonebook.pop(choice)
    view.printPhoneBook()

def change_contact():
    ''' функция по изменению контакта. предлагает выбрать контакт под интересующим номером, предлагает к изменению данные по отдельности (либо имя, либо фамилия и т п)'''
    choice = int(input('Введите номер элемента для изменения: '))
    choice2 = int(input('Что изменяем(0-имя 1-фамилия, 2-отчество, 3-телефон): '))
    contact = model.phonebook.pop(choice).split(';')
    print(contact)
    contact[choice2] = input()
    model.phonebook.insert(choice, ';'.join(contact))
    view.printPhoneBook()
    
def search_contact():
    '''Функция для поиска контакта, делаем двойной цикл 1й-для вытаскивания контакта целиком, 2й для разделения контакта на составляющие 
       и в них ищем совпадения. Для улучшения поиска, нужно список перевести в нижний регистр.   '''
   
    
    contact = model.phonebook
    
    search_cont=[]
    elem = input("Введите искомый элемент: ")
    for i in contact:
        if elem in i:
            search_cont.append(i)
    print(f'{search_cont}\n')
    
    view.printPhoneBook()
    

def open_contacts():
    pass

def show_contact():
    pass