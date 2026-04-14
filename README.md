# CONFIGURAÇÕES
Uma aplicação feita para trocar seu wallpaper de tempos em tempos, roda no Linux e talbez no Windows
Para fazer modificações do local da pasta e/ou tempo entre no diretório de Códigos, vá para o arquivo WallpaperSwitchConfig.py e altere para o endereço e/ou tempo desejado...

# RODANDO O APLICATIVO
Para rodar o app, digite no seu terminal: python ~/Área de Trabalho/Codigos/wallpaperSwitch.py

# CONFIGURAR PARA INICIALIZAR QUANDO PC LIGAR/REINICIAR
mkdir -p ~/.config/autostart
nano ~/.config/autostart/inicialização.desktop
Dentro do inicialização.desktop

## ======================================
## 🐧 INSTAÇALAÇÕES NECESSÁRIAS - LINUX
## ======================================
# 
sudo pacman -S python   # Arch/Manjaro
sudo apt install python3 # Ubuntu/Debian
## 1. Install Python
Arch / Manjaro:
sudo pacman -S python python-pip

Ubuntu / Debian:
sudo apt update
sudo apt install python3 python3-pip

Fedora:
sudo dnf install python3 python3-pip

### 2. Required KDE tools (ONLY if using KDE Plasma version)
Arch / Manjaro:
sudo pacman -S kde-cli-tools qt6-tools

Ubuntu / Debian:
sudo apt install kde-cli-tools qt6-tools

Fedora:
sudo dnf install kde-cli-tools qt6-qttools

### 3. (Optional) Tkinter support
Ubuntu / Debian:
sudo apt install python3-tk

Arch / Manjaro:
sudo pacman -S tk

## =======================================
## 🪟 INSTALAÇÕEOS NECESSÁRIAS - WINDOWS
## =======================================

### 1. Install Python
Download from:
https://www.python.org/downloads/

IMPORTANT:
✔ Mark "Add Python to PATH" during installation

### 2. Check installation
Open CMD or PowerShell:
python --version

### 3. Install Tkinter (usually already included)
If missing (rare):
pip install tk
