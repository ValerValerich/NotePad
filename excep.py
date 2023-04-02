import csv
import logg
import ui
import datetime
import os.path
import csv_worker


def id_generator():  # генератор айдишников Готово
    new_id = 0
    if os.path.isfile("id_generator.txt") == False:
        with open("id_generator.txt", "w", encoding='utf-8') as file:
            file.write(str(new_id))
    with open("id_generator.txt", "r") as id_generator:
        new_id = id_generator.read()
        print(new_id)
    with open("id_generator.txt", "w") as id_generator:
        id_generator.write(str(int(new_id)+1))
    return new_id


def check_lenght_csv():  # Проверка, что в записной книжке есть что-то, кроме шапки Готово
    with open('data.csv', "r", encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=";")
        count = 0
        res = False
        for row in file_reader:
            count += 1
            if (len(row) > 0 and count >= 2):
                res = True
        return res


def check_to_file_be(str):
    # проверка, что файл существует. Если нет - создаем и добавляем шапку Готово
    if os.path.isfile(str) == False:
        with open("data.csv", "w", encoding='utf-8',  newline='') as file:
            file_writer = csv.writer(file, delimiter=';')
            file_writer.writerow(
                ["id", "Заголовок", "Текст заметки", "Дата", "Время"])


def check_id(x):  # Проверяет, есть ли искомый idшник в файле Готово
    res = False
    with open('data.csv', "r", newline='', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=';')
        for row in file_reader:
            if row[0] == x:
                res = True
                break
    return res


def check_date(x):  # Проверяет, есть ли искомая дата в файле Готово
    res = False
    with open('data.csv', "r", newline='', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=';')
        for row in file_reader:
            if row[3] == x:
                res = True
                break
    return res

# Проверяет валидность вводимых данных в заголовок и текст Готово


def check_in_data(some_text, meta):

    while True:
        if some_text.strip() != "":
            return some_text
        else:
            print(f"Убедитесь, что ввели корректные данные: {meta}\n")
            some_text = input(
                "Еще раз\n")
            logg.logging.error(f"Ошибка при вводе параметра {meta}")
            continue


def data_input():  # формирование данных для создание записки с проверкой валидности Готово
    id = id_generator()
    title = check_in_data(input("Заголовок:\n"), "Заголовок")
    text = check_in_data(input("Текст заметки:\n"), "Текст заметки")
    date_of_change = datetime.date.today()
    time_of_change = datetime.datetime.now().strftime("%H:%M:%S")

    return id, title, text, date_of_change, time_of_change


def data_input_edit_note():  # Формирование данных для изменения записи по id Готово
    id = input("Введите id записи, которую хотите отредактировать\n")
    if check_id(id):
        title = check_in_data(input(
            "Новый заголовок:\n"), "Новый заголовок")
        text = check_in_data(input(
            "Новый текст заметки:\n"), "Новый текст заметки")
        date_of_change = datetime.date.today()
        time_of_change = datetime.datetime.now().strftime("%H:%M:%S")
        csv_worker.change_note(id, title, text, date_of_change, time_of_change)
    else:
        print("Нет записи с таким id. Попробуйте еще раз\n")
        ui.menu()


# def input_integer(message, message_error):
#     a = None
#     while True:
#         if a is None:
#             try:
#                 a = int(input(message))
#                 break
#             except ValueError:
#                 print(message_error)
#                 continue

#     return a


def show_all():
    # показать все записи из файла
    print("\n\n")
    if check_lenght_csv():
        with open('data.csv', "r", newline='', encoding='utf-8') as file:
            rows = csv.reader(file, delimiter=";")
            for row in rows:
                print(*row, sep=" | ")
                # print(f"  {row[0]}  | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
    else:
        print("Нет записей, добавьте хотя бы одну")

    print('\n\n')
    ui.menu()


def delete_note_from_csv():  # Удаление записи по айдишнику Готово
    delete_note = input(
        'Введите id записи, которую хотите удалить:\n')
    if check_id(delete_note):
        print(f"Запись с id {delete_note} успешно удалена\n")
        csv_worker.del_note(delete_note)
        ui.menu()
    else:
        print("Такого idшника нет, попробуй еще раз\n")
        ui.menu()


def show_this_note():  # Вывод конкретной записи по айдишнику Готово
    search = input(
        "Введите id нужной записи\n")
    if check_id(search):
        print("\n\n")
        with open('data.csv', "r", newline='', encoding='utf-8') as file:
            rows = csv.reader(file, delimiter=";")
            for row in rows:
                if row[0] == "id" or row[0] == search:
                    print(*row, sep=" | ")
        print("\n\n")
        ui.menu()
    else:
        print(f"\nНет записи с id {search}, попробую еще раз\n\n")
        ui.menu()


def show_notes_for_date():  # Вывод записей за указанное число Готово
    search_date = input(
        "\nВведите дату в формате гггг-мм-чч, за которую ищите заметки\n")
    if check_date(search_date):
        print("\n\n")
        with open('data.csv', "r", newline='', encoding='utf-8') as file:
            rows = csv.reader(file, delimiter=";")
            for row in rows:
                if row[3] == "Дата" or row[3] == search_date:
                    print(*row, sep=" | ")
        print("\n\n")
        ui.menu()
    else:
        print(f"\nНет записи с датой {search_date}, попробую еще раз\n\n")
        ui.menu()
