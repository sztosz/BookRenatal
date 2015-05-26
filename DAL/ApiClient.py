import requests


class ApiClient():
    def __init__(self, url):
        self.url = url
        pass

    def get_all_books(self):
        response = requests.get(self.url + '/books/')
        return response.json()

    def get_book(self, _id):
        pass

    def edit_book(self, _id, book):
        response = requests.put(self.url + '/books/' + str(_id) + '/', book)
        return response.json()

    def put_book(self, book):
        response = requests.post(self.url + '/books/', book)
        return response.json()

    def delete_book(self, _id):
        response = requests.delete(self.url + '/books/' + str(_id) + '/')
        if response.status_code == 204:
            return True
        return False

    def get_all_renters(self):
        response = requests.get(self.url + '/renting-persons/')  # TODO: Change to /renters/ (also in API)
        return response.json()

    def get_renter(self, _id):
        pass

    def edit_renter(self, _id, renter):
        response = requests.put(self.url + '/renting-persons/' + str(_id) + '/', renter)
        return response.json()

    def put_renter(self, renter):
        response = requests.post(self.url + '/renting-persons/', renter)  # TODO: Change to /renters/ (also in API)
        return response.json()

    def delete_renter(self, _id):
        response = requests.delete(self.url + '/renting-persons/' + str(_id) + '/')
        if response.status_code == 204:
            return True
        return False

    def get_all_rented_books(self):
        response = requests.get(self.url + '/books-rented/')  # TODO: Change to /rented-books/ (also in API)
        # print(response.json())
        return response.json()

    def get_rented_book(self, _id):
        pass

    def put_rented_book(self, rented_book):
        response = requests.post(self.url + '/books-rented/', rented_book)
        return response.json()

    def delete_rented_book(self, _id):
        response = requests.delete(self.url + '/books-rented/' + str(_id) + '/')
        if response.status_code == 204:
            return True
        return False
