import os

def escolherImagens(pasta):
    return [
        os.path.join(pasta, f)
        for f in os.listdir(pasta)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]


tempo = 3

pasta = os.path.expanduser(
    "~/Área de trabalho/WallpaperSwitch/Linux/Midia"
)
