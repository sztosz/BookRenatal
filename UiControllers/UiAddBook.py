from PyQt5 import uic
from PyQt5 import QtWidgets

from DAL.DataProxy import DataProxy


class UiAddBook(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        uic.loadUi('Ui/UiAddBook.ui', self)

        self.data_proxy = DataProxy()
        self.parent = parent
        self.buttonBox.accepted.connect(self.accept_)
        self.buttonBox.rejected.connect(self.reject)

        self.setModal(True)

        self.show()

    def accept_(self):
        if self.title_input.text() and self.isbn_input.text():
            book = {
                'title': self.title_input.text(),
                'isbn': self.isbn_input.text()
            }
            self.parent.books_model.insertRows(data=self.data_proxy.put_book(book))  # TODO: show message on error
            self.close()
            self.parent.update_books_count()
