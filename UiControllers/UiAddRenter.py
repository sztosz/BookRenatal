from PyQt5 import uic
from PyQt5 import QtWidgets

from DAL.DataProxy import DataProxy


class UiAddRenter(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        uic.loadUi('Ui/UiAddRenter.ui', self)

        self.data_proxy = DataProxy()
        self.parent = parent
        self.buttonBox.accepted.connect(self.accept_)
        self.buttonBox.rejected.connect(self.reject)

        self.setModal(True)

        self.show()

    def accept_(self):
        if self.name_input.text() and self.surname_input.text() and self.pesel_input.text():
            renter = {
                'name': self.name_input.text(),
                'surname': self.surname_input.text(),
                'pesel': self.pesel_input.text()
            }
            self.parent.renters_model.insertRows(data=self.data_proxy.put_renter(renter))  # TODO: show message on error
            self.close()
            self.parent.update_renters_count()
