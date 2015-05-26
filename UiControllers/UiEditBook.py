from .UiAddBook import UiAddBook


class UiEditBook(UiAddBook):
    def __init__(self, parent, index, book):
        super().__init__(parent)

        self.index = index
        self.book = book

        self.title = 'Edit Book'
        self.title_input.setText(book['title'])
        self.isbn_input.setText(book['isbn'])

    def accept_(self):
        if self.title_input.text() and self.isbn_input.text():
            book = {
                'title': self.title_input.text(),
                'isbn': self.isbn_input.text()
            }
            self.parent.books_model.setData(self.index, data=self.data_proxy.edit_book(self.book['id'], book))
            # TODO: show message on error
        self.close()
