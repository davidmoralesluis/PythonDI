import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from modeloLista import modeloLista

from reportlab.platypus import SimpleDocTemplate,Table

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        caixaV = QVBoxLayout()

        self.modelo = modeloLista([(False,"Miña primera tarea")])
        self.lstTarefas = QListView()
        self.lstTarefas.setModel(self.modelo)

        caixaV.addWidget(self.lstTarefas)

        caixaH = QHBoxLayout()
        caixaV.addLayout(caixaH)
        self.btnBorrar=QPushButton("Borrar")
        self.btnBorrar.pressed.connect(self.on_btnBorrar)
        caixaH.addWidget(self.btnBorrar)

        self.btnFeito=QPushButton("Feito")
        self.btnFeito.pressed.connect(self.on_btnFeito)
        caixaH.addWidget(self.btnFeito)

        self.lneNovaTarefa = QLineEdit()
        self.lneNovaTarefa.returnPressed.connect(self.on_btnEngadir)
        self.lneNovaTarefa.setPlaceholderText("Escribe")
        caixaV.addWidget(self.lneNovaTarefa)

        self.btnEngadir = QPushButton("Engadir")
        self.btnEngadir.pressed.connect(self.on_btnEngadir)
        caixaV.addWidget(self.btnEngadir)

        self.btnPasarAPapel= QPushButton("Pasar a papel")
        self.btnEngadir.pressed.connect(self.on_btnPaserAPapel_pressed)
        caixaV.addWidget(self.btnPasarAPapel)

        contenedor = QWidget()
        contenedor.setLayout(caixaV)

        self.setCentralWidget(contenedor)

        self.show()

    def on_btnEngadir(self):
        novaTarefa=self.lneNovaTarefa.text()
        novaTarefa = novaTarefa.strip()

        if novaTarefa:
            self.modelo.listaTarefa.append((False, novaTarefa))
            self.modelo.layoutChanged.emit()
            self.lneNovaTarefa.setText("")


    def on_btnBorrar(self):
        indices = self.lstTarefas.selectedIndexes()

        if indices:
            indice = indices[0]
            del self.modelo.listaTarefa[indice.row()]
            # self.modelo.ListaTarefas.remove(self.modelo.listaTrefas[indice.row()])
            self.modelo.layoutChanged.emit()
            self.lstTarefas.clearSelection()

    def on_btnFeito(self):
        indices = self.lstTarefas.selectedIndexes()

        if indices:
            indice = indices[0]
            fila = indice.row()
            estado, descripcion =self.modelo.listaTarefa[fila]
            self.modelo.listaTarefa[fila]=(True, descripcion)
            self.modelo.dataChanged.emit()
            self.lstTarefas.clearSelection()

    def on_btnPaserAPapel_pressed(self):
        doc = SimpleDocTemplate('exemploT.pdf', pagesize=A4)
        operacions = []

        datos = [('', 'Ventas', 'Compras'),
                 ('Xaneiro', 300, 500),
                 ('Febreiro', -400, 500),
                 ('Marzo', 30, 2000)]

        taboa = Table(datos, colWidths=100, rowHeights=30)

        estilo = ([
            ('TEXTCOLOR', (0, 1), (0, -1), colors.blue),
            ('TEXTCOLOR', (1, 1), (2, -1), colors.green),
            ('BACKGROUND', (1, 1), (-1, -1), colors.lightgreen),
            ('BOX', (1, 1), (-1, -1), 1.5, colors.gray),
            ('INNERGRID', (1, 1), (-1, -1), 1, colors.lightgrey),
            ('VALING', (0, 0), (-1, -1), 'MIDDLE')
        ])
        taboa.setStyle(estilo)
        doc.build(taboa)



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()