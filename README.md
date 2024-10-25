# Simple pdf to image converter

## Usage

Just execute the script, it will ask for a directory where the pdf files containing images is, and will then convert all pdfs in this same directory into jpg-images.
These images will be saved in the same directory where the pdf's are laying. If an image file exists already, will skip this file.

## Build as executable

- install all dependencies using uv: `uv sync`
- run `pyinstaller --onefile pdf2imageconverter.py`
- in folder `dist` you will find your executable