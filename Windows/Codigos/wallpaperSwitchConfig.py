import tkinter as tk
import os
from tkinter import filedialog

def escolherPasta():
    root = tk.Tk()
    root.withdraw()  # esconde janela principal

    pasta = filedialog.askdirectory(title="Escolha a pasta de wallpapers")

    if not pasta:
        print("Nenhuma pasta selecionada.")
        exit()

    return pasta


def escolherImagens(pasta):
    extensoes = (".png", ".jpg", ".jpeg", ".bmp", ".webp")

    fotos = [
        os.path.join(pasta, f)
        for f in os.listdir(pasta)
        if f.lower().endswith(extensoes)
    ]

    return fotos


def escolherTempo():
    try:
        tempo = int(input("Insira o tempo (segundos) para troca de wallpapers: "))
        return tempo
    except:
        print("Valor inválido, usando 10 segundos.")
        return 10


# 🔧 CONFIG PADRÃO (caso não queira usar seletor)
tempo = 10

# 📁 Pasta padrão no Windows (corrigida)
pasta = os.path.join(
    os.path.expanduser("~"),
    "Desktop",
    "WallpaperSwitch",
    "Midia"
)

# 🧠 Escolher pasta via interface (opcional)
# descomente se quiser escolher manualmente:
# pasta = escolherPasta()

# 🖼️ Carrega imagens
imagens = escolherImagens(pasta)
