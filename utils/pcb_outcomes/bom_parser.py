import os
import csv
from template import template_get_column_by_name
from template import create_template


def make_rows(reader):
    rows = []
    for row in reader:
        rows.append(row)
    return rows


def find_bom(bom_vault):
    bom_list = os.listdir(bom_vault + "doc/pcb/")
    for i in bom_list:
        if i.find("Bill of Materials") == 0 and i.find(".csv") != -1:
            return i
    return None


def get_bom_quantity(bom_vault):
    bom = bom_vault + "doc/pcb/" + find_bom(bom_vault)
    with open(bom, newline='', encoding='cp1251', ) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        rows = make_rows(reader)
    csvfile.close()
    return len(rows) - 1


def create_name(vault):
    index = None
    for i in range(2, len(vault)):
        if vault[i * -1] == "/" and i != 0:
            index = len(vault) + (i * -1)
            break
    if index is not None:
        last_index = (len(vault) - 1, len(vault) - 2)[vault[len(vault) - 1] != "/"]
        name = vault[index + 1: last_index]
        name = name.replace("_", " ")
        name = name.replace("-", " ")
        name = name.upper()
        return name
    return None


def get_bom_content_like_rows(bom_vault, template_file):
    bom = bom_vault + "doc/pcb/" + find_bom(bom_vault)
    with open(bom, newline='', encoding='cp1251', ) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        bom_row = make_rows(reader)
    num = template_get_column_by_name(template_file, 'N')
    code = template_get_column_by_name(template_file, 'Код')
    article = template_get_column_by_name(template_file, 'Артикул')
    description = template_get_column_by_name(template_file, 'Описание')
    manufacturing = template_get_column_by_name(template_file, 'Производитель')
    nomenclature = template_get_column_by_name(template_file, 'Номенклатура')
    nomenclature_new = template_get_column_by_name(template_file, 'Номенклатура новая текстом')
    spec_num = template_get_column_by_name(template_file, 'Поз. по спецификации')
    character = template_get_column_by_name(template_file, 'Характеристика')
    quantity = template_get_column_by_name(template_file, 'Количество')
    value_type = template_get_column_by_name(template_file, 'Ед.изм.')
    order_type = template_get_column_by_name(template_file, 'Тип заявки')
    plan_price_one = template_get_column_by_name(template_file, 'Планируемая стоимость, за ед.')
    common_price = template_get_column_by_name(template_file, 'Общая планируемая стоимость')
    currency = template_get_column_by_name(template_file, 'Валюта')
    price = template_get_column_by_name(template_file, 'Стоимость, руб.')
    agent = template_get_column_by_name(template_file, 'Контрагент')
    cancel_reason = template_get_column_by_name(template_file, 'Отменено по причине')
    on_warehouse = template_get_column_by_name(template_file, 'Доступно на складе')
    warehouse = template_get_column_by_name(template_file, 'Склад')
    price_serial = template_get_column_by_name(template_file, 'Стоимость  10/100/1000')
    order_supplier = template_get_column_by_name(template_file, 'Заказы поставщику')
    good_time = template_get_column_by_name(template_file, 'Дата получений прогноз')
    link = template_get_column_by_name(template_file, 'Ссылка')
    target_supplier = template_get_column_by_name(template_file, 'Предлагаемый поставщик')
    status = template_get_column_by_name(template_file, 'Статус')

    # "N","Код","Артикул","Описание","Производитель","Номенклатура","Номенклатура новая текстом","Поз. по спецификации",
    # "Характеристика","Количество","Ед.изм.","Тип заявки","Планируемая стоимость, за ед.","Общая планируемая стоимость"
    # "Валюта","Стоимость, руб.","Контрагент ","Отменено по причине","Доступно на складе","Склад",
    # "Стоимость  10/100/1000","Заказы поставщику","Дата получений прогноз","Ссылка","Предлагаемый поставщик","Статус"
    gen = [[0 for x in range(26)] for y in range(get_bom_quantity(bom_vault))]
    for el in range(1, get_bom_quantity(bom_vault) + 1):
        gen[el - 1][num] = str(el)
        gen[el - 1][code] = ""
        gen[el - 1][article] = bom_row[el][4]
        gen[el - 1][description] = bom_row[el][0] + " " + bom_row[el][1] + " " + bom_row[el][3]
        gen[el - 1][manufacturing] = ""
        gen[el - 1][nomenclature] = ""
        gen[el - 1][nomenclature_new] = ""
        gen[el - 1][spec_num] = "поз " + str(el)
        gen[el - 1][character] = ""
        gen[el - 1][quantity] = bom_row[el][6]
        gen[el - 1][value_type] = ""
        gen[el - 1][order_type] = "PCB Комплектующие"
        gen[el - 1][plan_price_one] = ""
        gen[el - 1][common_price] = ""
        gen[el - 1][currency] = ""
        gen[el - 1][price] = ""
        gen[el - 1][agent] = ""
        gen[el - 1][cancel_reason] = ""
        gen[el - 1][on_warehouse] = ""
        gen[el - 1][warehouse] = ""
        gen[el - 1][price_serial] = ""
        gen[el - 1][order_supplier] = ""
        gen[el - 1][good_time] = ""
        gen[el - 1][link] = ""
        gen[el - 1][target_supplier] = ""
        gen[el - 1][status] = ""
    csvfile.close()
    return gen


def save_fill_to(vault, template_file, save_to):
    f = open(save_to, 'w')
    writer = csv.writer(f)
    rows = get_bom_content_like_rows(vault, template_file)
    for i in range(0, get_bom_quantity(vault)):
        writer.writerow(rows[i])
    f.close()


def save_empty_for_pcb(vault, template_file, save_to):
    f = open(save_to, 'w')
    writer = csv.writer(f)
    num = template_get_column_by_name(template_file, 'N')
    code = template_get_column_by_name(template_file, 'Код')
    article = template_get_column_by_name(template_file, 'Артикул')
    description = template_get_column_by_name(template_file, 'Описание')
    manufacturing = template_get_column_by_name(template_file, 'Производитель')
    nomenclature = template_get_column_by_name(template_file, 'Номенклатура')
    nomenclature_new = template_get_column_by_name(template_file, 'Номенклатура новая текстом')
    spec_num = template_get_column_by_name(template_file, 'Поз. по спецификации')
    character = template_get_column_by_name(template_file, 'Характеристика')
    quantity = template_get_column_by_name(template_file, 'Количество')
    value_type = template_get_column_by_name(template_file, 'Ед.изм.')
    order_type = template_get_column_by_name(template_file, 'Тип заявки')
    plan_price_one = template_get_column_by_name(template_file, 'Планируемая стоимость, за ед.')
    common_price = template_get_column_by_name(template_file, 'Общая планируемая стоимость')
    currency = template_get_column_by_name(template_file, 'Валюта')
    price = template_get_column_by_name(template_file, 'Стоимость, руб.')
    agent = template_get_column_by_name(template_file, 'Контрагент')
    cancel_reason = template_get_column_by_name(template_file, 'Отменено по причине')
    on_warehouse = template_get_column_by_name(template_file, 'Доступно на складе')
    warehouse = template_get_column_by_name(template_file, 'Склад')
    price_serial = template_get_column_by_name(template_file, 'Стоимость  10/100/1000')
    order_supplier = template_get_column_by_name(template_file, 'Заказы поставщику')
    good_time = template_get_column_by_name(template_file, 'Дата получений прогноз')
    link = template_get_column_by_name(template_file, 'Ссылка')
    target_supplier = template_get_column_by_name(template_file, 'Предлагаемый поставщик')
    status = template_get_column_by_name(template_file, 'Статус')
    gen = [[0 for x in range(26)] for y in range(1)]
    gen[0][num] = "1"
    gen[0][code] = ""
    gen[0][article] = create_name(vault)  # TODO https://rm.comitas.ru/issues/644
    gen[0][description] = ""
    gen[0][manufacturing] = "Comitas"
    gen[0][nomenclature] = ""
    gen[0][nomenclature_new] = ""
    gen[0][spec_num] = "Gerber Файлы"
    gen[0][character] = ""
    gen[0][quantity] = ""
    gen[0][value_type] = ""
    gen[0][order_type] = "PCB Изготовление "
    gen[0][plan_price_one] = ""
    gen[0][common_price] = ""
    gen[0][currency] = ""
    gen[0][price] = ""
    gen[0][agent] = ""
    gen[0][cancel_reason] = ""
    gen[0][on_warehouse] = ""
    gen[0][warehouse] = ""
    gen[0][price_serial] = ""
    gen[0][order_supplier] = ""
    gen[0][good_time] = ""
    gen[0][link] = ""
    gen[0][target_supplier] = ""
    gen[0][status] = ""
    writer.writerow(gen[0])
    f.close()


def save_empty_for_place(vault, template_file, save_to):
    f = open(save_to, 'w')
    writer = csv.writer(f)
    num = template_get_column_by_name(template_file, 'N')
    code = template_get_column_by_name(template_file, 'Код')
    article = template_get_column_by_name(template_file, 'Артикул')
    description = template_get_column_by_name(template_file, 'Описание')
    manufacturing = template_get_column_by_name(template_file, 'Производитель')
    nomenclature = template_get_column_by_name(template_file, 'Номенклатура')
    nomenclature_new = template_get_column_by_name(template_file, 'Номенклатура новая текстом')
    spec_num = template_get_column_by_name(template_file, 'Поз. по спецификации')
    character = template_get_column_by_name(template_file, 'Характеристика')
    quantity = template_get_column_by_name(template_file, 'Количество')
    value_type = template_get_column_by_name(template_file, 'Ед.изм.')
    order_type = template_get_column_by_name(template_file, 'Тип заявки')
    plan_price_one = template_get_column_by_name(template_file, 'Планируемая стоимость, за ед.')
    common_price = template_get_column_by_name(template_file, 'Общая планируемая стоимость')
    currency = template_get_column_by_name(template_file, 'Валюта')
    price = template_get_column_by_name(template_file, 'Стоимость, руб.')
    agent = template_get_column_by_name(template_file, 'Контрагент')
    cancel_reason = template_get_column_by_name(template_file, 'Отменено по причине')
    on_warehouse = template_get_column_by_name(template_file, 'Доступно на складе')
    warehouse = template_get_column_by_name(template_file, 'Склад')
    price_serial = template_get_column_by_name(template_file, 'Стоимость  10/100/1000')
    order_supplier = template_get_column_by_name(template_file, 'Заказы поставщику')
    good_time = template_get_column_by_name(template_file, 'Дата получений прогноз')
    link = template_get_column_by_name(template_file, 'Ссылка')
    target_supplier = template_get_column_by_name(template_file, 'Предлагаемый поставщик')
    status = template_get_column_by_name(template_file, 'Статус')
    gen = [[0 for x in range(26)] for y in range(1)]
    gen[0][num] = "1"
    gen[0][code] = ""
    gen[0][article] = create_name(vault)  # TODO https://rm.comitas.ru/issues/644
    gen[0][description] = ""
    gen[0][manufacturing] = "Comitas"
    gen[0][nomenclature] = ""
    gen[0][nomenclature_new] = ""
    gen[0][spec_num] = "Gerber Файлы"
    gen[0][character] = ""
    gen[0][quantity] = ""
    gen[0][value_type] = ""
    gen[0][order_type] = "PCB c монтажом"
    gen[0][plan_price_one] = ""
    gen[0][common_price] = ""
    gen[0][currency] = ""
    gen[0][price] = ""
    gen[0][agent] = ""
    gen[0][cancel_reason] = ""
    gen[0][on_warehouse] = ""
    gen[0][warehouse] = ""
    gen[0][price_serial] = ""
    gen[0][order_supplier] = ""
    gen[0][good_time] = ""
    gen[0][link] = ""
    gen[0][target_supplier] = ""
    gen[0][status] = ""
    writer.writerow(gen[0])
    f.close()


def get_vault():
    return "/Users/doc/projects/comitas/battery_2p12s_right/"


def get_template():
    return "/Users/doc/Desktop/Импортировать в 1C.csv"


if __name__ == '__main__':
    print(get_bom_quantity(get_vault()))
    print('--------------------------------------------------------------------------------------------------------')
    bom = get_bom_content_like_rows(get_vault(), get_template())
    for i in range(0, get_bom_quantity(get_vault())):
        print(bom[i])
