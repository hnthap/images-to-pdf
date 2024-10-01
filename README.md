# Images-to-PDF

Converts image files into a single PDF using the `PIL` library.

## Setup

```bash
python -m venv env
./env/Scripts/activate # or run "source ./env/bin/activate"
pip install -r requirements.txt # only the PIL package is needed
```

## Usage

Run the script:

```bash
python images_to_pdf.py [image_files] -o [output_pdf_name] -r [resolution]
```

Replace `[image_files]` with the paths to the images (may including wildcards), `[output_pdf_name]` with your desired path of the PDF file and `[resolution]` with your desired image resolution (300 by default).

The script will create a new PDF file containing all specified image files, in the order as specified.

Example:

```bash
# Create a new PDF file named "temp/output.pdf" containing all images located
# in the "temp/images/" directory, using the file pattern "*.png".
python temp/images/*.png -o temp/output.pdf
```
