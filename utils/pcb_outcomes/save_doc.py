import os
import zipfile
import shutil


def save_doc(vault, name, save_to):
    shutil.make_archive(save_to+ name, "zip", vault + "doc/pcb/")


def get_vault():
    return "/Users/doc/projects/comitas/tof-sensor-hardware/"


def get_save_to():
    return "/Users/doc/Desktop/"


if __name__ == '__main__':
    save_doc(get_vault(), "Файлы для заказа с монтажом", get_save_to())
