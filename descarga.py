from imgurpython import ImgurClient
 
import os
import urllib.request
import timeit
 
clienteSec = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
clienteID = "bfa0e227a1c5643"
 
cliente = ImgurClient(clienteID, clienteSec)

def descarga_url_img(link):
   print(link)
   imgNombre = link.split("/")[3]
   imgFormato = imgNombre.split(".")[1]
   imgNombre = imgNombre.split(".")[0]
   print(imgNombre, imgFormato)
   urlLocal = "./imagenes/{}.{}"
   urllib.request.urlretrieve(link, urlLocal.format(imgNombre, imgFormato))
 
def main():
   id_album = "bUaCfoz"
   imagenes = cliente.get_album_images(id_album)
 
   for imagen in imagenes:
       descarga_url_img(imagen.link)
 
if __name__ == "__main__":
   print("Tiempo de descarga {}".format(timeit.Timer(main).timeit(number=1)))