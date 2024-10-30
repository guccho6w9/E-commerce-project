import flet as ft
from registro import register_view
from login import login_view
from paginaPrincipal import pagina_principal_view  # Importar la vista principal

async def main(page: ft.Page):
    page.title = "App de Registro y Login"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Inicializar el nombre de usuario en la página
    page.user_name = "Usuario"  # Valor por defecto

    # Función de manejo de rutas
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(login_view(page))
        elif page.route == "/register":
            page.views.append(register_view(page))
        elif page.route == "/main":  # Manejo de la ruta principal
            page.views.append(pagina_principal_view(page, page.user_name))  # Usar el atributo user_name
        page.update()

    page.on_route_change = route_change
    page.go("/")  # Ruta inicial (login)

ft.app(target=main)
