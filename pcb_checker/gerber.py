import tomli
import os
from board_option import get_board_option_dict


def check_drill(file_list, layers):
    drr = ldp = txt = False
    for i in file_list:
        if i.find(".DRR") > 0 or i.find(".drr") > 0:
            drr = True
        if i.find(".LDP") > 0 or i.find(".ldp") > 0:
            ldp = True
        if i.find(".TXT") > 0 or i.find(".txt") > 0:
            txt = True
    if not (drr and ldp and txt):
        print(" В папке doc/pcb/gerber/ найдены ошибки с файлами сверловки")
        raise SystemExit(1)


def check_cooper_layers(file_list, layers):
    top = bottom = inner1 = inner2 = inner3 = inner4 = False
    for i in file_list:
        if i.find(".GTL") > 0 or i.find(".gtl") > 0:
            top = True
        if i.find(".GBL") > 0 or i.find(".gbl") > 0:
            bottom = True
        if i.find(".G1") > 0 or i.find(".g1") > 0:
            inner1 = True
        if i.find(".G2") > 0 or i.find(".g2") > 0:
            inner2 = True
        if i.find(".G3") > 0 or i.find(".g3") > 0:
            inner3 = True
        if i.find(".G4") > 0 or i.find(".g4") > 0:
            inner4 = True
    if not (top and bottom):
        print(" В папке doc/pcb/gerber/ не найдены gerber файлы для слоев top и bottom ")
        raise SystemExit(1)
    if (layers > 2 and not (inner1 and inner2)) or (layers > 4 and not (inner3 and inner4)):
        print(" В папке doc/pcb/gerber/ не найдены gerber  для внутренних слоев платы")
        raise SystemExit(1)


def check_other_layers(file_list, layers):
    board = top_over = bot_overlay = top_solder = bot_solder = top_paste = bot_paste = apr = False
    for i in file_list:
        if i.find(".GM1") > 0 or i.find(".gm1") > 0:
            board = True
        if i.find(".GTO") > 0 or i.find(".gto") > 0:
            top_over = True
        if i.find(".GBO") > 0 or i.find(".gbo") > 0:
            bot_overlay = True
        if i.find(".GTS") > 0 or i.find(".gts") > 0:
            top_solder = True
        if i.find(".GBS") > 0 or i.find(".gbs") > 0:
            bot_solder = True
        if i.find(".GTP") > 0 or i.find(".gtp") > 0:
            top_paste = True
        if i.find(".GBP") > 0 or i.find(".gbp") > 0:
            bot_paste = True
        if i.find(".apr") > 0 or i.find(".APR") > 0:
            apr = True
    if not board or not apr:
        print(" В папке doc/pcb/gerber/ не найдены gerber файлы для Board слоя или иные файлы не найдены")
        raise SystemExit(1)
    if not (top_over and bot_overlay):
        print(" В папке doc/pcb/gerber/ не найдены gerber файлы для слоев TopOverlay или BotOverlay")
        raise SystemExit(1)
    if not (top_solder and bot_solder):
        print(" В папке doc/pcb/gerber/ не найдены gerber файлы для слоев TopSolder или BotSolder")
        raise SystemExit(1)
    if not (top_paste and bot_paste):
        print(" В папке doc/pcb/gerber/ не найдены gerber файлы для слоев TopPaste или BotPaste")
        raise SystemExit(1)


def gerber_check(gerber, board_option):
    board_option = get_board_option_dict(board_option)
    gerber_list = os.listdir(gerber)
    check_cooper_layers(gerber_list, board_option.get("layers"))
    check_other_layers(gerber_list, board_option.get("layers"))
    check_drill(gerber_list, board_option.get("layers"))
    # try:
    #     gerber_list.index("board_option_draw.png")
    # except ValueError:
    #     print("Файл doc/pcb/board_option_draw.png  отсутствует  или имеет неверное название или расширение")
    #     raise SystemExit(1)


def get_gerber():
    return "/Users/doc/projects/comitas/tof-sensor-hardware/doc/pcb/gerber"


def get_board_option_file():
    return "/Users/doc/projects/comitas/tof-sensor-hardware/doc/pcb/"


if __name__ == '__main__':
    gerber_check(get_gerber(), get_board_option_file())
