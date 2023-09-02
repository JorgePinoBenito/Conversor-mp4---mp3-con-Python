import os
import shutil
import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

mp4_file = file_path

nombre = input("Nombre del archivo para guardar: ")
mp3_file = nombre + ".mp3"

VideoClip = VideoFileClip(mp4_file)

audioclip = VideoClip.audio

audioclip.write_audiofile(mp3_file)

audioclip.close()

VideoClip.close()

shutil.move(mp3_file, "C:/Program Files/Soundpad/sounds")

eliminar = input("¿Desea eliminar el archivo original? (s/n): ")

if eliminar == "s":
    os.remove(mp4_file)
else:
    print("El archivo no se eliminó")
