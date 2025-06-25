import os

def pcbdoc_delete_if_found(doc_list, name):
    try:
        index = doc_list.index(name)
    except ValueError:
        index = None
    if index is not None:
        doc_list.remove(name)


def pcb_list_checker_trash(pcb_list):
    pcbdoc_delete_if_found(pcb_list, 'board_options_draw.png')
    pcbdoc_delete_if_found(pcb_list, '.DS_Store')
    pcbdoc_delete_if_found(pcb_list, 'Status Report.Txt')
    pcbdoc_delete_if_found(pcb_list, "ext_bom.csv")
    if len(pcb_list) != 0:
        print("В папке /doc/pcb/  репозитория содержится 'мусор' :")
        print(pcb_list)
        raise SystemExit(1)


def pcb_folder_board_options(pcb_list):
    try:
        pcb_list.index("board_options.txt")
        pcb_list.remove("board_options.txt")
    except ValueError:
        print("Файл board_options.txt отсутствует в /doc/pcb/ ")
        raise SystemExit(1)


def pcb_folder_pick_place(pcb_list):
    for i in pcb_list:
        if i.find("Pick Place") == 0 and i.find(".csv") != -1:
            pcb_list.remove(i)
            return
    print("Файл  Pick Place xxxxxx.csv в /doc/pcb/  не найден или имеет не верное расширение")
    raise SystemExit(1)


def pcb_folder_bom(pcb_list):
    for i in pcb_list:
        if i.find("Bill of Materials") == 0 and i.find(".csv") != -1:
            pcb_list.remove(i)
            return
    print("Файл  Bill of Materials xxxxxx.csv в /doc/pcb/ не найден или имеет не верное расширение")
    raise SystemExit(1)


def pcb_folder_gerber(pcb_list):
    try:
        pcb_list.index("gerber")
        pcb_list.remove("gerber")
    except ValueError:
        print("Папка gerber отсутствует в /doc/pcb/gerber/ ")
        raise SystemExit(1)


def pcb_folder_schematic_prints(pcb_list):
    try:
        pcb_list.index("Schematic Prints.PDF")
        pcb_list.remove("Schematic Prints.PDF")
    except ValueError:
        print("Файл Schematic Prints.PDF отсутствует в /doc/pcb/ ")
        raise SystemExit(1)


def pcb_folder_assembly_drawings(pcb_list):
    try:
        pcb_list.index("Assembly Drawings.PDF")
        pcb_list.remove("Assembly Drawings.PDF")
    except ValueError:
        print("Файл Assembly Drawings.PDF отсутствует в /doc/pcb/ ")
        raise SystemExit(1)
    

def pcb_folder_draftsman(pcb_list):
    try:
        pcb_list.index("Draftsman.PDF")
        pcb_list.remove("Draftsman.PDF")
    except ValueError:
        print("Файл Draftsman.PDF отсутствует в /doc/pcb/ ")
        # raise SystemExit(1)


def doc_pcb_folder_check(doc_pcb):
    doc_pcb = os.listdir(doc_pcb)
    pcb_folder_assembly_drawings(doc_pcb)
    pcb_folder_schematic_prints(doc_pcb)
    pcb_folder_gerber(doc_pcb)
    pcb_folder_bom(doc_pcb)
    pcb_folder_pick_place(doc_pcb)
    pcb_folder_board_options(doc_pcb)
    pcb_folder_draftsman(doc_pcb)
    pcb_list_checker_trash(doc_pcb)


def get_vault_test_pcb():
    return "/Users/doc/projects/comitas/tof-sensor-hardware/doc/pcb/"


if __name__ == '__main__':
    doc_pcb_folder_check(get_vault_test_pcb())
