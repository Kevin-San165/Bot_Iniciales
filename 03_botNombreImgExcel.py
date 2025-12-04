import os
import pandas as pd

# Función para obtener los nombres de los archivos de una carpeta sin la extensión
def obtener_nombres_imagenes_sin_extension(carpeta):
    nombres_imagenes = []
    for archivo in os.listdir(carpeta):
        ruta_completa = os.path.join(carpeta, archivo)
        # Solo agregar si es un archivo y no un directorio
        if os.path.isfile(ruta_completa):
            # Obtener el nombre del archivo sin la extensión
            nombre_sin_extension = os.path.splitext(archivo)[0]
            nombres_imagenes.append(nombre_sin_extension)
    return nombres_imagenes

# Función para guardar nombres en un archivo Excel
def guardar_nombres_en_excel(nombres, archivo_excel):
    df = pd.DataFrame(nombres, columns=["Nombre de Imagen"])
    df.to_excel(archivo_excel, index=False)
    print(f'Archivo Excel guardado: {archivo_excel}')

# Función principal
def procesar_nombres_imagenes(carpeta_con_caracteres, carpeta_sin_caracteres, carpeta_excel):
    # Asegurarse de que la carpeta Excel existe
    if not os.path.exists(carpeta_excel):
        os.makedirs(carpeta_excel)
        print(f'Carpeta creada: {carpeta_excel}')

    # Obtener los nombres de las imágenes sin extensión de cada carpeta
    nombres_con_caracteres = obtener_nombres_imagenes_sin_extension(carpeta_con_caracteres)
    nombres_sin_caracteres = obtener_nombres_imagenes_sin_extension(carpeta_sin_caracteres)

    # Rutas de los archivos Excel
    archivo_con_caracteres = os.path.join(carpeta_excel, 'nombres_con_caracteres.xlsx')
    archivo_sin_caracteres = os.path.join(carpeta_excel, 'nombres_sin_caracteres.xlsx')

    # Guardar nombres en los archivos Excel
    guardar_nombres_en_excel(nombres_con_caracteres, archivo_con_caracteres)
    guardar_nombres_en_excel(nombres_sin_caracteres, archivo_sin_caracteres)

# Directorios de tu sistema
carpeta_con_caracteres = r'F:\ZONA\1. GENERAL\0. Descargas Diarias\1. CopiaBots\03_imagenes_con_caracteres'
carpeta_sin_caracteres = r'F:\ZONA\1. GENERAL\0. Descargas Diarias\1. CopiaBots\03_imagenes_sin_caracteres'
carpeta_excel = r'F:\ZONA\1. GENERAL\0. Descargas Diarias\1. CopiaBots\04_excel_datos'

# Ejecutar el proceso
procesar_nombres_imagenes(carpeta_con_caracteres, carpeta_sin_caracteres, carpeta_excel)
