from bs4 import BeautifulSoup
import requests

# URL de la página a hacer scraping
url = 'https://github.com/MarianoGarciaGz'

# Realizar la solicitud a la página
response = requests.get(url)
content=response.text

soup = BeautifulSoup(content, 'lxml')

# print(soup.prettify())

name=soup.find('span', class_='p-name')
desc=soup.find('div', class_='p-note')
print(name)
print(desc)

file_name = 'informacion_perfil.txt'
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(f'Nombre: {name.text}' if name else 'Nombre no encontrado\n')
    file.write(f'Descripción: {desc.text}' if desc else 'Descripción no encontrada\n')

print(f'La información se ha guardado en {file_name}')