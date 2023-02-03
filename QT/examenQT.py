import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QListWidget, QPushButton, QComboBox, QLineEdit,
                             QRadioButton, QHBoxLayout, QVBoxLayout, QWidget)



class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exame 12-12_2022")

        BoxMain = QVBoxLayout()
        line1= QHBoxLayout()
        line2= QHBoxLayout()
        line3= QHBoxLayout()
        line4 = QHBoxLayout()
        line5 = QHBoxLayout()
        line6leftTop = QHBoxLayout()
        line6left= QVBoxLayout()
        line6right= QVBoxLayout()
        line6 = QHBoxLayout()
        line7 = QHBoxLayout()
        line8= QHBoxLayout()

        lblNome = QLabel("Nome")
        lblApelido = QLabel("Apelido")
        lblTratamento = QLabel("Tratamento")
        lblUsuario = QLabel("Usuario")



        self.txtNome = QLineEdit()
        self.txtApelido = QLineEdit()
        self.txtTratamento = QLineEdit()
        txtUsuario = QLineEdit()
        lblFormato = QLabel("Formato")
        self.cmbFormato = QComboBox()
        self.cmbFormato.addItems(("Html", "Texto plano", "Personalizado"))
        self.cmbFormato.currentTextChanged.connect(self.cambiarFormato)

        lblDireccionC = QLabel("Dirección de correo")
        self.txtDireccionC = QLineEdit()

        self.lstDireccionC = QListWidget()


        self.btnEngadir = QPushButton("Engadir")
        self.btnEngadir.clicked.connect(self.engadir)
        btnEditar = QPushButton("Editar")
        self.btnBorrar = QPushButton("Borrar")
        self.btnBorrar.clicked.connect(self.clear)
        btnPorDefecto = QPushButton("Por Defecto")

        lblFormato2 = QLabel("Formato de correo:")

        self.rbtHtml = QRadioButton("HTML")
        self.rbtHtml.clicked.connect(self.radioSelected)

        self.rbtTextoPlano = QRadioButton ("Texto Plano")
        self.rbtTextoPlano.clicked.connect(self.radioSelected)

        self.rbtPersonalizado = QRadioButton ("Personalizado")
        self.rbtPersonalizado.clicked.connect(self.radioSelected)

        btnAceptar = QPushButton("Aceptar")
        btnCancelar = QPushButton("Cancelar")


        line1.addWidget(lblNome)
        line1.addWidget(lblTratamento)
        line2.addWidget(self.txtNome)
        line2.addWidget(self.txtTratamento)
        line3.addWidget(lblApelido)
        line3.addWidget(lblUsuario)
        line4.addWidget(self.txtApelido)
        line4.addWidget(txtUsuario)
        line5.addWidget(lblFormato)
        line5.addWidget(self.cmbFormato)

        line6leftTop.addWidget(lblDireccionC)
        line6leftTop.addWidget(self.txtDireccionC)
        line6left.addLayout(line6leftTop)
        line6left.addWidget(self.lstDireccionC)
        line6right.addWidget(self.btnEngadir)
        line6right.addWidget(btnEditar)
        line6right.addWidget(self.btnBorrar)
        line6right.addWidget(btnPorDefecto)
        line6.addLayout(line6left)
        line6.addLayout(line6right)

        line7.addWidget(self.rbtHtml)
        line7.addWidget(self.rbtTextoPlano)
        line7.addWidget(self.rbtPersonalizado)
        line8.addWidget(btnCancelar)
        line8.addWidget(btnAceptar)

        BoxMain.addLayout(line1)
        BoxMain.addLayout(line2)
        BoxMain.addLayout(line3)
        BoxMain.addLayout(line4)
        BoxMain.addLayout(line5)
        BoxMain.addLayout(line6)
        BoxMain.addWidget(lblFormato2)
        BoxMain.addLayout(line7)
        BoxMain.addLayout(line8)


        widget = QWidget()
        widget.setLayout(BoxMain)
        self.setCentralWidget(widget)

        self.show()

    def cambiarFormato(self, formato):
        print("formato seleccionado: " + formato)


    def radioSelected(self):
        if self.rbtHtml.isChecked():
            #self.cmbFormato.setCurrentText(self.rbtHtml.text())
            #self.cmbFormato.setEditText(self.rbtHtml.text())
            self.cambiarFormato(self.rbtHtml.text())

        if self.rbtTextoPlano.isChecked():
            # self.cmbFormato.setCurrentText(self.rbtTextoPlano.text())
            # self.cmbFormato.setEditText(self.rbtTextoPlano.text())
            self.cambiarFormato(self.rbtTextoPlano.text())

        if self.rbtPersonalizado.isChecked():
            # self.cmbFormato.setCurrentText(self.rbtPersonalizado.text())
            # self.cmbFormato.setEditText(self.rbtPersonalizado.text())
            self.cambiarFormato(self.rbtPersonalizado.text())

    def engadir(self):
        self.lstDireccionC.addItem(str(self.txtTratamento.text())+str(", ")+str(self.txtNome.text())+str(", ")+str(self.txtApelido.text())+str(", ")+str(self.txtDireccionC.text()))

    def clear(self):

        itemSelected = self.lstDireccionC.selectedItems()
        print(itemSelected[0])
        #self.lstDireccionC.takeItem(itemSelected[0])



if __name__=="__main__":

    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()

    aplicacion.exec()