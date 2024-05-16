import os
import sys
import shutil


def rename(vault):
    file_list = os.listdir(vault)
    try:
        os.remove(".DS_Store")
    except:
        print("")
    print(file_list)
    for i in file_list:
        os.rename(vault + i, vault + i.lower())
    file_list = os.listdir(vault)
    print(file_list)


def get_vault():
    arg = sys.argv[1]
    vault = (arg, arg + "/")[arg[len(arg) - 1] != "/"]
    return vault


if __name__ == '__main__':
    print("low names start")
    rename(get_vault())
    print("renamed")
