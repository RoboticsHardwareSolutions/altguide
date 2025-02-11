import os
import shutil
import csv


def make_rows(reader):
    rows = []
    for row in reader:
        rows.append(row)
    return rows


def get_row(rows, name):
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if (rows[i][j] == name):
                return j
    raise Exception("Sorry, cannot find ")


def create_template(name, save_to):
    shutil.copyfile(os.getcwd() + "/template/1c_template.csv", save_to + "1c_template.csv")
    os.rename(save_to + "1c_template.csv", save_to + name)
    return


def template_get_column_by_name(file, name_column):
    with open(file, newline='', encoding='UTF-8', ) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        rows = make_rows(reader)
        csvfile.close()
    return get_row(rows, name_column)


def get_name():
    return "Импортировать в 1C.csv"


def get_save_to():
    return "/Users/doc/Desktop/"


if __name__ == '__main__':
    create_template(get_name(), get_save_to())
    print(template_get_column_by_name(get_save_to() + get_name(), "Артикул"))
