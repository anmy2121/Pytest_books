import collections
from src.services.book_fetcher_service import BookFetcherService
from src.services.book_service import BookService


def test_list_book_ids(monkeypatch):
    # we define a function that will replace the existing function
    # instead of calling the mocked server, we use a controlled dataset
    def mock_get_books(*args):
        return [
            {
                "id": "aaa-001",
                "name": "Origine",
                "author": {"firstname": "Dan", "lastname": "Brown"},
            },
            {
                "id": "aaa-002",
                "name": "Anges & Démons",
                "author": {"firstname": "Dan", "lastname": "Brown"},
            },
            {
                "id": "aaa-003",
                "name": "Ulysses",
                "author": {"firstname": "James", "lastname": "Joyce"},
            },
        ]

    monkeypatch.setattr(BookFetcherService, "get_books", mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())
    ids = book_service.list_books_ids()

    assert ids == ["aaa-001", "aaa-002", "aaa-003"]


def test_list_authors(monkeypatch):
    def mock_get_books(*args):
        return [
            {
                "id": "aaa-001",
                "name": "Origine",
                "author": {"firstname": "Dan", "lastname": "Brown"},
            },
            {
                "id": "aaa-002",
                "name": "Anges & Démons",
                "author": {"firstname": "Dan", "lastname": "Brown"},
            },
            {
                "id": "aaa-003",
                "name": "Ulysses",
                "author": {"firstname": "James", "lastname": "Joyce"},
            },
        ]

    monkeypatch.setattr(BookFetcherService, "get_books", mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())
    authors = book_service.list_books_authors()

    # assert authors == ['Brown Dan', 'Joyce James']
    assert collections.Counter(authors) == collections.Counter(
        ["Brown Dan", "Joyce James"]
    )


def test_list_names(monkeypatch):
    def mock_get_books(*args):
        return [
            {
                "id": "aaa-001",
                "name": "Origine",
                "author": {"firstname": "Dan", "lastname": "Brown"},
            },
            {
                "id": "aaa-002",
                "name": "Anges & Démons",
                "author": {"firstname": "Dan", "lastname": "Brown"},
            },
            {
                "id": "aaa-003",
                "name": "Ulysses",
                "author": {"firstname": "James", "lastname": "Joyce"},
            },
        ]

    monkeypatch.setattr(BookFetcherService, "get_books", mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())
    names = book_service.list_books_names()

    assert names == ["Origine", "Anges & Démons", "Ulysses"]


# cas 2
def test_list_with_no_book(monkeypatch):
    def mock_get_books(*args):
        return []


# cas 3
def test_list_only_one_book(monkeypatch):
    def mock_get_books(*args):
        return [
            {
                "id": "aaa-003",
                "name": "Ulysses",
                "author": {"firstname": "James", "lastname": "Joyce"},
            }
        ]

    monkeypatch.setattr(BookFetcherService, "get_books", mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())
    only_one_book = book_service.list_books_ids()

    assert only_one_book == ["aaa-003"]


# cas 4


def test_list_with_no_author_s_firstname(monkeypatch):
    def mock_get_books(*args):
        return [{"id": "aaa-003", "name": "Ulysses", "author": {"lastname": "Joyce"}}]

    monkeypatch.setattr(BookFetcherService, "get_books", mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())
    with_no_author_s_firstname = book_service.list_books_ids()

    assert with_no_author_s_firstname == ["aaa-003"]


# cas 5
def test_list_with_no_author(monkeypatch):
    def mock_get_books(*args):
        return [{"id": "aaa-001", "name": "Origine"}]

    monkeypatch.setattr(BookFetcherService, "get_books", mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())
    with_no_author = book_service.list_books_ids()

    assert with_no_author == ["aaa-001"]
