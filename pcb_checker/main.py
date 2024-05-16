import sys, os
from root_check import root_folder_check
from pcbfolder import doc_pcb_folder_check
from doccheck import doc_folder_check
from gitignore import gitignore_check
from readme import readme_check
from drawing import doc_drawing_check
from photo import doc_photo_check
from pinout import doc_pinout_check
from board_option import board_option_check
from gerber import gerber_check
from bom import bom_check
from ext_bom import ext_bom_check


def get_vault():
    arg = sys.argv[1]
    vault = (arg, arg + "/")[arg[len(arg) - 1] != "/"]
    return vault


if __name__ == '__main__':
    print("PCB checker запущен")
    print("Описание требований тут :")
    print("https://gitlab.com/RoboticsHardwareSolutions/guidelines/hardware-pcb-altium-designer")
    root_folder_check(get_vault())
    gitignore_check(get_vault() + ".gitignore")
    readme_check(get_vault() + "README.md")
    doc_folder_check(get_vault() + "doc/")
    doc_pcb_folder_check(get_vault() + "doc/pcb/")
    doc_drawing_check(get_vault() + "doc/drawing/")
    doc_photo_check(get_vault() + "doc/photo/")
    doc_pinout_check(get_vault() + "doc/pinout/")
    board_option_check(get_vault() + "doc/pcb/")
    gerber_check(get_vault() + "doc/pcb/gerber/", get_vault() + "doc/pcb/")
    bom_check(get_vault() + "doc/pcb/")
    ext_bom_check(get_vault() + "doc/pcb/")
    print("Cодержимое репозитория соответствует стандартам")
