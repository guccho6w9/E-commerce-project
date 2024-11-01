import flet as ft
import requests
from paginaPrincipal import pagina_principal_view  # Importar la vista principal

API_URL = "http://localhost:8000/api"  # Asegúrate de que coincida con tu configuración

def login_view(page):
    def login_user(e):
        user_data = {
            "email": email_user.value,
            "password": password_user.value,
        }
        
        try:
            response = requests.post(f"{API_URL}/login/", json=user_data)
            response.raise_for_status()  # Lanza un error para respuestas de error HTTP
            print("Respuesta del servidor:", response.text)
            
            user_info = response.json()  # Suponiendo que recibes la información del usuario
            user_name = user_info.get("name", "Usuario")
            full_name = user_info.get("full_name", "Usuario Desconocido")  # Si tienes otro campo
            print(user_name,  user_info)

            # Almacenar el nombre del usuario en el objeto page
            page.user_name = user_name
            
            # Redirigir a la vista principal con el nombre del usuario
            page.views.clear()  # Limpiar vistas anteriores
            page.views.append(pagina_principal_view(page, user_name))  # Agregar la vista principal
            page.go("/main")  # Redirigir a la ruta principal (puedes cambiarla si es necesario)

        except requests.exceptions.HTTPError as http_err:
            print("Error al iniciar sesión:", response.json().get("detail", "Error desconocido"))
            status_text.value = f"Error al iniciar sesión: {response.json().get('detail', 'Error desconocido')} (HTTP {http_err.response.status_code})"
            page.update()
        except requests.exceptions.RequestException as req_err:
            print("Error de conexión:", req_err)
            status_text.value = "Error de conexión. Por favor, intenta nuevamente."
            page.update()

    email_user = ft.TextField(label="Correo electrónico", width=400)
    password_user = ft.TextField(label="Contraseña", password=True, width=400)
    login_button = ft.ElevatedButton("Iniciar sesión", on_click=login_user)

    # Mensaje de estado
    status_text = ft.Text("")

    # Botón para ir a la vista de registro
    register_button = ft.TextButton("Registrarse", on_click=lambda _: page.go("/register"))

    return ft.View(
        "/",
        [
            email_user,
            password_user,
            login_button,
            status_text,  # Agregado para mostrar mensajes de estado
            register_button
        ],
    )
