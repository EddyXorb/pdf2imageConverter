#!/usr/bin/python3

from pdf2image import convert_from_bytes
import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
import logging
from rich.logging import RichHandler
from rich.progress import track
from rich import print

root = tk.Tk()
root.withdraw()  # Hide the root window

print("PDF to JPG converter")
print("Select the directory where the PDF files are located...")
directory = filedialog.askdirectory(title="Select Directory with PDF Files")
if not directory:
    print("No directory selected. Exiting...")
    exit()

# Configure logging
log_file = os.path.join(directory, "conversion2jpg.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(log_file), RichHandler()],
)
logger = logging.getLogger("pdf2imageconverter")
logger.info(f"Chosen location where to look after pdf-files to convert: {directory}")

files_to_convert = []
for item in Path(directory).iterdir():
    if item.is_file() and item.suffix.lower() == ".pdf":
        files_to_convert.append(item)

logger.info(f"Found {len(files_to_convert)} PDF files to convert.")

for file in track(files_to_convert):
    logger.info(f"Converting {file}...")
    images = convert_from_bytes(open(file, "rb").read())
    for i in range(len(images)):
        filename = (
            Path(directory) / f"{file.stem}{'_' + i if len(images) >  1 else ''}.jpg"
        )
        if os.path.exists(filename):
            logger.warning(f"File {filename} already exists. Skipping...")
            continue
        images[i].save(filename, quality=70)

print("\n")
print("Conversion finished, print entered to exit...")
input()
