import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from conexionBD import ConexionBD
from reportlab.platypus import (SimpleDocTemplate,
                                PageBreak,
                                Image,
                                Spacer,
                                Paragraph,
                                Table,
                                TableStyle)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

class Exame(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exame 13-04-2023")
        self.set_border_width(10)

        builder = Gtk.Builder()
        builder.add_from_file("Aplicacionsperfis.glade")


        hboxSuperior = Gtk.HBox()
        frmUsuarios = Gtk.Frame (label = "Usuarios")
        lblNome = Gtk.Label (label = "Nome")
        txtNome = Gtk.Entry ()
        lblDni = Gtk.Label(label = "Dni")
        self.txtDni = Gtk.Entry()
        self.txtDni.set_text("111111k")
        lblDepartamento = Gtk.Label (label = "Departamento")
        cmbDepartamento = Gtk.ComboBox()
        lblCorreoe = Gtk.Label(label = "Correoe")
        txtCorreoe = Gtk.Entry()
        chkActivo = Gtk.CheckButton (label = "Activo")
        hboxSuperior.add(frmUsuarios)
        hboxSuperior.add(lblNome)
        hboxSuperior.add(txtNome)
        hboxSuperior.add(lblDni)
        hboxSuperior.add(self.txtDni)
        hboxSuperior.add(lblDepartamento)
        hboxSuperior.add(cmbDepartamento)
        hboxSuperior.add(lblCorreoe)
        hboxSuperior.add(txtCorreoe)
        hboxSuperior.add(chkActivo)

        hboxInferior = Gtk.HBox()
        vboxIz = Gtk.VBox()
        vboxDer = Gtk.VBox()

        frmPerfis = Gtk.Frame (label = "Perfís aplicación")

        frAppper = builder.get_object("frAppper")
        self.entry1 = builder.get_object("entry1")
        self.entry2 = builder.get_object("entry2")
        self.entry3 = builder.get_object("entry3")
        self.entry4 = builder.get_object("entry4")
        self.entry5 = builder.get_object("entry5")
        vboxIz.add(frAppper)

        bd = ConexionBD("/home/dam2a/Escritorio/Python/PythonDI/DiEx/perfisUsuarios.bd")
        bd.conectaBD()
        bd.creaCursor()
        sqlNomePerfil = "SELECT nomePerfil FROM perfis"
        lPerfis = bd.consultaSenParametros(sqlNomePerfil)



        ntbPerfis = Gtk.Notebook()
        trvPerfis= Gtk.TreeView()
        trvTreeView = Gtk.TreeView()
        trvOperaciones = Gtk.TreeView()
        ntbPerfis.add(trvPerfis)
        ntbPerfis.add(trvTreeView)
        ntbPerfis.add(trvOperaciones)
        frmPerfis.add(ntbPerfis)

        vboxDer.add(frmPerfis)

        hboxInferior.add(vboxIz)
        hboxInferior.add(vboxDer)

        hboxBoton = Gtk.HBox()
        self.button = Gtk.Button(label="Xenerar informe")
        self.button.connect("clicked", self.on_btnInforme_clicked)
        hboxBoton.add(self.button)

        vboxMain = Gtk.VBox()
        vboxMain.add(hboxSuperior)
        vboxMain.add(hboxInferior)
        vboxMain.add(hboxBoton)

        self.add(vboxMain)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_btnInforme_clicked(self, bd):
        doc = SimpleDocTemplate("tablaExamen.pdf", pageSize=4)
        op = []

        dni = self.txtDni.get_text()

        bd = ConexionBD("perfisUsuarios.bd")
        bd.conectaBD()
        bd.creaCursor()
        sqlDatosUsuario = "SELECT nome,departamento,correoe,activo FROM usuarios WHERE dni=?"
        sqlPermisos = "SELECT permiso, idPerfil FROM perfisUsuario WHERE dniUsuario=?"
        lDatosUsuario = bd.consultaConParametros(sqlDatosUsuario,dni)
        listaDatos = list()
        listaPermisos = list()
        for datos in lDatosUsuario:
            listaDatos.append(datos)
            lPermisos = bd.consultaConParametros(sqlPermisos,dni)
            for permisos in lPermisos:
                listaPermisos.append(permisos)

        print(listaPermisos[0][1])

        sqlPerfiles = "SELECT nomePerfil FROM perfis WHERE idPefil=?"
        lPerfis = bd.consultaConParametros(sqlPerfiles,listaPermisos[0][1])
        listaPerfiles = list()
        for perfiles in lPerfis:
            listaPerfiles.append(perfiles)

        print(listaPerfiles[0][0])

        data = [('DNI', 'Nome','Departamento','Correo','Activo','Perfis','Permisos'),
                (dni, listaDatos[0][0],listaDatos[0][1],listaDatos[0][2],listaDatos[0][3],listaPerfiles[0][0],listaPermisos[0][0])]

        table = Table(data, colWidths=87, rowHeights=20)


        op.append(table)

        doc.build(op)


if __name__=="__main__":
    Exame()
    Gtk.main()