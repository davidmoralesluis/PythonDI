
from PyQt6.QtCore import QAbstractListModel, Qt
from PyQt6.QtGui import *





tick = QImage('tick.png')

class modeloLista(QAbstractListModel):
    def __init__(self, listaTarefa=None):
        super().__init__()
        self.listaTarefa =listaTarefa or []

    def data(self, indice, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            estado,texto = self.listaTarefa[indice.row()]
            return texto


        if rol == Qt.ItemDataRole.DecorationRole:
            estado,texto = self.listaTarefa[indice.row()]

            if estado:
                return tick


    def rowCount(self, index):
        return  len(self.listaTarefa)