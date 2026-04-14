import tkinter as tk
import os
from tkinter import filedialog


def renomearArquivos(arquivos, destino, nome_base, contador):
    for arquivo in arquivos:
        if arquivo.lower().endswith(".jpg"):
            final = "jpg"
        elif arquivo.lower().endswith(".png"):
            final = "png"
        else:
            continue

        nome_final = f'{arquivo}" "{destino}/{nome_base}{contador}.{final}'

        com0 = f'mv "{arquivo}" "{destino}/{nome_base}{contador}.{final}"'

        print(com0)

        retorno = os.system(com0)
        print("Código de retorno:", retorno)

        contador = contador + 1

root = tk.Tk()
root.withdraw()

arquivos = filedialog.askopenfilenames()

print("Arquivo selecionado:", arquivos)

print("EXEMPLO -> fotos (Arquivos: fotos0, fotos1...) <- EXEMPLO")
nome_base = input("Insira o texto base para renomear: ")
contador = int(input("Insira o valor inicial da contagem: "))
destino = os.path.expanduser("~/Área de trabalho/Wallpapers")

renomearArquivos(arquivos, destino, nome_base, contador)
