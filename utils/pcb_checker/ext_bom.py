import csv
import os
from board_option import get_board_option_dict


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


def ext_bom_check_part(rows):
    row = get_row(rows, "Part")
    if len(rows) < 2:
        print(" В таблице bom не хватает данных")
        raise SystemExit(1)
    for i in range(1, len(rows)):
        if rows[i][row] == "" or rows[i][row] == " " or rows[i][row] == "M3" or rows[i][row] == "M4":
            print(" В таблице ext_bom есть незаполненные поля Part")
            raise SystemExit(1)


def ext_bom_check_connect_to(rows):
    row = get_row(rows, "Connect to")
    for i in range(1, len(rows)):
        if rows[i][row] == "" or rows[i][row] == " ":
            print(" В таблице ext_bom есть незаполненные поля Connect to")
            raise SystemExit(1)


def ext_bom_check_quantity(rows):
    row = get_row(rows, "Quantity")
    for i in range(1, len(rows)):
        if rows[i][row] == "" or rows[i][row] == " ":
            print(" В таблице ext_bom есть незаполненные поля Quantity")
            raise SystemExit(1)


def ext_bom_check_headers(rows):
    if len(rows[0]) < 5:
        print("В таблице ext_bom нехватет столбцов")
        raise SystemExit(1)
    ok = 5
    if rows[0][0] == "Connect to":
        ok -= 1
    if rows[0][1] == "Part":
        ok -= 1
    if rows[0][2] == "Alternative Part":
        ok -= 1
    if rows[0][3] == "Comment":
        ok -= 1
    if rows[0][4] == "Quantity":
        ok -= 1
    if ok != 0:
        print(" В таблице ext_bom.csv содержатся неверные названия заголовков столбцов")
        print(
            "Требуемые : 'Connect to', 'Part', 'Alternative Part', 'Comment', 'Quantity'")
        raise SystemExit(1)


def find_ext_bom(ext_bom_directory):
    bom_list = os.listdir(ext_bom_directory)
    for i in bom_list:
        if i.find("ext_bom") == 0 and i.find(".csv") != -1:
            return i
    return None


def make_rows(reader):
    rows = []
    for row in reader:
        rows.append(row)
    return rows


def ext_bom_check(ext_bom_directory):
    option = get_board_option_dict(ext_bom_directory)

    if option.get("ext_bom") is False:
        return

    folder_list = os.listdir(ext_bom_directory)
    try:
        folder_list.index("ext_bom.csv")
    except ValueError:
        print("Файл doc/pcb/ext_bom.csv отсутствует в репозитории")
        raise SystemExit(1)
        
    bom = ext_bom_directory + find_ext_bom(ext_bom_directory)
    with open(bom, newline='', encoding='cp1251', ) as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        rows = make_rows(reader)
        ext_bom_check_headers(rows)
        ext_bom_check_connect_to(rows)
        ext_bom_check_part(rows)
        ext_bom_check_quantity(rows)
        csvfile.close()


def get_ext_bom():
    return "/Users/doc/projects/comitas/tof-sensor-hardware/doc/pcb/"




if __name__ == '__main__':
    ext_bom_check(get_ext_bom())
