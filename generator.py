import flet as ft

from settings import *
from Utils.utils import Utils
from Utils.menus import main_menu

def app(page: ft.Page):
    page.theme_mode = 'dark'
    page.title = "code generator"
    page.navigation_bar = nav_bar

    util = Utils(page)

    nav_bar.on_change = util.navigate_handler
    checkbox_theme.on_change = util.theme_handler
    btn_g.on_click = util.generate_handler

    page.add(main_menu)


ft.app(target=app)