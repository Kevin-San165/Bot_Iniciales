import os
import shutil

def mover_imagenes_no_encontradas(codigos, carpeta_origen, carpeta_destino):
    # Crea la carpeta destino si no existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
    
    # Recorre todos los archivos en la carpeta origen
    for filename in os.listdir(carpeta_origen):
        # Extraer el nombre del archivo sin la extensión
        nombre_sin_extension = os.path.splitext(filename)[0]
        
        # Si el nombre del archivo coincide con un código no encontrado
        if nombre_sin_extension in codigos:
            # Mueve el archivo a la carpeta destino
            ruta_origen = os.path.join(carpeta_origen, filename)
            ruta_destino = os.path.join(carpeta_destino, filename)
            shutil.move(ruta_origen, ruta_destino)
            print(f"Moviendo {filename} a {ruta_destino}")

# Lista de códigos no encontrados
# codigos_no_encontrados = [
#     "-BGX510", "023114611-074", "090_50321_01", "131-8679_01", "131_7230_30", 
#     "1AB0175000065", "1AB167280002", "3AK97079ABAA", "3AL7821BAAF01", 
#     "3AL78856BAABO1", "3AL78886AAAAB01", "3AL79773AAAAA01", "4712KL-07W-B4948V", 
#     "8DG61279AAAAC1", "AT3545G-20-1AS", "BX9005E00324", "CMR 23", "EHE05036AA", 
#     "MB-ADP-750H", "MCPF-001", "SFP-JUNIPER- - 01", "T - CSF", "T - EC - 16GB", 
#     "T - ESS1", "UMM 160 R", "ZMXMP-OL64"
# ]

codigos_no_encontrados = [
    "0231OMUQ",
    "16020276-100",
    "1ABO17500065",
    "FANX30",
    "MXCH-SDH", 
]

# Define las carpetas
carpeta_origen = 'C:/Users/Lizeth Cardenas/Downloads/2024-20240912T161353Z-001/14-09-2024/imgCompletas'
carpeta_destino = 'C:/Users/Lizeth Cardenas/Downloads/2024-20240912T161353Z-001/14-09-2024/noEncontradas'

# Llamar a la función para mover las imágenes
mover_imagenes_no_encontradas(codigos_no_encontrados, carpeta_origen, carpeta_destino)
