import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacion (Gtk.Window):

    def __init__(self):
        super().__init__(title="Lista tarefas")

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)

        modelo = Gtk.ListStore(str,bool)
        modelo.append (("Tarefa 1", False))
        self.tvwTarefas = Gtk.TreeView()
        self.tvwTarefas.set_model(modelo)
        crtTarefa = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Tarefa",crtTarefa, text=0)
        crtTarefa.set_property("editable",True)
        crtTarefa.connect("edited",self.on_crtTarefa_edited,modelo)
        self.tvwTarefas.append_column(columna)

        crtFeito = Gtk.CellRendererToggle()
        columna = Gtk.TreeViewColumn("Feito", crtFeito, active=1)
        self.tvwTarefas.append_column(columna)
        crtFeito.connect("toggled", self.on_crtFeito_toggled ,modelo)




        caixaV.pack_start(self.tvwTarefas,True, True, 1)
        self.add(caixaV)

        self.connect ("destroy", Gtk.main_quit)
        self.show_all()


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
        modelo[fila][1] = not modelo [fila][1]
        print(modelo[fila][1])
        print ("Executo on_crtFeito")

    def on_crtTarefa_edited(self, celda, fila,texto, modelo):
        print("cambio "+modelo[fila][0]+" -> "+texto)
        modelo[fila][0] = texto




if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
