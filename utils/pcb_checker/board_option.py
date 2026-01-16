import tomli
import os


def check_board_option_draw(options):
    options_list = os.listdir(options.replace("board_options.txt", ''))
    try:
        options_list.index("board_options_draw.png")
    except ValueError:
        print("Файл doc/pcb/board_options_draw.png  отсутствует  или имеет неверное название или расширение")
        raise SystemExit(1)


def board_option_check(options):
    options += "board_options.txt"
    with open(options, "rb") as file:
        try:
            toml_dict = tomli.load(file)
        except tomli.TOMLDecodeError:
            print("Ошибка в составления файла board_options.txt")
            raise SystemExit(1)
    board_opt = toml_dict.get("board_options")
    if board_opt is None:
        print("В файле остуствует строка [board_options]  или содержит ошибки ")
        raise SystemExit(1)
    board_length = board_opt.get("length")
    if board_length is None or not isinstance(board_length, (int, float)):
        print("Поле 'length' отсутсвует или содержит неверное значение (ожидается число)")
        raise SystemExit(1)
    board_width = board_opt.get("width")
    if board_width is None or not isinstance(board_width, (int, float)):
        print("Поле 'width' отсутсвует или содержит неверное значение (ожидается число)")
        raise SystemExit(1)
    board_type = board_opt.get("type")
    if board_type is None or not ((board_type == "typical") or (board_type == "custom")):
        print("Поле 'type' отсутсвует или содердит ошибки (возможные варианты значений 'typical' и 'custom' )")
        raise SystemExit(1)
    board_layers = board_opt.get("layers")
    if board_layers is None:
        print("Поле 'layers' отсутсвует или содердит ошибки ")
        raise SystemExit(1)
    if not (board_layers == 2 or board_layers == 4 or board_layers == 6 or board_layers == 8):
        print("Поле 'layers'  содержит ошибки ")
        raise SystemExit(1)
    if board_layers > 4 and board_type != "custom":
        print(
            "Плата больше 4х слоев должна иметь тип 'custom' а также должна быть приложена послойная структура"
            " печатной платы в файле pcb/doc/board_options_draw.png "
        )
        raise SystemExit(1)
    if board_layers > 4 or board_type == 'custom':
        check_board_option_draw(options)
    surface_finish = board_opt.get("surface_finish")
    if surface_finish is None:
        print("Поле 'surface_finish' отсутсвует ")
        print(
            "Подробней тут https://www.rezonit.ru/directory/v-pomoshch-konstruktoru/kharakteristiki-finishnykh-pokrytiy/")
        raise SystemExit(1)
    pcb_color = board_opt.get('pcb_color')
    if pcb_color is None or not (
            pcb_color == "black" or pcb_color == "green" or pcb_color == "blue" or pcb_color == "red"):
        print("Поле 'pcb_color' отсутсвует или содержит неверное значение   ")
        print("Возможные варианты 'black' / 'green' / 'blue' / 'red' ")
        raise SystemExit(1)
    overlay_color = board_opt.get('overlay_color')
    if overlay_color is None or not overlay_color == 'white':
        print("Поле 'overlay_color' отсутсвует или содержит неверное значение   ")
        print("Возможные варианты 'white'")
        raise SystemExit(1)
    pcb_thickness = board_opt.get('pcb_thickness')
    if pcb_thickness is None or not (
            pcb_thickness == 1.5 or pcb_thickness == 0.8 or pcb_thickness == 2 or pcb_thickness == 1):
        print("Поле 'pcb_thickness' отсутсвует или содержит неверное значение   ")
        print("Возможные варианты 0.8 / 1 / 1.5 / 2 ")
        raise SystemExit(1)
    cooper_thickness = board_opt.get('cooper_thickness')
    if cooper_thickness is None or not (
            cooper_thickness == 18 or cooper_thickness == 35 or cooper_thickness == 70 or cooper_thickness == 105):
        print("Поле 'cooper_thickness' отсутсвует или содержит неверное значение   ")
        print("Возможные варианты 18 / 35 / 70 / 105 ")
        raise SystemExit(1)
    solder_point = board_opt.get("solder_point")
    if solder_point is None or (solder_point < 1 or solder_point > 4000):
        print("Поле 'solder_point' отсутсвует или содержит неверное значение   ")
        raise SystemExit(1)
    ext_bom = board_opt.get("ext_bom")
    if ext_bom is None:
        print("Поле 'ext_bom' отсутсвует или содержит неверное значение")
        raise SystemExit(1)
    ext_bom = board_opt.get("length")
    if ext_bom is None:
        print("Поле 'length' отсутсвует или содержит неверное значение")
        raise SystemExit(1)
    ext_bom = board_opt.get("width")
    if ext_bom is None:
        print("Поле 'width' отсутсвует или содержит неверное значение")
        raise SystemExit(1)
    drill_file_check = board_opt.get("drill_file_check")
    if drill_file_check is not None:  # делает существование этого поля в файле необязательным
        if not isinstance(drill_file_check, bool):
            print("Поле 'drill_file_check' содержит неверное значение (ожидается 'true' или 'false')")
            raise SystemExit(1)
    file.close()


def get_board_option_dict(options):
    options += "board_options.txt"
    with open(options, "rb") as file:
        try:
            toml_dict = tomli.load(file)
        except tomli.TOMLDecodeError:
            print("Ошибка в составления файла board_options.txt")
            raise SystemExit(1)
    return toml_dict.get("board_options")


def get_board_options():
    return "/Users/doc/projects/comitas/tof-sensor-hardware/doc/pcb/"


if __name__ == '__main__':
    board_option_check(get_board_options())
