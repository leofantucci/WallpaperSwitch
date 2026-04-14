import tkinter as tk
import os
from tkinter import filedialog

def escolherPasta():
    pasta = filedialog.askdirectory(title="Escolha a pasta de wallpapers")
    if not pasta:
        print("Nenhuma pasta selecionada.")
        exit()
    return pasta

def escolherImagens(pasta):
    fotos = [
        os.path.join(pasta, f)
        for f in os.listdir(pasta)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]
    return fotos

def escolherTempo():
    tempo = int(input("Insira o tempo para a troca de telas: "))
    return tempo

# DEFINE O TEMPO DE TROCA
tempo = 10

#DEFINE A PASTA PADRÃO
pasta = os.path.expanduser("~/Área de trabalho/WallpaperSwitch/Midia")

# SELECIONA AS IMAGENS
imagens = escolherImagens(pasta)
