import os
import sys
from bom_parser import save_fill_to
from bom_parser import save_empty_for_pcb
import shutil


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


def gen_outcomes(vault, spec_folder, save_to):
    # Изготовление PCB
    dir_pcb = save_to + "PCB Изготовление " + create_name(vault) + "/"
    os.mkdir(dir_pcb)
    shutil.make_archive(dir_pcb + "Aрхив для заказа " + create_name(vault), "zip", vault + "doc/pcb/")
    for file_name in os.listdir(spec_folder):
        source = spec_folder + file_name
        destination = dir_pcb + file_name
        if os.path.isfile(source):
            shutil.copy(source, destination)
    save_empty_for_pcb(vault, os.getcwd() + "/template/1c_template.csv", dir_pcb + " Импортировать в 1С.csv")

    # Комплектующие PCB
    dir_pcb = save_to + "PCB Комплектующие " + create_name(vault) + "/"
    os.mkdir(dir_pcb)
    for file_name in os.listdir(spec_folder):
        source = spec_folder + file_name
        destination = dir_pcb + file_name
        if os.path.isfile(source):
            shutil.copy(source, destination)
    save_fill_to(vault, os.getcwd() + "/template/1c_template.csv", dir_pcb + " Импортировать в 1С.csv")

    # PCB с монтажом
    dir_pcb = save_to + "PCB c монтажом " + create_name(vault) + "/"
    os.mkdir(dir_pcb)
    shutil.make_archive(dir_pcb + "Aрхив для заказа " + create_name(vault), "zip", vault + "doc/pcb/")
    for file_name in os.listdir(spec_folder):
        source = spec_folder + file_name
        destination = dir_pcb + file_name
        if os.path.isfile(source):
            shutil.copy(source, destination)
    save_empty_for_pcb(vault, os.getcwd() + "/template/1c_template.csv", dir_pcb + " Импортировать в 1С.csv")


def get_vault():
    arg = sys.argv[1]
    vault = (arg, arg + "/")[arg[len(arg) - 1] != "/"]
    return vault


def get_save_to():
    arg = sys.argv[3]
    save_to = (arg, arg + "/")[arg[len(arg) - 1] != "/"]
    return save_to


def get_spec_folder():
    arg = sys.argv[2]
    save_to = (arg, arg + "/")[arg[len(arg) - 1] != "/"]
    return save_to


if __name__ == '__main__':
    print("PCB outcomes запущен")
    gen_outcomes(get_vault(), get_spec_folder(), get_save_to())
    print("Архивы для публикации готовы")
