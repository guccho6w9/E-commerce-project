import flet as ft 
import requests

API_URL=""

async def main(page: ft.Page):
    page.padding = 0
    page.margin = 0
    page.title = "Login Acceder"
    
    def revisa_user(e):
        user_data = {
            "name": name_user.value,
            "password": password_user.value,
        }
        response = requests.post(API_URL, json=user_data)
        if response.status_code == 200:
            pass
            #Hay que hacer aca la comparacion primero ver que exista el usuario y si existe comparar las contraseñas
        else:
            print("Error al crear registro", response.text)
    
    #Campos de entrada
    name_user = ft.TextField(label="Nombre del usuario", border_radius=20, width=800)
    password_user = ft.TextField(label="Contraseña", border_radius=20, width=800)
    
    #Boton para crear el registro
    create_button = ft.ElevatedButton("ACCEDER", on_click=revisa_user)
    
    
    #Se crea un contenedor que tendra todos los elementos centrales
    item_center = [
        ft.Container(width=50), #Margen izquierdos
        ft.Container(name_user, alignment=ft.alignment.center),
        ft.Container(width=30), #Margen derecho
        ft.Container(password_user, alignment=ft.alignment.center),
        ft.Container(create_button, margin= ft.margin.only(top=20),alignment=ft.alignment.bottom_center)
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