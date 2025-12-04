import os
import shutil
from PIL import Image

# Función para verificar si el archivo es una imagen
def es_imagen(archivo):
    try:
        with Image.open(archivo) as img:
            return True
    except IOError:
        return False

# Función para procesar imágenes
def procesar_imagenes(carpeta_origen, carpeta_destino):
    # Asegurarse de que la carpeta destino existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
        print(f'Carpeta creada: {carpeta_destino}')
    
    # Recorrer todos los archivos de la carpeta origen
    for archivo in os.listdir(carpeta_origen):
        ruta_completa = os.path.join(carpeta_origen, archivo)

        # Si es un archivo
        if os.path.isfile(ruta_completa):
            # Verificar si es una imagen
            if es_imagen(ruta_completa):
                # Abrir la imagen
                with Image.open(ruta_completa) as img:
                    # Convertir la imagen a formato jpg y guardarla en la carpeta destino
                    nombre_base, _ = os.path.splitext(archivo)
                    ruta_nueva = os.path.join(carpeta_destino, f'{nombre_base}.jpg')
                    
                    # Convertir y guardar la imagen en formato jpg
                    img.convert('RGB').save(ruta_nueva, 'JPEG')
                    print(f'Imagen procesada y movida: {ruta_nueva}')
            else:
                # Si no es una imagen, imprimir mensaje de alerta
                print(f'ALERTA: El archivo "{archivo}" no es una imagen.')

# Directorios de tu sistema
carpeta_origen = r'F:\ZONA\1. GENERAL\0. Descargas Diarias\1. CopiaBots\01_imagenes_iniciales'
carpeta_destino = r'F:\ZONA\1. GENERAL\0. Descargas Diarias\1. CopiaBots\02_imagenes_convertidas'

# Ejecutar el proceso
procesar_imagenes(carpeta_origen, carpeta_destino)
