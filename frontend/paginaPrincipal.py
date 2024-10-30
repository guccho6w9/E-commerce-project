import flet as ft

def pagina_principal_view(page, user_name):
    # Contenedor para el mensaje de bienvenida
    welcome_message = ft.Text(f"Bienvenido {user_name}", style="headlineMedium")

    # Función para manejar el cierre de sesión
    def logout():
        page.user_name = None  # Limpiar el nombre de usuario
        page.go("/")  # Redirigir a la vista de inicio de sesión

    # Botón de cerrar sesión
    logout_button = ft.ElevatedButton(text="Cerrar sesión", on_click=lambda e: logout())

    # Diseño de la vista principal
    return ft.View(
        "/main",  # Asegúrate de que esta ruta coincida con la lógica en main.py
        [
            ft.Container(
                content=welcome_message,
                alignment=ft.alignment.center,
                height=500,  # Altura del contenedor
                bgcolor=ft.colors.LIGHT_BLUE_50,  # Fondo suave
                padding=20
            ),
            # Agregar el botón de cerrar sesión debajo del mensaje de bienvenida
            ft.Container(
                content=logout_button,
                alignment=ft.alignment.center,
                margin=20  # Añadir un margen
            )
        ],
    )
