from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSortFilterProxyModel, QRegExp, Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMenu, QAbstractItemView

from DAL.DataProxy import DataProxy
from .UiBooks import UiBooks
from .UiAddBookRent import UiAddBookRent
from .UiRenters import UiRenters
from ViewModels.RentedBookModel import RentedBookModel


class UiMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui/UiMainWindow.ui', self)

        self.books_window = None
        self.renters_window = None
        self.add_book_window = None
        self.add_new_book_rent_window = None

        self.data_proxy = DataProxy()

        self.populate_model()

        self.search_comboBox.addItems(self.rented_books_model.headers)

        self.update_counters()

        self.btn_show_books.clicked.connect(self.show_books_clicked)
        self.btn_show_renters.clicked.connect(self.show_renters_clicked)
        self.add_new_book_rent_button.clicked.connect(self.add_new_book_rent_button_clicked)
        self.search_comboBox.currentIndexChanged.connect(self.change_search_column)
        self.search_input.textChanged.connect(self.search)
        self.rented_books_model.dataChanged.connect(self.update_counters)

        self.rented_books_QTableView.resizeColumnsToContents()
        # self.rented_books_QTableView.setSortingEnabled(True)

        self.rented_books_QTableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.rented_books_QTableView.customContextMenuRequested.connect(self.show_context_menu)
        self.rented_books_QTableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.show()

    def populate_model(self):
        self.rented_books_model = RentedBookModel(self.rented_books_QTableView)
        self.rented_books_proxy_model = QSortFilterProxyModel(self)
        self.rented_books_proxy_model.setSourceModel(self.rented_books_model)
        self.rented_books_QTableView.setModel(self.rented_books_proxy_model)

    def show_books_clicked(self):
        self.books_window = UiBooks()

    def show_renters_clicked(self):
        self.renters_window = UiRenters()

    def add_new_book_rent_button_clicked(self):
        self.add_new_book_rent_window = UiAddBookRent(self)

    def change_search_column(self, index):
        self.rented_books_proxy_model.setFilterKeyColumn(index)

    def search(self, text):
        search = QRegExp(text, Qt.CaseInsensitive, QRegExp.RegExp)
        self.rented_books_proxy_model.setFilterRegExp(search)

    def show_context_menu(self, event):
        index = self.rented_books_QTableView.indexAt(event)
        if index.isValid():
            menu = QMenu(self)
            menu.addAction('Remove Rent', lambda: self.remove_rent(index))
            menu.popup(QCursor.pos())

    def remove_rent(self, index):
        rent_id = self.rented_books_model.get_data(index)['id']
        if self.data_proxy.delete_rented_book(rent_id):
            self.populate_model()
            self.update_counters()

    def update_rented_books_count(self):
        self.rented_books_count.setText(str(self.rented_books_model.rowCount(self)))

    def update_overdue_counter(self):
        self.overdue_books_count.setText(str(self.rented_books_model.overdue_counter()))

    def update_counters(self):
        self.update_rented_books_count()
        self.update_overdue_counter()
