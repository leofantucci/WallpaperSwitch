import tkinter as tk
import time
import random
import subprocess
import wallpaperSwitchConfig
import ctypes

root = tk.Tk()
root.withdraw()

pasta = wallpaperSwitchConfig.pasta
fotos = wallpaperSwitchConfig.escolherImagens(pasta)
tempo = wallpaperSwitchConfig.tempo

print("PASTA:", pasta)
print("IMAGENS ENCONTRADAS:", fotos)
print("QUANTIDADE:", len(fotos))

usadas = []

while True:
    disponiveis = [f for f in fotos if f not in usadas]

    if not disponiveis:
        usadas = []
        disponiveis = fotos

    foto = random.choice(disponiveis)
    usadas.append(foto)

    print("Usando:", foto)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, foto, 3)
    time.sleep(tempo)
