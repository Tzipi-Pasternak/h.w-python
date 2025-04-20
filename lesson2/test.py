import pytest
from library import Library
from book import Book


def test_add_book():
    library = Library()
    book = Book("The Little Prince", "Antoine de Saint-Exupéry")
    library.add_book(book)
    assert book in library.books


def test_add_user():
    library = Library()
    library.add_user("Tzipi")
    assert "Tzipi" in library.users


def test_check_out_book_success():
    library = Library()
    user = "alice"
    book = Book("Harry Potter", "J.K. Rowling")
    library.add_user(user)
    library.add_book(book)
    library.check_out_book(user, book)
    assert book.is_checked_out is True
    assert library.checked_out_books[user] == book


def test_return_book_success():
    library = Library()
    user = "bob"
    book = Book("The Hobbit", "J.R.R. Tolkien")
    library.add_user(user)
    library.add_book(book)
    library.check_out_book(user, book)
    library.return_book(user, book)
    assert book.is_checked_out is False
    assert user not in library.checked_out_books


def test_search_books_exact_match():
    library = Library()
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("The Grapes of Wrath", "John Steinbeck")
    book3 = Book("Harry Potter", "J.K. Rowling")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    results = library.search_books("The Great Gatsby")
    assert len(results) == 1
    assert results[0] == book1


def test_check_out_nonexistent_book():
    library = Library()
    user = "dana"
    book = Book("Ghost Book", "No One")
    library.add_user(user)
    with pytest.raises(ValueError, match="is not in the library"):
        library.check_out_book(user, book)


def test_check_out_by_unregistered_user():
    library = Library()
    book = Book("1984", "George Orwell")
    library.add_book(book)
    with pytest.raises(ValueError, match="is not registered"):
        library.check_out_book("nonexistent_user", book)


def test_illegal_values_book_and_user():
    with pytest.raises(ValueError, match="Title and author must not be empty"):
        Book("", "Author Name")
    library = Library()
    with pytest.raises(ValueError, match="Username must not be empty"):
        library.add_user("")


def test_unexpected_values_book_and_user():
    library = Library()
    book = Book("###1234@@@", "!!Author!!")
    library.add_book(book)
    assert book in library.books
    username = "1234_user$%^"
    library.add_user(username)
    assert username in library.users