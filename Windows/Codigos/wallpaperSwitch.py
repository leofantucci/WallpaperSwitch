import time
import random
import ctypes
import os
import wallpaperSwitchConfig

# Esconde janela (opcional)
import tkinter as tk
root = tk.Tk()
root.withdraw()

pasta = wallpaperSwitchConfig.pasta
fotos = wallpaperSwitchConfig.escolherImagens(pasta)
tempo = wallpaperSwitchConfig.tempo

print("PASTA:", pasta)
print("IMAGENS ENCONTRADAS:", fotos)
print("QUANTIDADE:", len(fotos))

# garante caminhos absolutos (IMPORTANTE no Windows)
fotos = [os.path.abspath(f) for f in fotos]

usadas = []

while True:
    disponiveis = [f for f in fotos if f not in usadas]

    if not disponiveis:
        usadas = []
        disponiveis = fotos

    foto = random.choice(disponiveis)
    usadas.append(foto)

    print("Usando:", foto)

    # 🔥 muda wallpaper no Windows
    ctypes.windll.user32.SystemParametersInfoW(20, 0, foto, 3)

    time.sleep(tempo)
