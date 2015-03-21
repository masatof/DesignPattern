def test_iterator():
    from iterator import BookShelf, Book

    bookshelf = BookShelf()
    bookshelf.append_book(Book("Book_1"))
    bookshelf.append_book(Book("Book_2"))
    bookshelf.append_book(Book("Book_3"))
    bookshelf.append_book(Book("Book_4"))

    assert bookshelf.get_length() == 4  # books

    it = bookshelf.iterator()

    count = 1
    while it.has_next():
        book = it.next()
        assert book.get_name() == 'Book_' + str(count)
        count += 1

    assert count == 5
