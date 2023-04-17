# №8.1[49]. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
# Информация о человеке:
# Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека.
# Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе
# Усложнение.
# - Сделать тесты для функций
# - Разделить на model-view-controller

# fio = {'Иванов Иван': ['897097', 'работник'], 'Петров Петр': ['35346', 'не работник']}

# fio = {'Иванов Иван': ['897097', 'работник']}, {'Петров Петр': ['35346', 'не работник']} # список словарей

# fio = [{1: ["Иванов", "Иван","89234145", "работник"]}]
fio = [{1: {'Surname': "Иванов", 'Name': "Иван", 'Number':"89234145", 'Discrip': "работник"}}] #список словарей
# fio = [{'Surname': "Иванов", 'Name': "Иван", 'Number':"89234145", 'Discrip': "работник"}]

phonebook = {}
phonebook_last_id = 0

def create (db: dict, id:int, surname: str, name:str, number:str, discrip:str) -> dict: #data_base    
    db[id] = {"Surname": surname, "Name": name, "Phone": number, "Discrip": discrip}
    id += 1
    return db, id

def read (db: dict, surname_filter: str)-> int: #выдает список ключей
    for _id in db:
        if surname_filter.lower() in db[_id]['Surname'].lower():
            return _id

def delete(db: dict) -> None:
    recs = read(db, get_surname())
    # print(recs)
    if recs:
        db.pop(recs)
    
def update(db: dict)-> str:
    recs = read(db, get_surname())
    print()        
    print("Искомый контакт: ")
    print_record(db, recs)
    record = get_user_data()
    db, recs = create(db, recs, *record)


def print_record(db:dict, _id:int)-> str:
    # альтернативный вариант записи отладки
    # if _id is not None:
    #     print(f'{db[_id]}\n')
    # else:
    #     print(f'{"="*30}\n Запись не найдена!')
    print(f'{db[_id]}\n')

def get_user_data() -> dict:
    # surname: str, name: str, phone: str, discrip: str
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    discrip = input("Введите описание: ")
    return surname, name, phone, discrip

def print_data(db: dict)-> None:
    for id, data in db.items():
        print(f"[{id}: {data['Surname']} | {data['Name']} | {data['Phone']} | {data['Discrip']}]")

def get_surname()-> str:
    surname = input('Введите искомую фамилию: ')
    return surname


# 3) экспорт данных в текстовый файл формата csv
def export_db(db:dict, filepath: str,  delimeter: str = '#') -> None:
    filepath
    with open (filepath, "w", encoding='utf-8') as file:
        for _id, data in db.items():
            file.write(f"{data['Surname']}{delimeter}{data['Name']}{delimeter}{data['Phone']}{delimeter}{data['Discrip']} \n")

def get_file_name() -> str:
    return input("Введите имя файла: ")


# 4) импорт данных из текстового файла формата csv
def import_db(db:dict, last_id:int, filepath: str, delimeter: str = '#') -> tuple:
    # last_id = 0
    with open(filepath, "r", encoding= 'utf-8') as file:
        for line in file:
            _data = line.strip().split(delimeter)
            db[last_id] = {"Surname": _data[0], "Name": _data[1], "Phone": _data[2], "Discrip": _data[3]}
            last_id +=1
    return db, last_id


def menu(db: dict, last_id: int)-> int:
    while True:
        print("Возможные действие: ")
        print("1. Создать запись")
        print("2. Вывести имеющиеся данные: ")
        print("3. Экспортировать данные в файл: ")
        print("4. Импортировать данные из файла")
        print("5. Найти пользователя: ")
        print("6. Изменение пользователя")
        print("7. Удаление пользователя")
        print("8. Выход")

        user_input = input("Введите действие > ")
        if user_input == "1":
            record = get_user_data()
            db, last_id = create(db, last_id, *record)
        elif user_input == "2":
            print_data(db)
        elif user_input == "3":
            export_db(db, get_file_name())
        elif user_input == "4":
            # db, last_id = import_db(db, last_id, get_file_name())
            db, last_id = import_db(db, last_id, 'data3.txt')
        elif user_input == "5":
            found_id = read(db, get_surname()) 
            try:            #в данный код помещается только тот код, который может выдать ошибку
                print_record(db, found_id)
            except KeyError:
                print(f'{"="*30}\n Запись не найдена!\n{"="*30}')
        elif user_input == "6":
            update(db)
        elif user_input == "7":
            delete(db)
        else:
            break
        
menu(phonebook, phonebook_last_id)
