#OBSOLETO

# --- Conversión de imágenes CZI a JPG ---
import os
from pathlib import Path
import numpy as np
from tifffile import imread
from PIL import Image
import czifile

# --- Paths ---
base_dir = Path(r"D:\Bioinformatica\Investigacion\Smithsonian\Podocarpus_Analysis\00_Training_and_Classification")
input_dir = base_dir / "Podocarpus_Modern"
output_dir = base_dir / "Podocarpus_Modern_jpg"
output_dir.mkdir(parents=True, exist_ok=True)

# --- Conversión con normalización ---
def normalize_to_uint8(image):
    """Normaliza la intensidad a rango 0-255 (8 bits)"""
    img = image.astype(np.float32)
    img = img - img.min()
    if img.max() > 0:
        img = img / img.max()
    img = (img * 255).astype(np.uint8)
    return img

def convert_czi_to_jpg(czi_path, jpg_path):
    try:
        with czifile.CziFile(czi_path) as czi:
            data = czi.asarray()

        # Asegurar que sea 2D (tomamos la primera slice si hay varias)
        img = data.squeeze()

        # Si hay más de 2D, colapsamos usando máximo proyectado
        if img.ndim > 2:
            img = img.max(axis=0)

        # Normalizar intensidades
        img_8bit = normalize_to_uint8(img)

        # Guardar como JPG
        Image.fromarray(img_8bit).save(jpg_path, quality=95)
        print(f"[OK] {czi_path.name} -> {jpg_path}")
    except Exception as e:
        print(f"[ERROR] No se pudo convertir {czi_path}: {e}")

# --- Loop sobre todas las carpetas y archivos ---
for genus_folder in input_dir.iterdir():
    if genus_folder.is_dir():
        out_genus = output_dir / genus_folder.name
        out_genus.mkdir(exist_ok=True)

        for czi_file in genus_folder.glob("*.czi"):
            jpg_file = out_genus / (czi_file.stem + ".jpg")
            convert_czi_to_jpg(czi_file, jpg_file)
