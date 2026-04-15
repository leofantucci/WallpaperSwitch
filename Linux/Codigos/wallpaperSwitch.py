import time
import random
import subprocess
import os
import sys

from Linux.Codigos import wallpaperSwitchConfig


def trocarWallpaper(foto):
    subprocess.run([
        "qdbus6",
        "org.kde.plasmashell",
        "/PlasmaShell",
        "org.kde.PlasmaShell.evaluateScript",
        f"""
            var desktops = desktops();
            for (var i = 0; i < desktops.length; i++) {{
                var d = desktops[i];
                d.wallpaperPlugin = 'org.kde.image';
                d.currentConfigGroup = ['Wallpaper', 'org.kde.image', 'General'];
                d.writeConfig('Image', 'file://{foto}');
                d.writeConfig('ImageFillMode', 0);
            }}
        """
    ])


def main():
    # 🔥 recebe argumentos da interface
    if len(sys.argv) < 3:
        print("Uso: python -m Linux.Codigos.wallpaperSwitch <pasta> <tempo>")
        sys.exit(1)

    pasta = os.path.expanduser(sys.argv[1])
    tempo = int(sys.argv[2])

    try:
        fotos = wallpaperSwitchConfig.escolherImagens(pasta)
    except Exception as e:
        print("Erro:", e)
        sys.exit(1)

    print("PASTA:", pasta)
    print("IMAGENS:", len(fotos))
    print("TEMPO:", tempo)

    usadas = []

    while True:
        disponiveis = [f for f in fotos if f not in usadas]

        if not disponiveis:
            usadas = []
            disponiveis = fotos

        foto = random.choice(disponiveis)
        trocarWallpaper(foto)

        usadas.append(foto)

        print("Wallpaper:", foto)

        time.sleep(tempo)


if __name__ == "__main__":
    main()
