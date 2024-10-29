import flet as ft 
import requests

API_URL=""

async def main(page: ft.Page):
    page.padding = 0
    page.margin = 0
    page.title = "Login Registro"
    
    def create_user(e):
        user_data = {
            "name": name_user.value,
            "description": email_user.value,
            "password": password_user.value,
            "confirm": password_confir_user,
        }
        response = requests.post(API_URL, json=user_data)
        if response.status_code == 200:
            #Hay que ver que el email no tenga otro usuario, si el emal no esta usado se hace el registro
            print("Registro Exitoso")
        else:
            print("Error al crear registro", response.text)
    
    #Campos de entrada
    name_user = ft.TextField(label="Nombre del usuario", border_radius=20, width=800)
    email_user = ft.TextField(label="Email", border_radius=20, width=800)
    password_user = ft.TextField(label="Contraseña", border_radius=20, width=395)
    password_confir_user = ft.TextField(label="Confirmar contraseña", border_radius=20, width=395)
    
    #Boton para crear el registro
    create_button = ft.ElevatedButton("REGISTRARSE", on_click=create_user)
    
    # Agrupando las contraseñas en una fila centrada
    password_row = ft.Row(
        controls=[
            ft.Container(password_user, alignment=ft.alignment.center),
            ft.Container(password_confir_user, alignment=ft.alignment.center)
        ],
        alignment=ft.MainAxisAlignment.CENTER  # Centra la fila horizontalmente
    )
    
    # Se crea un contenedor que tendrá todos los elementos centrales
    item_center = [
        ft.Container(width=50),  # Margen izquierdo
        ft.Container(name_user, margin=ft.margin.only(left=10, right=10), alignment=ft.alignment.center),
        ft.Container(width=30),  # Margen derecho
        ft.Container(email_user, margin=ft.margin.only(left=10, right=10, bottom=10), alignment=ft.alignment.center),
        password_row,  # Añadimos la fila de contraseñas centrada
        ft.Container(create_button, margin=ft.margin.only(top=20), alignment=ft.alignment.bottom_center)
    ]
    
    #Se crean el footer, center y 
    superior = ft.Container(height=80, margin = ft.margin.only(top=0))
    centro = ft.Container(content=ft.Column(item_center),height=500, margin = ft.margin.only(top=10), alignment=ft.alignment.center)
    inferior = ft.Container(height=80, margin = ft.margin.only(top=10))
    
    #Contenedor que contiene todo
    col = ft.Column(spacing=0, controls=[
        superior,
        centro,
        inferior,
    ])
    
    #Contenedor padre
    contenedor = ft.Container(col, bgcolor=ft.colors.WHITE, alignment=ft.alignment.top_center)
    
    await page.add_async(contenedor)
    
ft.app(target=main)