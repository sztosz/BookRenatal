from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSortFilterProxyModel, QRegExp, Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMenu, QAbstractItemView

from DAL.DataProxy import DataProxy
from .UiAddRenter import UiAddRenter
from .UiEditRenter import UiEditRenter
from ViewModels.RenterModel import RenterModel


class UiRenters(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui/UiRenters.ui', self)

        self.add_renter_window = None
        self.edit_renter_window = None

        self.data_proxy = DataProxy()

        self.populate_model()

        self.search_comboBox.addItems(self.renters_model.headers)

        self.renters_count.setText(str(self.renters_model.rowCount(self)))

        self.add_new_renter_button.clicked.connect(self.add_new_renter_button_clicked)
        self.search_comboBox.currentIndexChanged.connect(self.change_search_column)
        self.search_input.textChanged.connect(self.search)
        self.renters_model.dataChanged.connect(self.update_renters_count)
        self.close_button.clicked.connect(self.close)

        self.renters_QTableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.renters_QTableView.customContextMenuRequested.connect(self.show_context_menu)
        self.renters_QTableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.setModal(True)

        self.renters_QTableView.resizeColumnsToContents()
        # self.renters_QTableView.setSortingEnabled(True)  # Shouldn't be enabled, screws indexes badly, and needs
        # tons of boiler plate code to work.
        self.show()

    def populate_model(self):
        self.renters_model = RenterModel(self.renters_QTableView)
        self.renters_proxy_model = QSortFilterProxyModel(self)
        self.renters_proxy_model.setSourceModel(self.renters_model)
        self.renters_QTableView.setModel(self.renters_proxy_model)

    def add_new_renter_button_clicked(self):
        self.add_renter_window = UiAddRenter(self)

    def change_search_column(self, index):
        self.renters_proxy_model.setFilterKeyColumn(index)

    def search(self, text):
        search = QRegExp(text, Qt.CaseInsensitive, QRegExp.RegExp)
        self.renters_proxy_model.setFilterRegExp(search)

    def update_renters_count(self):
        self.renters_count.setText(str(self.renters_model.rowCount(self)))

    def show_context_menu(self, event):
        index = self.renters_QTableView.indexAt(event)
        if index.isValid():
            menu = QMenu(self)
            menu.addAction('Edit Renter', lambda: self.edit_renter(index))
            menu.addAction('Remove Renter', lambda: self.remove_renter(index))
            menu.popup(QCursor.pos())

    def edit_renter(self, index):
        self.edit_renter_window = UiEditRenter(self, index, self.renters_model.get_data(index))

    def remove_renter(self, index):
        renter_id = self.renters_model.get_data(index)['id']
        if self.data_proxy.delete_renter(renter_id):
            self.populate_model()
            self.update_renters_count()
