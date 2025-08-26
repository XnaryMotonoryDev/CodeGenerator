import flet as ft

from setting import *


def app(page: ft.Page):
    page.theme_mode = 'dark'
    page.title = "code generator"

    def generate(e):
        code = f"{dropdown_type.value} {name_type.value} = {value.value}"

        code_text.value = code
        page.update()

    btn_g = ft.Button(text="Generate", on_click=generate)

    page.add(ft.Row(
        [
            dropdown_type,
            name_type,
            value
        ], alignment=ft.MainAxisAlignment.CENTER
    ))

    page.add(ft.Row(
        [
            btn_g
        ], alignment=ft.MainAxisAlignment.CENTER
    ))

    page.add(ft.Row(
        [
            code_container
        ], alignment=ft.MainAxisAlignment.CENTER
    ))


ft.app(target=app)