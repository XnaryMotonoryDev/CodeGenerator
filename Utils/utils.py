import flet as ft

from settings import *
from Utils.menus import *

from functools import partial
from typing import List, Union

class Utils:
    def __init__(self, page: ft.Page):
        self.page = page
        self.navigate_handler = partial(self.__navigate)
        self.theme_handler = partial(self.__change_theme)
        self.generate_handler =partial(self.__generate)

    def is_empty(self, controls: List[Union[ft.Control]]) -> bool:
        for control in controls:
            if hasattr(control, 'value'):
                return control.value is None or control.value == ''
            
    def clear(self, controls: List[Union[ft.Control]]):
        for control in controls:
            if hasattr(control, 'value'):
                control.value = ''
            
    def __navigate(self, e):
        index = self.page.navigation_bar.selected_index

        self.page.clean()
        match index:
            case 0:
                self.page.add(main_menu)
                print("Your page is 0")
            case 1:
                self.page.add(settings_menu)
                print("Your page is 1")

        self.page.update()

    def __change_theme(self, e):
        self.page.theme_mode = "light" if checkbox_theme.value else "dark"
        self.page.update()

    
    def __generate(self, e):
        if self.is_empty([dropdown_type, name_type, value]):
            self.page.open(ft.SnackBar(ft.Text("Any fields is can't be empty")))
            self.page.update()
            return
        
        code = f"{dropdown_type.value} {name_type.value} = {value.value};"
        print(code)
        self.clear([dropdown_type, name_type, value])

        code_text.value = code
        self.page.update()
