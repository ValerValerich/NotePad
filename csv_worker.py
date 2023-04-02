import csv
import ui
import os





def add(id, title, text, date, time): # Добавление записи в csv Готово
    with open("data.csv", "a", encoding='utf-8',  newline='') as file:
        file_add = csv.writer(file, delimiter=';')
        file_add.writerow([id, title, text, date, time])
    ui.menu()

def del_note(id): # Удаление записи по id Готово
    with open('data.csv', 'r', encoding='utf-8',  newline='') as inp, open('data2.csv', 'a', encoding='utf-8',  newline='') as out:
        writer = csv.writer(out, delimiter=';')
        for row in csv.reader(inp, delimiter=';'):
            if row[0] != str(id):
                writer.writerow(row)
    os.remove("data.csv")
    os.rename("data2.csv", "data.csv")

def change_note(id, title, text, date_change, time_change): # Изменение записи в csv по айдишнику через создание нового файла, удаления старого и переименования нового в старый Готово
    with open('data.csv', 'r', encoding='utf-8',  newline='') as inp, open('data2.csv', 'a', encoding='utf-8',  newline='') as out:
        writer = csv.writer(out, delimiter=';')
        for row in csv.reader(inp, delimiter=';'):
            if row[0] != str(id):
                writer.writerow(row)
            else:
                writer.writerow([id, title, text, date_change, time_change])
    os.remove("data.csv")
    os.rename("data2.csv", "data.csv")
    ui.menu()