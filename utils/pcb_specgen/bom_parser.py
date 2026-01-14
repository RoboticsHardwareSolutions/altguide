import os
import csv


def make_rows(reader):
    rows = []
    skipped_count = 0
    for row in reader:
        # Пропускаем пустые строки (где все ячейки пустые)
        if row and any(cell.strip() for cell in row):
            rows.append(row)
        else:
            skipped_count += 1
    if skipped_count > 0:
        print(f"В BOM файле есть пустые строки. Они не будут учитываться при проверке.")
    return rows


def find_bom(bom_vault):
    bom_list = os.listdir(bom_vault + "doc/pcb/")
    for i in bom_list:
        if i.find("Bill of Materials") == 0 and i.find(".csv") != -1:
            return i
    return None


def find_image(bom_vault):
    image_list = os.listdir(bom_vault + "doc/photo/")
    for i in image_list:
        if i.find("top") == 0 and i.find(".png") != -1:
            return i
    return None


def get_bom_quantity(bom_vault):
    bom = bom_vault + "doc/pcb/" + find_bom(bom_vault)
    with open(bom, newline='', encoding='cp1251', ) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        rows = make_rows(reader)
    csvfile.close()
    return len(rows) - 1


def get_board_image(bom_vault):
    image = bom_vault + "doc/photo/" + find_image(bom_vault)
    return image


def get_bom_content_like_context(bom_vault):
    bom = bom_vault + "doc/pcb/" + find_bom(bom_vault)
    with open(bom, newline='', encoding='cp1251', ) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        rows = make_rows(reader)
    context = {}
    for i in range(1, get_bom_quantity(bom_vault) + 1):
        context["n" + str(i)] = i
        context["descriptions" + str(i)] = rows[i][0] + " " + rows[i][1] + " " + rows[i][3]
        context["designator" + str(i)] = rows[i][2]
        context["part" + str(i)] = rows[i][4]
        context["quan" + str(i)] = rows[i][6]
    csvfile.close()
    return context


def get_bom_vault():
    return "/Users/doc/projects/comitas/tof-sensor-hardware/"


if __name__ == '__main__':
    print(get_bom_quantity(get_bom_vault()))
    print(get_bom_content_like_context(get_bom_vault()))
