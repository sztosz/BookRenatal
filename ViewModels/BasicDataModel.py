import operator

from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex

from DAL.DataProxy import DataProxy


class BasicDataModel(QAbstractTableModel):
    data_proxy = DataProxy()

    def __init__(self, parent, data_, *args):
        super().__init__(parent)
        self._data = data_

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(self.headers)

    def data(self, index, role=None, whole_row=False):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        if whole_row:
            return self._data[index.row()]
        return self._data[index.row()][self.headers[index.column()].lower()]

    def headerData(self, column, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headers[column]
        return None

    def sort(self, column, order=None):
        self.layoutAboutToBeChanged.emit()
        self._data = sorted(self._data, key=operator.itemgetter(self.headers[column]))
        if order == Qt.DescendingOrder:
            self._data.reverse()
        self.layoutChanged.emit()

    def insertRows(self, row=0, parent_index=None, data=None, *args, **kwargs):
        self.beginInsertRows(QModelIndex(), 0, 0)
        if data:
            self._data.append(data)
        self.endInsertRows()

    def setData(self, index, data, role=Qt.EditRole):
        if not index.isValid() or role != Qt.EditRole:
            return False
        self._data[index.row()] = data
        self.dataChanged.emit(index, index)

    def get_data(self, index, role=Qt.DisplayRole):  # TODO: Check usage, to be thrown away probably
        if not index.isValid():
            return None
        if index.row() > len(self._data):
            return None
        if role == Qt.DisplayRole or role == Qt.EditRole:
            return self._data[index.row()]
        return None
