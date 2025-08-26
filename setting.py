import flet as ft

options_type = [
    ft.DropdownOption(text="int"),
    ft.DropdownOption(text="float"),
    ft.DropdownOption(text="string"),
    ft.DropdownOption(text="bool"),
]
radius = .5
border_radius = ft.BorderRadius(radius, radius, radius, radius)
border = ft.Border(ft.BorderSide(1), ft.BorderSide(1), ft.BorderSide(1), ft.BorderSide(1))

dropdown_type = ft.Dropdown(options=options_type)
name_type = ft.TextField()
value = ft.TextField()

code_text = ft.Text("Hello")
code_container = ft.Container(content=code_text, border=border, border_radius=border_radius)