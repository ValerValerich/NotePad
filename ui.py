from logg import logging
import excep
import csv_worker


def menu():
    logging.info("Запуск приложения")
    type_num = input("Выберите вариант работы с базой\n"
                     "1 - Добавить заметку\n"
                     "2 - Изменить заметку\n"
                     "3 - Удалить заметку\n"
                     "4 - Найти заметку\n"
                     "5 - Заметки за число\n"
                     "6 - Показать всё\n"
                     "7 - Выход\n")
    
    excep.check_to_file_be("data.csv") # проверяем, есть ли файл. Если нет, создаем с названием столбцов

    match type_num:
        case "1":
            logging.info("Добавление записи") # Готово
            print("Добавляем запись")
            id, title, text, date, time = excep.data_input()
            csv_worker.add(id, title, text, date, time)
           
        case "2":
            logging.info("Изменяем данные") # Готово
            print("Изменяем данные")
            excep.data_input_edit_note()
            
        case "3":
            logging.info("Удаление записи") # Готово
            excep.delete_note_from_csv()

        case "4":
            logging.info("Показать заметку по id") # Готово
            excep.show_this_note()

        case "5":
            logging.info("Вывод заметок за число")
            excep.show_notes_for_date()
        case "6":
            logging.info("Вывод всех записаей") # Готово
            excep.show_all()

        case "7":
            logging.info("Выход")
            print("\n\nДо встречи!\n\n")
            
        case _:
            logging.error("Некорректный выбор режима")
            print("\n\nНекорректный выбор режима\n")
            menu()
