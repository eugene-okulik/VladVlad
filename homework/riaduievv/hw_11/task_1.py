class Book:
    material = "бумага"
    text = True

    def __init__(self, title, author, page_number, isbn, reserved_book):
        self.title = title
        self.author = author
        self.page_number = page_number
        self.isbn = isbn
        self.reserved_book = reserved_book
        self.reserved_message = 'зарезервирована' if reserved_book else ''


book1 = Book('Идиот', 'Достоевский', 500, 1, True)
book2 = Book('Война и мир', 'Лев Толстой', 501, 2, False)
book3 = Book('Отцы и дети', 'Иван Тургенев', 502, 3, True)
book4 = Book('Анна Каренина', 'Лев Толстой', 503, 4, True)
book5 = Book('Доктор Живаго', 'Борис Пастернак', 504, 5, False)


print("Название: {}, Автор: {}, страниц: {}, материал: {}, {}".format(
      book1.title, book1.author, book1.page_number, book1.material, book1.reserved_message))


class SchoolBooks(Book):
    def __init__(self, title, author, page_number, isbn, reserved_book, subject, school_class, tasks):
        super().__init__(title, author, page_number, isbn, reserved_book)
        self.subject = subject
        self.school_class = school_class
        self.tasks = tasks


school_book1 = SchoolBooks('Алгебра', 'Иванов', 200,
                           1, False, 'Математика', 9, True)
school_book2 = SchoolBooks('Геометрия', 'Сидоров', 201,
                           2, True, 'Математика', 10, True)

print("Название: {}, Автор: {}, страниц: {}, предмет: {}, класс: {}{}".format(
    school_book1.title, school_book1.author, school_book1.page_number,
    school_book1.subject, school_book1.school_class, school_book1.reserved_message))
