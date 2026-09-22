from PIL import Image
import pillow_heif
from pathlib import Path
import tkinter
from tkinter import filedialog


tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing

path = filedialog.askdirectory()
folder = Path(path)  # change this
extensions = {".heic", ".heif"}

files = [
    str(p.name)
    for p in folder.iterdir()
    if p.is_file() and p.suffix.lower() in extensions
]

# Include subfolders
# file_paths = [
#     str(p)
#     for p in folder.rglob("*")
#     if p.is_file() and p.suffix.lower() in extensions
# ]

for file in files:

    heif_file = pillow_heif.read_heif(path + "/" + file)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
    )

    image.save(f"./{file[:-5]}.jpeg", format("jpeg"))


