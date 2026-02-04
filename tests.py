import pytest

from conftest import multi_collector
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # Проверка добавления двух книг.
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    # Проверка добавления жанра к книге.
    def test_set_book_genre_add_one_genre(self):
        collector = BooksCollector()

        book_name = 'Оно'

        # Добавили книгу.
        collector.add_new_book(book_name)

        book_genre = collector.genre[1]

        collector.set_book_genre(book_name, book_genre)

        assert collector.books_genre.get(book_name) == book_genre

    # Проверка получения жанров книгам.
    def test_get_book_genre_check_genres(self, multi_collector):
        horror = multi_collector.genre[1]
        fantastic = multi_collector.genre[0]
        detective = multi_collector.genre[2]

        assert multi_collector.get_book_genre('Оно') == horror
        assert multi_collector.get_book_genre('Гарри Поттер') == fantastic
        assert multi_collector.get_book_genre('Шерлок Холмс') == detective
    
    # Проверка отсутствия книг с возрастным рейтингом в списке книг для детей.
    def test_get_books_for_children(self, multi_collector):
        books_for_children = multi_collector.get_books_for_children()

        assert len(books_for_children) == 1 and books_for_children[0] == 'Гарри Поттер'

    # Проверка получения книг с определенным жанром.
    def test_get_books_with_specific_genre(self, multi_collector):
        multi_collector.add_new_book('Дюна')
        multi_collector.add_new_book('Кольцо')
        multi_collector.add_new_book('Под куполом')

        multi_collector.set_book_genre('Дюна', 'Фантастика')
        multi_collector.set_book_genre('Кольцо', 'Ужасы')
        multi_collector.set_book_genre('Под куполом', 'Ужасы')

        horrors = multi_collector.get_books_with_specific_genre('Ужасы')
        assert len(horrors) == 3

        fantasy = multi_collector.get_books_with_specific_genre('Фантастика')
        assert len(fantasy) == 2

        detective = multi_collector.get_books_with_specific_genre('Детективы')
        assert len(detective) == 1
    
    # Проверка словаря (books_genre).
    @pytest.mark.parametrize('my_books_genre', [{'Гарри Поттер': '', 'Дюна': ''}, {'Гарри Поттер2': '', 'Дюна2': ''}])
    def test_get_books_genre(self, my_books_genre):
        collector = BooksCollector()

        for book, _ in my_books_genre.items():
            collector.add_new_book(book)

        books_genre = collector.get_books_genre()

        assert books_genre == my_books_genre

    # Проверка добавления в избранное.
    def test_add_book_in_favorites(self, multi_collector):
        multi_collector.add_book_in_favorites('Оно')

        favorites = multi_collector.favorites

        assert len(favorites) == 1 and favorites[0] == 'Оно'
    
    # Проверка получения списка избранных книг.
    def test_get_list_of_favorites_books(self, multi_collector):
        multi_collector.add_book_in_favorites('Оно')
        multi_collector.add_book_in_favorites('Гарри Поттер')
        multi_collector.add_book_in_favorites('Оно: Добро пожаловать в Дерри')

        favorites = multi_collector.get_list_of_favorites_books()

        assert len(favorites) == 2 and favorites[0] == 'Оно' and favorites[1] == 'Гарри Поттер'

    # Проверка удаления книги из списка избранных книг.
    def test_delete_book_from_favorites(self, multi_collector):
        multi_collector.add_book_in_favorites('Оно')
        multi_collector.add_book_in_favorites('Гарри Поттер')

        multi_collector.delete_book_from_favorites('Оно')

        favorites = multi_collector.get_list_of_favorites_books()

        assert len(favorites) == 1 and favorites[0] == 'Гарри Поттер'
