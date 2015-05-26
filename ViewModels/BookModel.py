from .BasicDataModel import BasicDataModel


class BookModel(BasicDataModel):
    def __init__(self, parent, *args):
        self.headers = ["Id", "Title", "ISBN"]
        super().__init__(parent, self.data_proxy.get_all_books())
