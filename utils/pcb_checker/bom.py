import csv
import os


def get_column(rows, name):
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if (rows[i][j] == name):
                return i
    raise Exception("Sorry, cannot find ")


def get_row(rows, name):
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if (rows[i][j] == name):
                return j
    raise Exception("Sorry, cannot find ")


def bom_check_part(rows): # TODO бывают просто платы без компонент добавить такой вариант
    row = get_row(rows, "Part")
    designator_row = get_row(rows, "Designator")
    if len(rows) < 2:
        print(" В таблице bom не хватает данных")
        raise SystemExit(1)
    for i in range(1, len(rows)):
        if rows[i][row] == "" or rows[i][row] == " " or rows[i][row] == "M3" or rows[i][row] == "M4":
            print(f" В таблице bom есть незаполненные поля Part в элементе: {rows[i][designator_row]}")
            raise SystemExit(1)


def bom_check_description(rows):
    row = get_row(rows, "Description")
    designator_row = get_row(rows, "Designator")
    for i in range(1, len(rows)):
        if rows[i][row] == "" or rows[i][row] == " ":
            print(f" В таблице bom есть незаполненные поля Description в элементе: {rows[i][designator_row]}")
            raise SystemExit(1)


def bom_check_footprint(rows):
    row = get_row(rows, "Footprint")
    designator_row = get_row(rows, "Designator")
    for i in range(1, len(rows)):
        if rows[i][row] == "" or rows[i][row] == " ":
            print(f" В таблице bom есть незаполненные поля Footprint в элементе: {rows[i][designator_row]}")
            raise SystemExit(1)
        if rows[i][row] == "M3" or rows[i][row] == "M4" or rows[i][row] == "M5" or rows[i][row] == "M6":
            print(
                f" В таблице bom есть не исключенные компоненты вероятно это M3/M4/M5/M6 в элементе: {rows[i][designator_row]} - они не являются обьектами спецификации")
            raise SystemExit(1)


def bom_check_designator(rows):
    row = get_row(rows, "Designator")
    for i in range(1, len(rows)):
        if rows[i][row] == "" or rows[i][row] == " ":
            print(f" В таблице bom есть незаполненные поля Designator в строке {i + 1}")
            raise SystemExit(1)


def bom_check_headers(rows):
    ok = 7
    if rows[0][0] == "Description":
        ok -= 1
    if rows[0][1] == "Comment":
        ok -= 1
    if rows[0][2] == "Designator":
        ok -= 1
    if rows[0][3] == "Footprint":
        ok -= 1
    if rows[0][4] == "Part":
        ok -= 1
    if rows[0][5] == "Alternative Part":
        ok -= 1
    if rows[0][6] == "Quantity":
        ok -= 1
    if ok != 0:
        print(" В таблице с bom содержатся неверные названия заголовков столбцов")
        print(
            "Требуемые : 'Description', 'Comment', 'Designator', 'Footprint', 'Part', 'Alternative Part', 'Quantity' ")
        raise SystemExit(1)


def find_bom(bom_directory):
    bom_list = os.listdir(bom_directory)
    for i in bom_list:
        if i.find("Bill of Materials") == 0 and i.find(".csv") != -1:
            return i
    return None


def make_rows(reader):
    rows = []
    first_empty_skipped = False
    row_number = 0
    
    for row in reader:
        row_number += 1
        # Проверяем, является ли строка пустой
        is_empty = not row or not any(cell.strip() for cell in row)
        
        if is_empty:
            if not first_empty_skipped and row_number == 2:
                # Пропускаем первую пустую строку после заголовка (строка 2)
                first_empty_skipped = True
                print("Первая пустая строка после заголовка (строка 2) проигнорирована - это стандартная строка Altium")
                continue
            else:
                # Все остальные пустые строки - ошибка
                print(f"Ошибка: В BOM файле обнаружена пустая строка {row_number}. Удалите все пустые строки кроме первой после заголовка.")
                raise SystemExit(1)
        
        rows.append(row)
    
    return rows


def bom_check(bom_directory):
    bom = bom_directory + find_bom(bom_directory)
    with open(bom, newline='', encoding='cp1251', ) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        rows = make_rows(reader)
        bom_check_headers(rows)
        bom_check_part(rows)
        bom_check_description(rows)
        bom_check_designator(rows)
        bom_check_footprint(rows)
        csvfile.close()


def get_bom():
    return "/Users/doc/projects/comitas/tof-sensor-hardware/doc/pcb/"


if __name__ == '__main__':
    bom_check(get_bom())
