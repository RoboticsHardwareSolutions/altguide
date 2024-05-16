import os


def pinout_list_checker_doc(pinout_list):
    try:
        pinout_list.index("pinout.png")
    except ValueError:
        print(
            "В папке /doc/pinout/  отсутствует  созданный в "
            "Draw.io файл pinout.png  или задано неверное имя или расширение")
        raise SystemExit(1)


def delete_pinout_if_found(pinout_list, name):
    try:
        index = pinout_list.index(name)
    except ValueError:
        index = None
    if index is not None:
        pinout_list.remove(name)


def pinout_list_checker_trash(pinout_list):
    delete_pinout_if_found(pinout_list, '.DS_Store')
    pinout_list.remove("pinout.png")
    if len(pinout_list) != 0:
        print("В папке /doc/pinout/ репозитория содержится 'мусор' :")
        print(pinout_list)
        raise SystemExit(1)


def doc_pinout_check(photo):
    photo_list = os.listdir(photo)
    delete_pinout_if_found(photo_list, '.DS_Store')
    pinout_list_checker_doc(photo_list)
    pinout_list_checker_trash(photo_list)


def get_vault_test_pinout():
    return "/Users/doc/projects/comitas/tof-sensor-hardware/doc/pinout/"


if __name__ == '__main__':
    doc_pinout_check(get_vault_test_pinout())
