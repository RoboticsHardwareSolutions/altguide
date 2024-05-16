import os


def delete_if_found(drawing_list, name):
    try:
        index = drawing_list.index(name)
    except ValueError:
        index = None
    if index is not None:
        drawing_list.remove(name)


def doc_drawing_check(drawing):
    found = False
    drawing_list = os.listdir(drawing)
    delete_if_found(drawing_list, '.DS_Store')
    for i in drawing_list:
        if i.find(".step") > 1 or i.find(".STEP") > 1 or i.find(".STP") > 1 or i.find(".stp"):
            found = True
            break
    if not found or len(drawing_list) > 1:
        print("В папке /doc/drawing/  репозитория содержится 'мусор' или нужный файл 3d модели платы отсутствует ")
        raise SystemExit(1)


def get_vault_test_drawing():
    return "/Users/doc/projects/comitas/tof-sensor-hardware/doc/drawing"


if __name__ == '__main__':
    doc_drawing_check(get_vault_test_drawing())
