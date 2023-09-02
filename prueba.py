#haz un programa para convertir un video en mp4 que se pide al usuario que lo seleccione a formato a mp3 y guardarlos en la ruta de C:\Program Files\Soundpad\sounds eligiendo el nombre del archivo y eliminar el archivo original

import os
import shutil
import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *

#pedir la ruta del archivo por ui
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

mp4_file = file_path

#pedir el nombre del archivo
nombre = input("Nombre del archivo para guardar: ")
mp3_file = nombre + ".mp3"

VideoClip = VideoFileClip(mp4_file)

audioclip = VideoClip.audio

audioclip.write_audiofile(mp3_file)

audioclip.close()

VideoClip.close()

#mover el archivo a la ruta de soundpad
shutil.move(mp3_file, "C:/Program Files/Soundpad/sounds")

#preguntar si se quiere  eliminar el archivo original
eliminar = input("¿Desea eliminar el archivo original? (s/n): ")

if eliminar == "s":
    os.remove(mp4_file)
else:
    print("El archivo no se eliminó")

    

    