# LIBREARIA SCRAPY

1- Instalar anaconda bajando el archivo desde [Anaconda](https://www.anaconda.com/)

2- Crear un nuevo ambiente en Anaconda Navigator

3- Play y abrir terminal en el ambiente para ejecutar:

conda install -c conda forge-c scrapy

o buscar el paquete ahí mismo en el navegador de anaconda e instalarlo

Abrir en terminal y ejecutar: where Python

Identificar la ruta: C:\Users\pc\.conda\envs\MyScrapy\python.exe

Se agrega la ruta a pycharm:

C:\Users\pc\.conda\envs\

Ejecutar en consola:

conda install -c conda-forge protego

Probar un par de comandos, con el segundo creamos un proyecto:

scrapy fetch http://google.com

scrapy startproject spider_tutorial

Comenzamos a usar nuestro spider mandando como parámetro una página web donde están disponibles datos de la población mundial, en la consola:

scrapy genspider worldometers https://www.worldometers.info/world-population/population-by-country

Se genera este resultado en la consola:

Created spider 'worldometers' using template 'basic' in module:

spider_tutorial.spiders.worldometers

PS C:\Users\pc\.conda\envs\spider_tutorial\spider_tutorial>

Se crear un archivo en Pycharm

# versión 1

import scrapy

class WorldometersSpider(scrapy.Spider):
name = "worldometers"
allowed_domains = ["www.worldometers.info"]
start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        title = response.xpath('//h1/text()').get()
        countries = response.xpath('//td/a/text()').getall()

        yield {
            'titles': title,
            'countries': countries,
        }

En terminal ejecutar:

scrapy crawl worldometers

# versión 2

import scrapy

class WorldometersSpider(scrapy.Spider):
name = "worldometers"
allowed_domains = ["www.worldometers.info"]
start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        rows = response.xpath('//tr')

        for row in rows:
            # title = response.xpath('//h1/text()').get()
            # countries = response.xpath('//td/a/text()').getall()
            countries = response.xpath('./td/a/text()').get()
            population = row.xpath('./td[3]/text()').get()

        yield {
            # 'titles': title,
            'countries': countries,
            'population': population,
        }

Ejecutar en terminal y revisar estos archivos nuevos

scrapy crawl worldometers -o population.csv

scrapy crawl worldometers -o population.json
