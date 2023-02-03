import gi

gi.require_version ("Gtk", "3.0")
from gi.repository import Gtk

class Aplicacion:

    def __init__(self):

        builder = Gtk.Builder()
        builder.add_from_file("saudoGlade.glade")

        fiestraPrincipal = builder.get_object("fiestraPrincipal")

if __name__=="__main__":
    Aplicacion()
    Gtk.main()