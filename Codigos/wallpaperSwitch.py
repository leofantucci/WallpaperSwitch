import tkinter as tk
import time
import random
import subprocess
import wallpaperSwitchConfig

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
    subprocess.run([
        "qdbus6",
        "org.kde.plasmashell",
        "/PlasmaShell",
        "org.kde.PlasmaShell.evaluateScript",
        f"""
            var d = desktops()[0];
            d.wallpaperPlugin = 'org.kde.image';
            d.currentConfigGroup = ['Wallpaper', 'org.kde.image', 'General'];
            d.writeConfig('Image', 'file://{foto}');
            d.writeConfig('ImageFillMode', 0);
        """
        ])
    time.sleep(tempo)
