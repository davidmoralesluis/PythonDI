import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacion:

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("/home/dam2a/Escritorio/Python/glade/listaTarefasTreeView.glade")



        wndFiestraPrincipal = builder.get_object("wndFiestraPrincipal")
        self.tvwTarefas = builder.get_object("tvwTarefas")
        self.modeloLista = builder.get_object("modeloLista")
        self.tvcTarefa = builder.get_object ("tvcTarefa2")
        self.tvcFeito = builder.get_object ("trcFeito")
        self.txtTarefa = builder.get_object("txtTarefa")
        self.btnEngadir = builder.get_object("btnEngadir")
        self.crtFeito = builder.get_object ("crtFeito")
        print(self.crtFeito.get_property("editing"))
        self.crtTarefa = builder.get_object("crtTarefa")

        #self.crtTarefa.set_property("editable", True)
        #self.crtFeito.set_property("editable",True)
        #self.crtFeito.connect("toggled",self.on_crtFeito_toggled )

        #modeloLista = Gtk.ListStore(str, bool)
        #self.tvwTarefas.set_model(modeloLista)


        sinais = { "on_wndFiestraPrincipal_destroy": Gtk.main_quit,
                   "on_btnEngadir_clicked" : self.on_btnEngadir_clicked,
                   "on_txtTarefa_activate" : self.on_txtTarefa_activate,
                   "on_btnFeito_clicked": self.on_btnFeito_clicked,
                   "on_btnBorrar_clicked": self.on_btnBorrar_clicked,
                   "on_crtFeito_toggled" : self.on_crtFeito_toggled
        }

        builder.connect_signals(sinais)
        wndFiestraPrincipal.show_all()


    def on_btnEngadir_clicked (self, boton):
        self.engadirTarefa()

    def on_btnFeito_clicked (self, boton):
        seleccion = self.tvwTarefas.get_selection()
        modelo, fila = seleccion.get_selected()
        if fila is not None:
            modelo.set (fila, (0,), (True,))
            print (modelo[fila][0])

    def on_btnBorrar_clicked (self, boton):
        seleccion = self.tvwTarefas.get_selection()
        modelo, fila = seleccion.get_selected()
        if fila is not None:
            modelo.remove(fila)

    def on_txtTarefa_activate (self, cadroTexto):
        self.engadirTarefa()

    def engadirTarefa(self):
        modelo = self.tvwTarefas.get_model()
        pos = modelo.append ((False, self.txtTarefa.get_text() ))
        #modelo.set (pos, (0,1), (False, self.txtTarefa.get_text() ))
        self.txtTarefa.set_text(""  )

    def on_crtFeito_toggled(self, celda, fila, modelo):
        modelo[fila][0] = not self.modeloLista [fila][0]
        print(self.modeloLista[fila][0])
        print ("Executo on_crtFeito")



if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
