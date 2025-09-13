import flet as ft

from settings import *

settings_menu = ft.Row([
    checkbox_theme
], ft.MainAxisAlignment.CENTER)

main_menu = ft.Column([
    ft.Row([dropdown_type, name_type, value], ft.MainAxisAlignment.CENTER),
    ft.Row([btn_g], ft.MainAxisAlignment.CENTER),
    ft.Row([code_container], ft.MainAxisAlignment.CENTER)
])