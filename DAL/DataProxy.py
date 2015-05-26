from .ApiClient import ApiClient


class DataProxy():
    url = 'http://127.0.0.1:8000/api/v1'
    data_source = ApiClient(url)

    def get_all_books(self):
        return self.data_source.get_all_books()

    def get_book(self, _id):
        pass

    def edit_book(self, _id, book):
        return self.data_source.edit_book(_id, book)

    def put_book(self, book):
        return self.data_source.put_book(book)

    def delete_book(self, _id):
        return self.data_source.delete_book(_id)

    def get_all_renters(self):
        return self.data_source.get_all_renters()

    def get_renter(self, _id):
        pass

    def edit_renter(self, _id, renter):
        return self.data_source.edit_renter(_id, renter)

    def put_renter(self, renter):
        return self.data_source.put_renter(renter)

    def delete_renter(self, _id):
        return self.data_source.delete_renter(_id)

    def get_all_rented_books(self):
        return self.data_source.get_all_rented_books()

    def get_rented_book(self, _id):
        pass

    def put_rented_book(self, rented_book):
        return self.data_source.put_rented_book(rented_book)

    def delete_rented_book(self, _id):
        return self.data_source.delete_rented_book(_id)
