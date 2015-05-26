from .BasicDataModel import BasicDataModel


class RenterModel(BasicDataModel):
    def __init__(self, parent, *args):
        self.headers = ["Id", "Name", "Surname", "PESEL"]
        super().__init__(parent, self.data_proxy.get_all_renters())
