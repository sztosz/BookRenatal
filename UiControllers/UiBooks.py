from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSortFilterProxyModel, QRegExp, Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMenu, QAbstractItemView

from DAL.DataProxy import DataProxy
from .UiAddBook import UiAddBook
from .UiEditBook import UiEditBook
from ViewModels.BookModel import BookModel


class UiBooks(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui/UiBooks.ui', self)

        self.add_book_window = None
        self.edit_book_window = None

        self.data_proxy = DataProxy()

        self.populate_model()

        self.search_comboBox.addItems(self.books_model.headers)

        self.books_count.setText(str(self.books_model.rowCount(self)))

        self.add_new_book_button.clicked.connect(self.add_new_book_button_clicked)
        self.search_comboBox.currentIndexChanged.connect(self.change_search_column)
        self.search_input.textChanged.connect(self.search)
        self.books_model.dataChanged.connect(self.update_books_count)
        self.close_button.clicked.connect(self.close)

        self.books_QTableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.books_QTableView.customContextMenuRequested.connect(self.show_context_menu)
        self.books_QTableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.setModal(True)

        self.books_QTableView.resizeColumnsToContents()
        # self.books_QTableView.setSortingEnabled(True)  # Shouldn't be enabled, screws indexes badly, and needs tons of
        # boiler plate code to work.
        self.show()

    def populate_model(self):
        self.books_model = BookModel(self.books_QTableView)
        self.books_proxy_model = QSortFilterProxyModel(self)
        self.books_proxy_model.setSourceModel(self.books_model)
        self.books_QTableView.setModel(self.books_proxy_model)

    def add_new_book_button_clicked(self):
        self.add_book_window = UiAddBook(self)

    def change_search_column(self, index):
        self.books_proxy_model.setFilterKeyColumn(index)

    def search(self, text):
        search = QRegExp(text, Qt.CaseInsensitive, QRegExp.RegExp)
        self.books_proxy_model.setFilterRegExp(search)

    def update_books_count(self):
        self.books_count.setText(str(self.books_model.rowCount(self)))

    def show_context_menu(self, event):
        index = self.books_QTableView.indexAt(event)
        if index.isValid():
            menu = QMenu(self)
            menu.addAction('Edit Book', lambda: self.edit_book(index))
            menu.addAction('Remove Book', lambda: self.remove_book(index))
            menu.popup(QCursor.pos())

    def edit_book(self, index):
        self.edit_book_window = UiEditBook(self, index, self.books_model.get_data(index))

    def remove_book(self, index):
        book_id = self.books_model.get_data(index)['id']
        if self.data_proxy.delete_book(book_id):
            self.populate_model()
            self.update_books_count()
