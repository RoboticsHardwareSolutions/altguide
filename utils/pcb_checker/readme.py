import os


def check_standart_prj_name(file):
    file = open(file, 'r')
    for line in file.readlines():
        if line.find("ENTER YOUR PROJECT NAME HERE") != -1:
            print("В файлe  README.md не задано имя проекта ")
            raise SystemExit(1)
    file.close()


def check_len(file):
    file = open(file, 'r')
    count = file.readlines()
    if len(count) < 11:
        file.close()
        print(
            "Файл README.md в корне репозитория  пуст или содержит недостаточное описание ")
        print(
            "Пример тут https://gitlab.com/RoboticsHardwareSolutions/guidelines/hardware-pcb-altium-designer/-/blob/main/files/README.md")
        raise SystemExit(1)
    file.close()


def check_standart_gitlab(file):
    file = open(file, 'r')
    for line in file.readlines():
        if line.find("Getting started") != -1:
            print("Файл  README.md наиболее вероятно содержит стандартное описание взятое с gitlab ")
            raise SystemExit(1)
    file.close()


def readme_check(readme):
    check_len(readme)
    check_standart_gitlab(readme)
    check_standart_prj_name(readme)


def get_readme():
    return "/Users/doc/projects/comitas/tof-sensor-hardware/README.md"


if __name__ == '__main__':
    readme_check(get_readme())
