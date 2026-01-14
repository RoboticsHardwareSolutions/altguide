import sys, os
from io import StringIO
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
    print("https://roboticshardwaresolutions.github.io/altguide/")
    
    errors = []
    
    # Запускаем все проверки и собираем ошибки
    checks = [
        ("root_folder_check", lambda: root_folder_check(get_vault())),
        ("gitignore_check", lambda: gitignore_check(get_vault() + ".gitignore")),
        ("readme_check", lambda: readme_check(get_vault() + "README.md")),
        ("doc_folder_check", lambda: doc_folder_check(get_vault() + "doc/")),
        ("doc_pcb_folder_check", lambda: doc_pcb_folder_check(get_vault() + "doc/pcb/")),
        ("doc_drawing_check", lambda: doc_drawing_check(get_vault() + "doc/drawing/")),
        ("doc_photo_check", lambda: doc_photo_check(get_vault() + "doc/photo/")),
        ("doc_pinout_check", lambda: doc_pinout_check(get_vault() + "doc/pinout/")),
        ("board_option_check", lambda: board_option_check(get_vault() + "doc/pcb/")),
        ("gerber_check", lambda: gerber_check(get_vault() + "doc/pcb/gerber/", get_vault() + "doc/pcb/")),
        ("bom_check", lambda: bom_check(get_vault() + "doc/pcb/")),
        ("ext_bom_check", lambda: ext_bom_check(get_vault() + "doc/pcb/")),
    ]
    
    for check_name, check_func in checks:
        try:
            # Перехватываем вывод
            old_stdout = sys.stdout
            sys.stdout = StringIO()
            
            check_func()
            
            # Получаем вывод
            output = sys.stdout.getvalue()
            sys.stdout = old_stdout
            
            # Если есть вывод, показываем его
            if output.strip():
                print(output.strip())
                
        except SystemExit:
            # Получаем сообщение об ошибке и восстанавливаем stdout
            output = sys.stdout.getvalue()
            sys.stdout = old_stdout
            if output.strip():
                errors.append(output.strip())
        except Exception as e:
            sys.stdout = old_stdout
            errors.append(f"Ошибка в {check_name}: {str(e)}")
    
    # Выводим результат
    if errors:
        print("\n" + "="*50)
        print("НАЙДЕНЫ ОШИБКИ:")
        print("="*50)
        for error in errors:
            print(error)
        print("="*50)
        sys.exit(1)
    else:
        print("Cодержимое репозитория соответствует стандартам")
