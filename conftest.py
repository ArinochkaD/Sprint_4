import pytest

from main import BooksCollector

@pytest.fixture
def multi_collector():
    collector = BooksCollector()

    first_book = 'Оно'
    second_book = 'Гарри Поттер'
    third_book = 'Шерлок Холмс'

    collector.add_new_book(first_book)
    collector.add_new_book(second_book)
    collector.add_new_book(third_book)

    horror = collector.genre[1]
    fantasy = collector.genre[0]
    detective = collector.genre[2]

    collector.set_book_genre(first_book, horror)
    collector.set_book_genre(second_book, fantasy)
    collector.set_book_genre(third_book, detective)

    return collector
