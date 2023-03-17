import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from conexionBD import ConexionBD


class Aplicacion(Gtk.Window):

    def __init__(self):
        super().__init__(title="Exemplo ComboBox")

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)

        modelo = Gtk.ListStore(str,str,int,str)
        modeloPerfis = Gtk.ListStore(str,int)

        tryPerfilesUsuarios = Gtk.TreeView(model=modelo)

        celda = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("DNI", celda, text=0)
        tryPerfilesUsuarios.append_column(columna)

        celda2 = Gtk.CellRendererText()
        columna2 = Gtk.TreeViewColumn("Nome", celda2, text=1)
        tryPerfilesUsuarios.append_column(columna2)

        """celda3 = Gtk.CellRendererText()
        columna3 = Gtk.TreeViewColumn("Perfil", celda3, text=3)
        tryPerfilesUsuarios.append_column(columna3)
"""
        bd = ConexionBD("/home/dam2a/Escritorio/Python/PythonDI/Examen/perfisUsuarios.bd")
        conectBD = bd.conectaBD()
        cursorBD = bd.creaCursor()
        sqlUsuarios = "SELECT dni, nome FROM usuarios"
        sqlPerfisUsuario = "SELECT idPerfil FROM perfisUsuario WHERE dniUsuario=?"
        sqlPerfis = "SELECT descricion FROM perfis WHERE idPefil=?"
        sqlTodoPerfis = "SELECT descricion,idPefil FROM perfis"

        lUsuarios = bd.consultaSenParametros(sqlUsuarios)

        for usuario in lUsuarios:
            idPefil = bd.consultaConParametros(sqlPerfisUsuario, usuario[0])
            descripcionPerfil = bd.consultaConParametros(sqlPerfis, idPefil[0][0])
            elemento = list(usuario)
            elemento.append(idPefil[0][0])
            elemento.append(descripcionPerfil[0][0])
            modelo.append(elemento)

        listaTodoPerfis = bd.consultaSenParametros(sqlTodoPerfis)
        for perfil in listaTodoPerfis:
            modeloPerfis.append(perfil)

        celda3 = Gtk.CellRendererCombo()
        celda3.set_property("editable",True)
        celda3.set_property("model",modeloPerfis)
        celda3.set_property("text-column", 0)
        celda3.set_property("has-entry", False)
        celda3.connect("changed", self.on_celda3_changed, modelo, modeloPerfis)
        columna3 = Gtk.TreeViewColumn("Perfil", celda3, text=3)

        """sinais = {"on_wndFiestraPrincipal_destroy": Gtk.main_quit,
                  "on_btnEngadir_clicked": self.on_btnEngadir_clicked,
                  "on_txtTarefa_activate": self.on_txtTarefa_activate,
                  "on_btnFeito_clicked": self.on_btnFeito_clicked,
                  "on_btnBorrar_clicked": self.on_btnBorrar_clicked,
                  "on_crtFeito_toggled": self.on_crtFeito_toggled
                  }
        celda3.connect()"""

        tryPerfilesUsuarios.append_column(columna3)

        caixaV.pack_start(tryPerfilesUsuarios,True,True,0)

        self.add(caixaV)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_celda3_changed (self, cellRendererCombo, fila, elemento, modeloTrv, modeloCmbPerfis):
        modeloTrv[fila][2] = modeloCmbPerfis[elemento][1]
        modeloTrv[fila][3] = modeloCmbPerfis[elemento][0]


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
