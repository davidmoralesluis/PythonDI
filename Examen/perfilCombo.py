import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from conexionBD import ConexionBD


class Aplicacion(Gtk.Window):

    def __init__(self):
        super().__init__(title="Exemplo CellRenderer")

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)

        modelo = Gtk.ListStore(str,str,int,str)
        modeloPerfis = Gtk.ListStore(str,str)

        tryPerfilesUsuarios = Gtk.TreeView(model=modelo)

        celda = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("DNI", celda, text=0)
        tryPerfilesUsuarios.append_column(columna)

        celda2 = Gtk.CellRendererText()
        columna2 = Gtk.TreeViewColumn("Nome", celda2, text=1)
        tryPerfilesUsuarios.append_column(columna2)

        celda3 = Gtk.CellRendererText()
        columna3 = Gtk.TreeViewColumn("Perfil", celda3, text=3)
        tryPerfilesUsuarios.append_column(columna3)

        bd = ConexionBD("/home/dam2a/Escritorio/Python/PythonDI/Examen/perfisUsuarios.bd")
        conectBD = bd.conectaBD()
        cursorBD = bd.creaCursor()
        sqlUsuarios = "SELECT dni, nome FROM usuarios"
        sqlPerfisUsuario = "SELECT idPerfil FROM perfisUsuario WHERE dniUsuario=?"
        sqlPerfis = "SELECT descricion FROM perfis WHERE idPefil=?"

        lUsuarios = bd.consultaSenParametros(sqlUsuarios)

        for usuario in lUsuarios:
            idPefil = bd.consultaConParametros(sqlPerfisUsuario, usuario[0])
            descripcionPerfil = bd.consultaConParametros(sqlPerfis, idPefil[0][0])
            elemento = list(usuario)
            elemento.append(idPefil[0][0])
            elemento.append(descripcionPerfil[0][0])
            print(elemento)
            modelo.append(elemento)


        caixaV.pack_start(tryPerfilesUsuarios,True,True,0)

        self.add(caixaV)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
