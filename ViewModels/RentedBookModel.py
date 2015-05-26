from .BasicDataModel import BasicDataModel


class RentedBookModel(BasicDataModel):
    def __init__(self, parent, *args):
        # TODO: Correct headers, needs model or data_proxy rewrite!
        # self.headers = ["Id", "Renter", "Book", "Date Rented", "Days until return"]
        self.headers = ["Id", "Renting_Person", "Book", "Rented_date", "Rental_days", "Is_Overdue"]
        super().__init__(parent, self.data_proxy.get_all_rented_books())

    def overdue_counter(self):
        counter = 0
        for rent in self._data:
            if rent['is_overdue']:
                counter += 1
        return counter
