import os


def files_list_checker_hardware(root_list):
    try:
        root_list.index("hardware")
    except ValueError:
        print("Папка /hardware отсутствует в корне репозитория")
        raise SystemExit(1)


def files_list_checker_readme(root_list):
    try:
        root_list.index("README.md")
    except ValueError:
        print("Файл с описанием README.md отсутствует в корне репозитория")
        raise SystemExit(1)


def files_list_checker_ignore(root_list):
    try:
        root_list.index(".gitignore")
    except ValueError:
        print("Файл .gitignore с шаблонами игнорирования отсутствует  в корне репозитория")
        raise SystemExit(1)


def files_list_checker_doc(root_list):
    try:
        root_list.index("doc")
    except ValueError:
        print("Папка /doc c документацией отсутствует в корне репозитория")
        raise SystemExit(1)


def delete_if_found(root_list, name):
    try:
        index = root_list.index(name)
    except ValueError:
        index = None
    if index is not None:
        root_list.remove(name)


def files_list_checker_trash(root_list):
    root_list.remove("doc")
    root_list.remove(".gitignore")
    root_list.remove(".github")
    root_list.remove("README.md")
    root_list.remove("hardware")
    # root_list.remove('.gitlab-ci.yml')
    delete_if_found(root_list, '.git')
    delete_if_found(root_list, '.DS_Store')
    delete_if_found(root_list, 'simulation')
    delete_if_found(root_list, '.gitlab-ci.yml')
    delete_if_found(root_list, '.gitmodules')
    delete_if_found(root_list, 'software')
    delete_if_found(root_list, "firmware")
    if len(root_list) != 0:
        print("В корне репозитория содержится 'мусор' :")
        print(root_list)
        raise SystemExit(1)


def root_folder_check(vault):
    list = os.listdir(vault)
    files_list_checker_hardware(list)
    files_list_checker_readme(list)
    files_list_checker_ignore(list)
    files_list_checker_doc(list)
    files_list_checker_trash(list)


def get_vault_test():
    return "/Users/doc/projects/comitas/tof-sensor-hardware/"


if __name__ == '__main__':
    root_folder_check(get_vault_test())
