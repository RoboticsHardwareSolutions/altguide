
import os


def gitignore_check(gitignore):
    file = open(gitignore, 'r')
    count = file.readlines()
    if len(count) < 11:
        print(
            "Файл  .gitignore в корне репозитория  пуст или содержит недостаточное количество шаблонов игнорирования")
        print(
            "Пример тут https://gitlab.com/RoboticsHardwareSolutions/guidelines/hardware-pcb-altium-designer/-/blob/main/files/.gitignore")
        raise SystemExit(1)
    file.close()


def get_gitignore():
    return "/Users/doc/projects/comitas/tof-sensor-hardware/.gitignore"


if __name__ == '__main__':
    gitignore_check(get_gitignore())
