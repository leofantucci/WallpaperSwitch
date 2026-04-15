import os

def escolherImagens(pasta):
    if not os.path.isdir(pasta):
        raise ValueError(f"Pasta inválida: {pasta}")

    return [
        os.path.join(pasta, f)
        for f in os.listdir(pasta)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]
