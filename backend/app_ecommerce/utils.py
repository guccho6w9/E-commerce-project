# import os
# import json
# import requests
# from bs4 import BeautifulSoup

# Ruta donde guardar las imágenes
# IMAGE_SAVE_PATH = os.path.join(os.path.dirname(__file__), 'public', 'images')
# os.makedirs(IMAGE_SAVE_PATH, exist_ok=True)

# Ruta del archivo JSON
# JSON_FILE_PATH = os.path.join(os.path.dirname(__file__), 'products.json')

# def scrape_products():
#     url = 'https://listado.mercadolibre.com.ar/supermercado/bebes/higiene-cuidado-bebe/'
#     
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 # Safari/537.36'
#     }
    
#     response = requests.get(url, headers=headers)
#     if response.status_code != 200:
#         print(f"Error al realizar la solicitud: {response.status_code}")
#         return []

#     soup = BeautifulSoup(response.text, 'html.parser')
#     products_container = soup.find_all('li', class_="ui-search-layout__item")

#     if not products_container:
#         print("No se encontraron productos en la página.")
#         return []

#     new_products = []

#     for product in products_container[:50]:  # Limitamos a las primeras 50
#         title = product.find('h2').text.strip()
#         price = product.find('span', class_='andes-money-amount__fraction').text.strip()
#         
#         try:
#             img_link = product.find("img")["data-src"]
#         except KeyError:
 #            img_link = product.find("img")["src"]
# 
#         if title and price and img_link:
#             product_info = {
#                 "title": title,
#                 "price": price,
#                 "img_link": img_link,
#                 "category": "Bebés",
#                 "subcategory": "Higiene y cuidado del bebé"
 #            }
#             new_products.append(product_info)
#             print(f"Nombre: {product_info['title']}")
#             print(f"Precio: {product_info['price']}")
#             print(f"Imagen URL: {product_info['img_link']}")
#             print('---------------------')

            # Comentar la descarga de la imagen
            # download_image(img_link, title)

    # Cargar productos previos del JSON
#     existing_products = []
#     if os.path.exists(JSON_FILE_PATH):
#         with open(JSON_FILE_PATH, "r", encoding="utf-8") as json_file:
 #            try:
 #                existing_products = json.load(json_file)
#                 print(f"Productos existentes cargados: {len(existing_products)}")
 #            except json.JSONDecodeError:
#                 print("Error al decodificar el JSON existente. Creando un nuevo archivo.")
# 
 #    # Añadir los nuevos productos al JSON existente
#     all_products = existing_products + new_products

    # Guardar todos los productos de nuevo en el archivo JSON
    # Comentar la actualización del JSON
    # with open(JSON_FILE_PATH, "w", encoding="utf-8") as json_file:
    #     json.dump(all_products, json_file, ensure_ascii=False, indent=4)

 #    print(f"Total de productos guardados: {len(all_products)}")
    
    # Llamar a la función para actualizar las URLs de las imágenes
#     update_image_urls(all_products)

#     return new_products

# def update_image_urls(products):
 #    for product in products:
        # Sanitize the title to create a valid filename
#         sanitized_title = "".join(char for char in product['title'] if char.isalnum() or char.isspace()).replace(" ", "_")
        # Update the img_link with the new filename
 #        product['img_link'] = f"{sanitized_title}.webp"
    
    # Guardar los productos actualizados en el JSON
 #    with open(JSON_FILE_PATH, "w", encoding="utf-8") as json_file:
 #        json.dump(products, json_file, ensure_ascii=False, indent=4)
    
 #    print("URLs de las imágenes actualizadas y guardadas en el JSON.")

# Comentar la función de descarga de imágenes
# def download_image(img_url, title):
#     sanitized_title = "".join(char for char in title if char.isalnum() or char.isspace()).replace(" ", "_")
#     file_path = os.path.join(IMAGE_SAVE_PATH, f"{sanitized_title}.jpg")

#     try:
#         response = requests.get(img_url, stream=True)
#         response.raise_for_status()

#         with open(file_path, "wb") as img_file:
#             img_file.write(response.content)
#         print(f"Imagen guardada en: {file_path}")

#     except requests.RequestException as e:
#         print(f"Error al descargar la imagen {img_url}: {e}")

# Ejecutar la función
# if __name__ == "__main__":
 #    scrape_products()
