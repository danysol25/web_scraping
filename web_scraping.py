import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/?m=1')

print(type(resultado))

#print(resultado.text) #extrae todo el texto

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
print(sopa.select('title')) #Selecciona las etiquetas que yo solicito
print(sopa.select('p'))
print(sopa.select('title')[0].getText()) #discrimino la etiqueta para mostrar SOLO el contenido

resultado_articulo = requests.get('https://escueladirecta-blog.blogspot.com/2022/10/por-que-se-utiliza-python-en-ciencia-de.html?m=1')
sopa_articulo = bs4.BeautifulSoup(resultado_articulo.text, 'lxml')
print(sopa_articulo.select('p')) #selecciona todas las etiquetas 'p'
print(sopa_articulo.select('p')[2]) #elijo el elemento que me interesa
print(sopa_articulo.select('p')[3].getText()) # elijo el texto sin la etiqueta

#SELECCIONAR POR CLASE
seleccion_clase = sopa_articulo.select('.dim-overlay hidden')
print(seleccion_clase) 

seleccion_etiquetas = sopa_articulo.select('span>b')
print(seleccion_etiquetas)

