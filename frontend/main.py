import flet as ft
import requests

API_URL = "http://127.0.0.1:8000/products/"  # URL del backend para crear productos

def main(page: ft.Page):
    page.title = "E-commerce Product Manager"

    # Función para enviar datos al backend
    def create_product(e):
        product_data = {
            "name": name_field.value,
            "description": desc_field.value,
            "price": float(price_field.value),
            "image_url": image_url_field.value,
        }
        response = requests.post(API_URL, json=product_data)
        if response.status_code == 200:
            product = response.json()
            product_list.controls.append(ft.Text(f"{product['name']} - ${product['price']}"))
            page.update()
            name_field.value = ""
            desc_field.value = ""
            price_field.value = ""
            image_url_field.value = ""
        else:
            print("Error al crear el producto:", response.text)

    # Campos de entrada
    name_field = ft.TextField(label="Nombre del producto")
    desc_field = ft.TextField(label="Descripción")
    price_field = ft.TextField(label="Precio")
    image_url_field = ft.TextField(label="URL de la imagen (opcional)")

    # Botón para crear el producto
    create_button = ft.ElevatedButton("Crear producto", on_click=create_product)

    # Lista para mostrar productos
    product_list = ft.Column()

    # Agrega todos los elementos a la página
    page.add(
        ft.Column([
            name_field,
            desc_field,
            price_field,
            image_url_field,
            create_button,
            ft.Text("Productos creados:"),
            product_list
        ])
    )

ft.app(target=main)
