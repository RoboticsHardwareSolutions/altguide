import flet as ft
from flet import icons
from flet import

import time


def file_picker_view(result_choice):
    def on_dialog_result(e: ft.FilePickerResultEvent):
        print("Selected files:", e.files)
        print("Selected file or directory:", e.path)

    return ft.Row(
        [picker = ft.FilePicker(on_result=result_choice),
    ft.ElevatedButton("Choose vault folder...",
                      icon=icons.FOLDER_OPEN,
                      on_click=lambda _: file_picker.get_directory_path())
    ]
    )

    # ft.app(target=main)
