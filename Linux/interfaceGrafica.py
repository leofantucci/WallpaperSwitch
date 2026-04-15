import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import os
import subprocess

process = None
inputPasta = None
inputTempo = None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
gladeFile = os.path.join(BASE_DIR, "Interface", "Interface.glade")


def on_btnIniciar_clicked(widget):
    global process

    pasta = inputPasta.get_text().strip()
    tempo = inputTempo.get_text().strip()

    if not pasta:
        print("Erro: pasta vazia")
        return

    if not os.path.isdir(pasta):
        print("Erro: pasta inválida")
        return

    if not tempo:
        tempo = "5"

    process = subprocess.Popen(
        [
            "python3",
            "-m",
            "Linux.Codigos.wallpaperSwitch",
            pasta,
            tempo
        ],
        cwd=os.path.dirname(BASE_DIR)
    )

    print("Processo iniciado:", process.pid)


def on_btnParar_clicked(widget):
    global process
    if process:
        process.terminate()
        process = None
        print("Processo parado")


def on_btnPasta_clicked(widget):
    dialog = Gtk.FileChooserDialog(
        title="Escolha a pasta de wallpapers",
        parent=widget.get_toplevel(),
        action=Gtk.FileChooserAction.SELECT_FOLDER
    )

    dialog.add_buttons(
        Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
        Gtk.STOCK_OPEN, Gtk.ResponseType.OK
    )

    if dialog.run() == Gtk.ResponseType.OK:
        inputPasta.set_text(dialog.get_filename())

    dialog.destroy()


class App(Gtk.Application):
    def __init__(self):
        super().__init__()

    def do_activate(self):
        global inputPasta, inputTempo

        builder = Gtk.Builder()
        builder.add_from_file(gladeFile)

        window = builder.get_object("main")
        window.set_application(self)
        window.present()

        builder.get_object("btnIniciar").connect("clicked", on_btnIniciar_clicked)
        builder.get_object("btnParar").connect("clicked", on_btnParar_clicked)
        builder.get_object("btnPasta").connect("clicked", on_btnPasta_clicked)

        inputPasta = builder.get_object("inputPasta")
        inputTempo = builder.get_object("inputTempo")

        inputPasta.set_text(os.path.join(BASE_DIR, "Midia"))
        inputTempo.set_text("5")


app = App()
app.run()
