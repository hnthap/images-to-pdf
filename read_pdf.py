from pathlib import Path
from typing import Iterable

from PIL import Image

from normalize_paths import normalize_path


def save_images_as_pdf(image_files_arg: Iterable[str | Path], 
                       out_file_arg: str | Path, resolution = 300.0):
    
    # Normalize paths and validate input

    image_files = list(map(normalize_path, image_files_arg))
    assert len(image_files) > 0, 'No images provided'

    out_file = normalize_path(out_file_arg)
    assert out_file.suffix == '.pdf', 'Output file mus be a PDF file'

    # Convert images to PDF and save to output file

    images = list(map(Image.open, image_files))
    images[0].save(out_file, 'PDF', resolution=resolution, save_all=True, append_images=images[1:])
    print(images[0].im)
    for image in images:
        image.close()
