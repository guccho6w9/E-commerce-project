import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'E-commerce-project.settings')  # Asegúrate de reemplazar 'E-commerce-project.settings' con el nombre correcto del módulo de configuración de tu proyecto
django.setup()
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from app_ecommerce.models import Product, Category


# Comando para ejecutar el script
class Command(BaseCommand):
    
    help = 'Scrapes product data from Vea and prints it to the console.'

    def handle(self, *args, **options):
        # URL de la página de productos
        url = 'https://www.vea.com.ar/bebidas/gaseosa'
        
        # Hacer la solicitud HTTP
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar el contenedor de productos
        products_container = soup.find('div', class_='pr0 items-stretch vtex-flex-layout-0-x-stretchChildrenWidth flex')
        
        # Encontrar todos los productos dentro del contenedor
        products = products_container.find_all('div', class_='vtex-product-summary-2-x-container')

        # Iterar sobre cada producto
        for product in products:
            # Extraer la información del producto
            name = product.find('span', class_='vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body').text.strip()
            price_text = product.find('div', id='priceContainer').text.strip()
            price = float(price_text.replace('$', '').replace('.', '').replace(',', '.'))

            # Obtener la URL de la imagen
            image_url = product.find('img')['src']

            # Imprimir la información en consola
            print(f"Nombre: {name}")
            print(f"Precio: {price}")
            print(f"Imagen URL: {image_url}")
            print('---------------------')

            # Si quisieras guardar en la base de datos, puedes descomentar el siguiente código
            # category, created = Category.objects.get_or_create(name='Bebidas')  # Puedes ajustar la categoría según sea necesario
            # product_instance = Product(
            #     name=name,
            #     description='',  # Sin descripción
            #     price=price,
            #     image_url=f'/public/images/{name}.jpg',  # Cambia la URL de acuerdo a tu configuración
            #     category=category
            # )
            # product_instance.save()

        self.stdout.write(self.style.SUCCESS('Scraping completado y productos impresos en consola.'))

