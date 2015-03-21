class Iterator(object):

    def has_next(self):
        pass

    def next(self):
        pass


class BookShelfIterator(Iterator):

    def __init__(self, bookshelf):
        self.bookshelf = bookshelf
        self.index = 0

    def has_next(self):
        if self.index < self.bookshelf.get_length():
            return True
        return False

    def next(self):
        book = self.bookshelf.get_book_at(self.index)
        self.index += 1
        return book


class Aggregate(object):

    def iterator(self):
        pass


class Book(object):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class BookShelf(Aggregate):

    def __init__(self):
        self.books = []

    def iterator(self):
        return BookShelfIterator(self)

    def get_book_at(self, index):
        return self.books[index]

    def append_book(self, book):
        self.books.append(book)

    def get_length(self):
        return len(self.books)
