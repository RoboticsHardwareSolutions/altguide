import os


def docfolder_pinout_check(doc_list):
    try:
        doc_list.index("pinout")
    except ValueError:
        print("Папка doc/pinout отсутствует в репозитории")
        raise SystemExit(1)


def docfolder_photo_check(doc_list):
    try:
        doc_list.index("photo")
    except ValueError:
        print("Папка doc/photo отсутствует в репозитории")
        raise SystemExit(1)


def docfolder_pcb_check(doc_list):
    try:
        doc_list.index("pcb")
    except ValueError:
        print("Папка doc/pcb отсутствует в репозитории")
        raise SystemExit(1)


def docfolder_drawings_check(doc_list):
    try:
        doc_list.index("drawing")
    except ValueError:
        print("Папка doc/drawing отсутствует в репозитории")
        raise SystemExit(1)


def deletedoc_if_found(doc_list, name):
    try:
        index = doc_list.index(name)
    except ValueError:
        index = None
    if index is not None:
        doc_list.remove(name)


def doc_list_checker_trash(doc_list):
    doc_list.remove("pcb")
    doc_list.remove("drawing")
    doc_list.remove("pinout")
    doc_list.remove("photo")
    deletedoc_if_found(doc_list, '.DS_Store')
    if len(doc_list) != 0:
        print("В папке /doc  репозитория содержится 'мусор' :")
        print(doc_list)
        raise SystemExit(1)


def doc_folder_check(doc):
    doc_list = os.listdir(doc)
    docfolder_drawings_check(doc_list)
    docfolder_pcb_check(doc_list)
    docfolder_photo_check(doc_list)
    docfolder_pinout_check(doc_list)
    doc_list_checker_trash(doc_list)


def get_vault_test_doc():
    return "/Users/doc/projects/comitas/tof-sensor-hardware/doc/"


if __name__ == '__main__':
    doc_folder_check(get_vault_test_doc())
