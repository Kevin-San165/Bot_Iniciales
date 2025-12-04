import os
import shutil
import pandas as pd

# Función para leer nombres desde un archivo Excel sin encabezadoOOO
def leer_nombres_desde_excel(archivo_excel):
    df = pd.read_excel(archivo_excel, header=None)  # Lee el archivo sin encabezado
    if df.empty:
        print(f"Archivo vacío: {archivo_excel}")
        return []  # Devuelve una lista vacía si el archivo está vacío
    return df[0].astype(str).tolist()  # Convierte los valores a str y devuelve la primera columna

# Función para mover imágenes según la lista de nombres
def mover_imagenes(carpeta_origen, nombres_no_encontrados, carpeta_no_encontradas):
    # Asegurarse de que las carpetas de destino existan
    if not os.path.exists(carpeta_no_encontradas):
        os.makedirs(carpeta_no_encontradas)
        print(f'Carpeta creada: {carpeta_no_encontradas}')

    # Obtener los nombres de las imágenes en la carpeta de origen
    nombres_imagenes_en_carpeta = {os.path.splitext(archivo)[0] for archivo in os.listdir(carpeta_origen) if os.path.isfile(os.path.join(carpeta_origen, archivo))}
    
    # Procesar cada nombre en la lista de nombres
    for nombre in nombres_no_encontrados:
        archivo = nombre + '.jpg'  # Suponiendo que el formato es .jpg
        ruta_completa = os.path.join(carpeta_origen, archivo)
        
        if os.path.exists(ruta_completa):
            # Mover a la carpeta de no encontradas
            destino = os.path.join(carpeta_no_encontradas, archivo)
            shutil.move(ruta_completa, destino)
            print(f'Imagen movida a no encontradas: {destino}')
        else:
            print(f'Imagen no encontrada: {archivo} en {carpeta_origen}')

# Directorios de tu sistema
carpeta_con_caracteres = r'C:\Users\Kevin Caldera\Downloads\1. GENERAL\0. Descargas Diarias\1. CopiaBots\03_imagenes_con_caracteres'
carpeta_sin_caracteres = r'C:\Users\Kevin Caldera\Downloads\1. GENERAL\0. Descargas Diarias\1. CopiaBots\03_imagenes_sin_caracteres'
carpeta_no_encontradas_con_caracteres = r'C:\Users\Kevin Caldera\Downloads\1. GENERAL\0. Descargas Diarias\1. CopiaBots\05_imagenes_no_encontradas_con_caracteres'
carpeta_no_encontradas_sin_caracteres = r'C:\Users\Kevin Caldera\Downloads\1. GENERAL\0. Descargas Diarias\1. CopiaBots\05_imagenes_no_encontradas_sin_caracteres'


# Leer nombres desde archivos Excel
nombres_no_encontrados_con_caracteres = leer_nombres_desde_excel(r'C:\Users\Kevin Caldera\Downloads\1. GENERAL\0. Descargas Diarias\1. CopiaBots\04_excel_datos\no_encontrados_con_caracteres.xlsx')
nombres_no_encontrados_sin_caracteres = leer_nombres_desde_excel(r'C:\Users\Kevin Caldera\Downloads\1. GENERAL\0. Descargas Diarias\1. CopiaBots\04_excel_datos\no_encontrados_sin_caracteres.xlsx')

# Mover imágenes según la lista de nombres
if nombres_no_encontrados_con_caracteres:
    mover_imagenes(carpeta_con_caracteres, nombres_no_encontrados_con_caracteres, carpeta_no_encontradas_con_caracteres)
else:
    print("No se encontraron imágenes en el archivo no_encontrados_con_caracteres.xlsx")

if nombres_no_encontrados_sin_caracteres:
    mover_imagenes(carpeta_sin_caracteres, nombres_no_encontrados_sin_caracteres, carpeta_no_encontradas_sin_caracteres)
else:
    print("No se encontraron imágenes en el archivo no_encontrados_sin_caracteres.xlsx")
