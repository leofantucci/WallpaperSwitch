import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import os
import subprocess

process = None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
gladeFile = os.path.join(BASE_DIR, "Interface", "Interface.glade")


def on_btnIniciar_clicked(widget):
    global process

    script_path = os.path.join(BASE_DIR, "Codigos", "wallpaperSwitch.py")

    process = subprocess.Popen(
        ["python3", "-m", "Linux.Codigos.wallpaperSwitch"],
        cwd=os.path.dirname(BASE_DIR)
    )

    print("Processo iniciado:", process.pid)


def on_btnParar_clicked(widget):
    global process
    if process:
        process.terminate()
        process = None
        print("Processo parado")


class App(Gtk.Application):
    def __init__(self):
        super().__init__()

    def do_activate(self):
        builder = Gtk.Builder()
        builder.add_from_file(gladeFile)

        window = builder.get_object("main")
        window.set_application(self)
        window.present()

        btnIniciar = builder.get_object("btnIniciar")
        btnIniciar.connect("clicked", on_btnIniciar_clicked)

        btnParar = builder.get_object("btnParar")
        btnParar.connect("clicked", on_btnParar_clicked)


app = App()
app.run()
