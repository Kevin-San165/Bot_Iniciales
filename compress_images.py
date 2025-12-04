import os
from PIL import Image
import shutil

def compress_image(input_path, output_path, max_size_kb=450):
    """Comprime la imagen a un tamaño máximo especificado en KB."""
    img = Image.open(input_path)
    
    # Calcula el tamaño objetivo en bytes
    target_size = max_size_kb * 1024  # Convertir KB a bytes
    quality = 95  # Calidad inicial 95%
    
    while True:
        img.save(output_path, format='JPEG', quality=quality)
        current_size = os.path.getsize(output_path)
        
        if current_size <= target_size or quality <= 10:
            break
        quality -= 5  # Disminuir la calidad para reducir el tamaño

def process_images(folder_path, compressed_folder):
    """Lee todas las imágenes de una carpeta y comprime las que superen los 500 KB."""
    # Crea la carpeta de imágenes comprimidas si no existe
    os.makedirs(compressed_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        input_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_size_kb = os.path.getsize(input_path) / 1024  # Convertir a KB
            
            # Mover imágenes mayores a 500 KB a la carpeta de comprimidas
            if file_size_kb > 480:
                output_path = os.path.join(compressed_folder, filename)
                shutil.move(input_path, output_path)  # Mover imagen a la carpeta
                print(f"Movida: {filename} -> {output_path}")
                
                # Comprimir imagen y guardarla de nuevo en la misma ubicación
                compress_image(output_path, output_path)  # Comprime la imagen sin cambiar el nombre
                print(f"Comprimida: {filename}")

if __name__ == "__main__":
    folder_path = r"F:\ZONA\1. GENERAL\0. Descargas Diarias\1. CopiaBots\03_imagenes_sin_caracteres"  # Ruta de tu carpeta
    compressed_folder = r"F:\ZONA\1. GENERAL\0. Descargas Diarias\1. CopiaBots\03_imagenes_sin_caracteres\03_imagenes_comprimidas"  # Carpeta de imágenes comprimidas
    process_images(folder_path, compressed_folder)
