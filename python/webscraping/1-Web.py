import requests
from bs4 import BeautifulSoup

# URL de la página a hacer scraping
url = 'https://github.com/MarianoGarciaGz'

# Realizar la solicitud a la página
response = requests.get(url)
content=response.text

# Verificar si la solicitud fue exitosa (código 200)
if response.status_code == 200:
    # Parsear el contenido HTML de la página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar los elementos que contienen los títulos de las noticias
    titulos = soup.find_all('h2', class_='titulo-noticia')

    # Imprimir los títulos
    for titulo in titulos:
        print(titulo.text)
else:
    print(f'Error al acceder a la página. Código de estado: {response.status_code}')
