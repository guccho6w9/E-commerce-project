import flet as ft

def main(page: ft.Page):
    page.title = "Mi E-commerce"
    page.add(
        ft.Text("¡Bienvenido a mi tienda!")
    )

ft.app(target=main)