import sys

from PyQt6.QtCore import QAbstractTableModel, Qt
from PyQt6.QtWidgets import *

class ModeloTabla(QAbstractTableModel):
    def __init__(self, datos):
        super().__init__()
        self._datos = datos

    def data(self,indce,rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            return self._datos[indce.row()][indce.column()]

    def rowCount(self,indice):
        return len(self._datos)

    def columnCount(self,indice):
        return len(self._datos[0])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo QtTable")

        caixaV = QVBoxLayout()

        tableView = QTableView()
        caixaV.addWidget(tableView)

        contidoTaboa=[["Luns","Martes","Mercoles","Xoves","vernes","Sabado","Domingo"],
                      [3,5,6,5,3,0,0],
                      [3,2,5,7,2,3,0]
                      ]

        modelo = ModeloTabla(contidoTaboa)
        tableView.setModel(modelo)



        contenedor = QWidget()
        contenedor.setLayout(caixaV)

        self.setCentralWidget(contenedor)

        self.show()




app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()