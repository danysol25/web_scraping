import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/?m=1')
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

selec_img = sopa.select('.profile-img')[0]['src'] #selecciono el objetivo / la imagen a la que apunto extraer, de manera específica
print(selec_img)

imagen1 = requests.get(selec_img)
f = open('mi_imagen.jpg', 'wb') # abrir el archivo
f.write(imagen1.content) # escribo el archivo
f.close() # cierro el archivo.