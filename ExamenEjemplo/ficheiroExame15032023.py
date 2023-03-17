import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from conexionBD import ConexionBD

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table

class Exame(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exame 15-04-2023")
        self.set_border_width(10)

        builder = Gtk.Builder()
        builder.add_from_file("usuarios_fame.glade")

        frm_usuarios = builder.get_object("frm_usuarios")
        self.dni_cbm = builder.get_object("dni_cmb")
        self.nome_label = builder.get_object("nome_entry")

        self.db = ConexionBD("perfisUsuarios.bd")
        self.db.conectaBD()
        self.db.creaCursor()

        query_dni = "select dni from usuarios"

        dnis = self.db.consultaSenParametros(query_dni)

        print("------")
        print(dnis)
        print("------")
        for i, dni in enumerate(dnis):
            self.dni_cbm.append_text(dnis[i][0])

        self.dni_cbm.connect("changed", self.dni_cmb_changed)

        frmPerfis = Gtk.Frame(label="Perfís usuario")

        model = Gtk.ListStore(str, str, str)
        self.trvPerfis = Gtk.TreeView(model=model)

        crt = Gtk.CellRendererText()
        col1 = Gtk.TreeViewColumn("Nome perfil", crt, text=0)
        col2 = Gtk.TreeViewColumn("Decricion", crt, text=1)
        col3 = Gtk.TreeViewColumn("Permisos", crt, text=2)

        self.trvPerfis.append_column(col1)
        self.trvPerfis.append_column(col2)
        self.trvPerfis.append_column(col3)

        caixaVBotons = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)

        btnNovo = Gtk.Button(label="Novo")
        btnEditar = Gtk.Button(label="Editar")
        btnBorrar = Gtk.Button(label="Borrar")

        caixaVBotons.add(btnNovo)
        caixaVBotons.add(btnEditar)
        caixaVBotons.add(btnBorrar)

        frm_h_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        frm_h_box.add(self.trvPerfis)
        frm_h_box.add(caixaVBotons)

        frmPerfis.add(frm_h_box)

        lblNomePerfil = Gtk.Label(label="Nome perfíl")
        txtNomePerfil = Gtk.Entry()
        lblPermisos = Gtk.Label(label="Permisos")

        btm_h_box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        btm_h_box1.add(lblNomePerfil)
        btm_h_box1.add(txtNomePerfil)
        btm_h_box1.add(lblPermisos)

        lblDescripcionPerfil = Gtk.Label(label="Descripción")
        txtDescripcionPerfil = Gtk.Entry()
        cmbPermisos = Gtk.ComboBox()

        btm_h_box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        btm_h_box2.add(lblDescripcionPerfil)
        btm_h_box2.add(txtDescripcionPerfil)
        btm_h_box2.add(cmbPermisos)

        pdf_btn = Gtk.Button(label="Generar informe")
        pdf_btn.connect("clicked", self.on_pdf_clicked)

        main_v_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        main_v_box.add(frm_usuarios)
        main_v_box.add(frmPerfis)
        main_v_box.add(btm_h_box1)
        main_v_box.add(btm_h_box2)
        main_v_box.add(pdf_btn)

        self.add(main_v_box)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def dni_cmb_changed(self, cmb):
        dni = self.dni_cbm.get_active_text()

        nome_query = "select nome from usuarios where dni=?"
        nome = self.db.consultaConParametros(nome_query, dni)
        self.nome_label.set_text(nome[0][0])

        idPerfil_permisos = "select idPerfil, permiso from perfisUsuario where dniUsuario=?"
        query_perfis = "select nomePerfil, descricion from perfis where idPefil=?"

        idPerfil_permisos = self.db.consultaConParametros(idPerfil_permisos, dni)
        datos_perfil = self.db.consultaConParametros(query_perfis, idPerfil_permisos[0][0])
        print(datos_perfil[0][0], datos_perfil[0][1], idPerfil_permisos[0][1])

        model = self.trvPerfis.get_model()
        model.clear()
        permisos = ""
        if idPerfil_permisos[0][1] == 0:
            permisos = "Sen permisos"
        elif idPerfil_permisos[0][1] == 1:
            permisos = "Lectura"
        elif idPerfil_permisos[0][1] == 2:
            permisos = "Lectura y escritura"
        model.append([datos_perfil[0][0], datos_perfil[0][1], permisos])

    def on_pdf_clicked(self, row):
        dni = self.dni_cbm.get_active_text()

        doc = SimpleDocTemplate("InformeExamen.pdf", pagesize=A4)

        query_usuario = "select nome, correoe from usuarios where dni=?"

        datos_usuario = self.db.consultaConParametros(query_usuario, dni)

        data = ([("Nome", "DNI", "Correo",)])

        for row in datos_usuario:
            print(row[0])
            data.append([row[0], dni, row[1]])

        table = Table(data)

        doc.build([table])


if __name__ == "__main__":
    Exame()
    Gtk.main()
