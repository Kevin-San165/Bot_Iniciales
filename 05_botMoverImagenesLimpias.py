import os
import shutil

# Función para mover imágenes a la carpeta correspondiente
def mover_imagenes_restantes(carpeta_origen, carpeta_destino):
    # Asegurarse de que la carpeta de destino exista
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
        print(f'Carpeta creada: {carpeta_destino}')

    # Mover imágenes de la carpeta de origen a la de destino
    for archivo in os.listdir(carpeta_origen):
        ruta_completa = os.path.join(carpeta_origen, archivo)
        if os.path.isfile(ruta_completa):  # Solo mover archivos
            destino = os.path.join(carpeta_destino, archivo)
            shutil.move(ruta_completa, destino)
            print(f'Imagen movida: {destino}')

# Directorios de tu sistema
carpeta_con_caracteres = r'C:\Users\Kevin Caldera\Downloads\1. GENERAL\0. Descargas Diarias\1. CopiaBots\03_imagenes_con_caracteres'
carpeta_sin_caracteres = r'C:\Users\Kevin Caldera\Downloads\1. GENERAL\0. Descargas Diarias\1. CopiaBots\03_imagenes_sin_caracteres'
carpeta_subir_imagenes_con_caracteres = r'C:\Users\Kevin Caldera\Downloads\1. GENERAL\0. Descargas Diarias\1. CopiaBots\06_subir_imagenes_con_caracteres'
carpeta_subir_imagenes_sin_caracteres = r'C:\Users\Kevin Caldera\Downloads\1. GENERAL\0. Descargas Diarias\1. CopiaBots\06_subir_imagenes_sin_caracteres'

# Mover imágenes restantes
mover_imagenes_restantes(carpeta_con_caracteres, carpeta_subir_imagenes_con_caracteres)
mover_imagenes_restantes(carpeta_sin_caracteres, carpeta_subir_imagenes_sin_caracteres)
