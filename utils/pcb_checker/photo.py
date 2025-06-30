import os


def photo_list_checker_doc(photo_list):
    try:
        photo_list.index("top.png")
        photo_list.index("bot.png")
    except ValueError:
        print(
            "В папке /doc/photo/  отсутствует изображения top.png и/или bot.png или задано неверное имя или расширение")
        raise SystemExit(1)


def delete_photo_if_found(drawing_list, name):
    try:
        index = drawing_list.index(name)
    except ValueError:
        index = None
    if index is not None:
        drawing_list.remove(name)


def photo_list_checker_trash(photo_list):
    delete_photo_if_found(photo_list, '.DS_Store')
    delete_photo_if_found(photo_list, 'Status Report.Txt')
    photo_list.remove("top.png")
    photo_list.remove("bot.png")
    if len(photo_list) != 0:
        print("В папке /doc/photo/ репозитория содержится 'мусор' :")
        print(photo_list)
        raise SystemExit(1)


def doc_photo_check(photo):
    photo_list = os.listdir(photo)
    delete_photo_if_found(photo_list, '.DS_Store')
    photo_list_checker_doc(photo_list)
    photo_list_checker_trash(photo_list)

def get_vault_test_photo():
    return "/Users/doc/projects/comitas/tof-sensor-hardware/doc/photo/"


if __name__ == '__main__':
    doc_photo_check(get_vault_test_photo())
