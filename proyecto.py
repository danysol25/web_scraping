import bs4
import requests

url_base = 'http://books.toscrape.com/index.html'

#resultado = requests.get(url_base.format('1'))
#sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

#libros = sopa.select('.product_pod')

#transformo en lista para extraer títulos

#ejemplo = libros[0].select('.star-rating.Three')
#print(ejemplo)

#lista de titulos con 4 o 5 estrellas:
titulos_rating_alto = []

#iterar páginas:
for pagina in range (1,51):
    #crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    #seleccionar datos del libro
    libros = sopa.select('.product_pod')

    #seleccionar libros
    for libro in libros:
        #chequear el ranking
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')):
            #guardar titulo
            titulo = libro.select('a')[1]['title']
            #agregar libro a lista
            titulos_rating_alto.append(titulo)

#ver la lista de libros e 4 y 5 estrellas
for t in titulos_rating_alto:
    print(t)