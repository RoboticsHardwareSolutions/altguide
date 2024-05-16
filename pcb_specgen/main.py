import os
import sys
import shutil
from docx import Document
from docxtpl import DocxTemplate
import tomli
from bom_parser import get_bom_quantity
from bom_parser import get_bom_content_like_context
from bom_parser import get_board_image
from template import template_merger
from template import template_filler
from docxtpl import InlineImage
from docx.shared import Mm
from PIL import Image


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


def get_config():
    with open('config.toml', mode="rb") as f:
        return tomli.load(f)


def gen_spec(vault, save_to):
    config = get_config()
    tables = get_bom_quantity(vault) // 25
    if get_bom_quantity(vault) % 25 != 0:
        tables += 1
    template_merger(config.get("templates"), tables)
    temp_doc = Document('template.docx')
    template_filler(temp_doc)
    doc = DocxTemplate('template1.docx')
    img = Image.open(get_board_image(vault))
    img.thumbnail(size=(600, 500))
    img.save("tmp.png")
    context = {}
    context = get_bom_content_like_context(vault)
    context["image"] = InlineImage(doc, "tmp.png")
    context["project_name"] = create_name(vault)
    doc.render(context)
    doc.save("СПЕЦИФИКАЦИЯ " + create_name(vault) + ".docx")
    os.remove(os.getcwd() + "/template.docx")
    os.remove(os.getcwd() + "/template1.docx")
    os.remove(os.getcwd() + "/tmp.png")
    try:
        os.remove(save_to + "/СПЕЦИФИКАЦИЯ.docx")
    except :
        print("")
    shutil.move(os.getcwd() + "/СПЕЦИФИКАЦИЯ " + create_name(vault) + ".docx", save_to)


def get_vault():
    arg = sys.argv[1]
    vault = (arg, arg + "/")[arg[len(arg) - 1] != "/"]
    return vault


def get_save_to():
    arg = sys.argv[2]
    save_to = (arg, arg + "/")[arg[len(arg) - 1] != "/"]
    return save_to


if __name__ == '__main__':
    print("PCB specgen запущен")
    gen_spec(get_vault(), get_save_to())
    print("Файл спецификации готов")
