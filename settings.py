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
name_type = ft.TextField(hint_text="Enter the name")
value = ft.TextField(hint_text="Enter the value")
btn_g = ft.Button(text="Generate")

code_text = ft.Text()
code_container = ft.Container(content=code_text, border=border, border_radius=border_radius)

nav_bar = ft.NavigationBar([
    ft.NavigationBarDestination(label='Home', icon=ft.Icons.HOME),
    ft.NavigationBarDestination(label='Settings', icon=ft.Icons.SETTINGS)
])
checkbox_theme = ft.Checkbox(label="Change theme")