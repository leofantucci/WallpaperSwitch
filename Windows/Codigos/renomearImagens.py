import tkinter as tk
import os
from tkinter import filedialog


def renomearArquivos(arquivos, destino, nome_base, contador):
    # garante que a pasta existe
    os.makedirs(destino, exist_ok=True)

    for arquivo in arquivos:
        extensao = os.path.splitext(arquivo)[1].lower()

        if extensao not in [".jpg", ".jpeg", ".png"]:
            continue

        if extensao == ".jpeg":
            extensao = ".jpg"

        novo_nome = f"{nome_base}{contador}{extensao}"
        novo_caminho = os.path.join(destino, novo_nome)

        print(f"Renomeando: {arquivo} -> {novo_caminho}")

        try:
            os.rename(arquivo, novo_caminho)
            print("OK")
        except Exception as e:
            print("Erro:", e)

        contador += 1


# 🪟 Interface para selecionar arquivos
root = tk.Tk()
root.withdraw()

arquivos = filedialog.askopenfilenames(
    title="Selecione as imagens",
    filetypes=[("Imagens", "*.jpg *.jpeg *.png")]
)

print("Arquivos selecionados:", arquivos)

if not arquivos:
    print("Nenhum arquivo selecionado.")
    exit()

# 🧾 Inputs
print("EXEMPLO -> fotos (Arquivos: fotos0, fotos1...)")
nome_base = input("Insira o texto base para renomear: ")
contador = int(input("Insira o valor inicial da contagem: "))

# 📁 Destino (Windows Desktop)
destino = os.path.join(
    os.path.expanduser("~"),
    "Desktop",
    "Wallpapers"
)

# 🚀 Executa
renomearArquivos(arquivos, destino, nome_base, contador)
