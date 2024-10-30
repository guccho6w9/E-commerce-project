import flet as ft
import requests
import re

API_URL = "http://127.0.0.1:8000/register"

def register_view(page):
    def is_valid_email(email):
        pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        return re.match(pattern, email)

    def create_user(e):
        if not is_valid_email(email_user.value):
            status_text.value = "El email no tiene un formato válido"
            page.update()
            return
        
        if password_user.value != password_confir_user.value:
            status_text.value = "Las contraseñas no coinciden"
            page.update()
            return

        user_data = {
            "name": name_user.value,
            "email": email_user.value,
            "password": password_user.value,
        }

        response = requests.post(API_URL, json=user_data)
        
        if response.status_code == 200:
            status_text.value = f"Registro exitoso. Usuario: {user_data['name']}"
            page.update()
            page.go("/")
        else:
            status_text.value = f"Error: {response.json().get('detail', 'No se pudo registrar el usuario')}"
            page.update()

    # Campos de entrada
    name_user = ft.TextField(label="Nombre del usuario", border_radius=20, width=800)
    email_user = ft.TextField(label="Email", border_radius=20, width=800)
    password_user = ft.TextField(label="Contraseña", border_radius=20, width=395, password=True)
    password_confir_user = ft.TextField(label="Confirmar contraseña", border_radius=20, width=395, password=True)
    
    # Botón para crear el registro
    create_button = ft.ElevatedButton("REGISTRARSE", on_click=create_user)
    
    # Mensaje de estado
    status_text = ft.Text("")
    
    # Fila de contraseñas
    password_row = ft.Row(
        controls=[
            ft.Container(password_user, alignment=ft.alignment.center),
            ft.Container(password_confir_user, alignment=ft.alignment.center)
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Botón para regresar a login
    back_button = ft.TextButton("¿Ya tienes cuenta? Iniciar sesión", on_click=lambda _: page.go("/"))

    # Diseño centralizado y agrupado
    item_center = [
        ft.Container(name_user, margin=ft.margin.only(left=10, right=10), alignment=ft.alignment.center),
        ft.Container(email_user, margin=ft.margin.only(left=10, right=10, bottom=10), alignment=ft.alignment.center),
        password_row,
        ft.Container(create_button, margin=ft.margin.only(top=20), alignment=ft.alignment.bottom_center),
        status_text,
        back_button
    ]
    
    # Secciones de la vista
    superior = ft.Container(height=80)
    centro = ft.Container(content=ft.Column(item_center), height=500, alignment=ft.alignment.center)
    inferior = ft.Container(height=80)
    
    # Contenedor principal
    col = ft.Column(spacing=0, controls=[superior, centro, inferior])
    contenedor = ft.Container(col, bgcolor=ft.colors.WHITE, alignment=ft.alignment.top_center)
    
    # Devolver la vista con el contenedor centralizado
    return ft.View(
        "/register",
        [contenedor],
    )
