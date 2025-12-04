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

# Función para mover las imágenes según el nombre del archivo
def mover_imagenes_por_caracter(carpeta_origen, carpeta_con_caracteres, carpeta_sin_caracteres):
    # Asegurarse de que las carpetas de destino existan
    if not os.path.exists(carpeta_con_caracteres):
        os.makedirs(carpeta_con_caracteres)
        print(f'Carpeta creada: {carpeta_con_caracteres}')
        
    if not os.path.exists(carpeta_sin_caracteres):
        os.makedirs(carpeta_sin_caracteres)
        print(f'Carpeta creada: {carpeta_sin_caracteres}')
    
    # Recorrer todos los archivos de la carpeta origen
    for archivo in os.listdir(carpeta_origen):
        ruta_completa = os.path.join(carpeta_origen, archivo)

        # Si es un archivo
        if os.path.isfile(ruta_completa):
            # Verificar si es una imagen
            if es_imagen(ruta_completa):
                # Determinar a qué carpeta mover la imagen según si contiene coma
                if '_' in archivo:
                    destino = os.path.join(carpeta_con_caracteres, archivo)
                else:
                    destino = os.path.join(carpeta_sin_caracteres, archivo)
                
                # Mover la imagen
                shutil.move(ruta_completa, destino)
                print(f'Imagen movida a: {destino}')
            else:
                # Si no es una imagen, imprimir mensaje de alerta
                print(f'ALERTA: El archivo "{archivo}" no es una imagen.')

# Directorios de tu sistema
carpeta_origen = r'F:\ZONA\1. GENERAL\0. Descargas Diarias\1. CopiaBots\02_imagenes_convertidas'
carpeta_con_caracteres = r'F:\ZONA\1. GENERAL\0. Descargas Diarias\1. CopiaBots\03_imagenes_con_caracteres'
carpeta_sin_caracteres = r'F:\ZONA\1. GENERAL\0. Descargas Diarias\1. CopiaBots\03_imagenes_sin_caracteres'

# Ejecutar el proceso
mover_imagenes_por_caracter(carpeta_origen, carpeta_con_caracteres, carpeta_sin_caracteres)
