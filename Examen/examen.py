import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from conexionBD import ConexionBD


class Aplicacion(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Exame 13-04-2023")
        self.set_border_width(10)

        boxTop = Gtk.VBox(orientation=Gtk.Orientation.VERTICAL, spacing = 2)
        usuarios = Gtk.Frame(label="Usuarios")

        boxDni = Gtk.HBox(orientation=Gtk.Orientation.HORIZONTAL, spacing = 2)
        lblDni = Gtk.Label(label="Dni")
        cmbDni = Gtk.ComboBox()

        modelo = Gtk.ListStore(str)

        bd = ConexionBD("/home/dam2a/Escritorio/Python/DiExamen/perfisUsuarios.bd")
        bd.conectaBD()
        bd.creaCursor()
        sqlUsuarios = "SELECT dni FROM usuarios"
        dniUsuarios = bd.consultaSenParametros(sqlUsuarios)


        listaDni = list()

        for dni in dniUsuarios:
            listaDni.append(dni)

        print(listaDni)
        """cmbDni.add(listaDni)"""

        boxDni.add(lblDni)
        boxDni.add(cmbDni)

        boxNome = Gtk.HBox(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        lblNome = Gtk.Label(label="Nome")
        txtNome = Gtk.Entry()
        boxNome.add(lblNome)
        boxNome.add(txtNome)

        boxTop.add(boxDni)
        boxTop.add(boxNome)
        usuarios.add(boxTop)

        boxDown = Gtk.VBox(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        perfisUsuario = Gtk.Frame(label="Perfis usuario")

        box3buttons = Gtk.VBox(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        btnNovo = Gtk.Button(label="Novo")
        btnEdit = Gtk.Button(label="Editar")
        btnBorrar = Gtk.Button(label="Borrar")
        box3buttons.add(btnNovo)
        box3buttons.add(btnEdit)
        box3buttons.add(btnBorrar)

        boxNomeP = Gtk.HBox(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        lblNomeP = Gtk.Label(label="Nome Perfil")
        txtNomeP = Gtk.Entry()
        lblP = Gtk.Label(label="Permisos")
        boxNomeP.add(lblNomeP)
        boxNomeP.add(txtNomeP)
        boxNomeP.add(lblP)

        boxDesc = Gtk.HBox(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        lblDesc = Gtk.Label(label="Descripcion")
        txtDesc = Gtk.Entry()
        cmbDesc = Gtk.ComboBox()
        boxDesc.add(lblDesc)
        boxDesc.add(txtDesc)
        boxDesc.add(cmbDesc)

        boxDown.add(box3buttons)
        boxDown.add(boxNomeP)
        boxDown.add(boxDesc)
        perfisUsuario.add(boxDown)

        vboxMain = Gtk.VBox()
        vboxMain.add(usuarios)
        vboxMain.add(perfisUsuario)



        self.add(vboxMain)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()