
import sqlite3

def insert_varible_into_table(dev_id, name, email, join_date, salary):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_insert_with_param = """INSERT INTO sqlitedb_developers
                              (id, name, email, joining_date, salary)
                              VALUES (?, ?, ?, ?, ?);"""

        data_tuple = (dev_id, name, email, join_date, salary)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу sqlitedb_developers")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

insert_varible_into_table(2, 'Viktoria', 's_dom34@gmail.com', '2020-11-19', 6000)
insert_varible_into_table(3, 'Valentin', 'exp3@gmail.com', '2020-11-23', 6500)