import logging
from time import sleep
import file_picker
import flet as ft
from flet import (
    Column,
    FloatingActionButton,
    Icon,
    NavigationRail,
    NavigationRailDestination,
    Page,
    Row,
    Text,
    VerticalDivider,
    icons,
)


# logging.basicConfig(level=logging.DEBUG)


def main(page: Page):


    pages = [
        check_page,
        outcomes_page,
        specgen_page,
    ]

    def select_page():
        print(f"Selected index: {rail.selected_index}")
        for index, p in enumerate(pages):
            p.visible = True if index == rail.selected_index else False
        page.update()

    def dest_change(e):
        select_page()

    rail = NavigationRail(
        selected_index=0,
        label_type="all",
        # extended=True,
        min_width=100,
        min_extended_width=400,
        destinations=[
            NavigationRailDestination(icon=icons.SETTINGS_ETHERNET_ROUNDED, label="PCB checker"),
            NavigationRailDestination(icon=icons.DEVICE_HUB_OUTLINED, label="PCB outcomes"),
            NavigationRailDestination(icon=icons.CLEANING_SERVICES_ROUNDED, label="PCB specgen"),
        ],
        on_change=dest_change,
    )

    select_page()

    page.add(
        Row(
            [
                rail,
                VerticalDivider(width=1),
                Column(pages, alignment="start", expand=True),
            ],
            expand=True,
        )
    )


ft.app(target=main)
