from PyQt5 import uic
from PyQt5 import QtWidgets

from DAL.DataProxy import DataProxy


class UiAddBookRent(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        uic.loadUi('Ui/UiAddBookRent.ui', self)

        self.data_proxy = DataProxy()
        self.parent = parent

        self.books = self.all_books()
        self.renters = self.all_renters()

        self.books_comboBox.insertItems(0, self.books)
        self.renters_comboBox.insertItems(0, self.renters)

        self.buttonBox.accepted.connect(self.accept_)
        self.buttonBox.rejected.connect(self.reject)

        self.setModal(True)

        self.show()

    def all_books(self):
        all_books = self.data_proxy.get_all_books()
        books = []
        for each_book in all_books:
            books.append(each_book['title'])
        return books

    def all_renters(self):
        all_renters = self.data_proxy.get_all_renters()
        renters = []
        for each_renter in all_renters:
            renters.append('{0} {1}'.format(each_renter['name'], each_renter['surname']))
        return renters

    def accept_(self):

        def save_book(length, date_, book, renter):
            rented_book = {
                'renting_person': renter,
                'book': book,
                'rented_date': date_.toString('yyyy-MM-dd'),
                'rental_days': length,
            }
            self.parent.rented_books_model.insertRows(data=self.data_proxy.put_rented_book(rented_book))

        try:
            length = int(self.length_input.text())
            date_ = self.calendar.selectedDate()
            renter = self.renters_comboBox.currentText()
            book = self.books_comboBox.currentText()
            save_book(length, date_, book, renter)
            self.close()
            self.parent.update_counters()
        except ValueError as e:
            self.length_input.setStyleSheet("border: 1px solid red;")
