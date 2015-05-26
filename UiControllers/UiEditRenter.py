from .UiAddRenter import UiAddRenter


class UiEditRenter(UiAddRenter):
    def __init__(self, parent, index, renter):
        super().__init__(parent)

        self.index = index
        self.renter = renter

        self.title = 'Edit Renter'
        self.name_input.setText(renter['name'])
        self.surname_input.setText(renter['surname'])
        self.pesel_input.setText(renter['pesel'])

    def accept_(self):
        if self.name_input.text() and self.surname_input.text() and self.pesel_input.text():
            renter = {
                'name': self.name_input.text(),
                'surname': self.surname_input.text(),
                'pesel': self.pesel_input.text()
            }
            self.parent.renters_model.setData(self.index, data=self.data_proxy.edit_renter(self.renter['id'], renter))
            # TODO: show message on error
        self.close()
