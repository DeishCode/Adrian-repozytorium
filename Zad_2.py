class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Library in: {self.city}, {self.street}, {self.zip_code}\n"
            f"Open hours: {self.open_hours}\nPhone: {self.phone}"
        )


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Employee: {self.first_name} {self.last_name}\n"
            f"Hire Date: {self.hire_date}\nBirth Date: {self.birth_date}\n"
            f"Location: {self.city}, {self.street}, {self.zip_code}\nPhone: {self.phone}"
        )


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Book: {self.author_name} {self.author_surname}\n"
            f"Published: {self.publication_date}\nPages: {self.number_of_pages}\nLibrary: {self.library}"
        )


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = "\n".join(
            [f"{book.author_name} {book.author_surname}" for book in self.books])
        return (
            f"Order:\nEmployee: {self.employee}\nStudent: {self.student}\n"
            f"Books: {book_list}\nOrder Date: {self.order_date}"
        )


library1 = Library("City1", "Street1", "12-345", "8:00  20:00", "123-456-789")
library2 = Library("City2", "Street2", "54-321", "6:00 - 18:00", "987-654-321")

employee1 = Employee("Jan", "Kowalski", "05.05.2022",
                     "01.01.2000", "City1", "Street1", "12-345", "555-111-222")
employee2 = Employee("Arek", "Janusz", "05.05.2022",
                     "02.02.2001", "City1", "Street1", "12-345", "555-333-444")

book1 = Book(library1, "05.06.1900", "Author1", "Surname1", 200)
book2 = Book(library1, "01.06.1925", "Author2", "Surname2", 300)
book3 = Book(library2, "05.07.1906", "Author3", "Surname3", 400)
book4 = Book(library2, "03.06.1970", "Author4", "Surname4", 500)

student1 = "Student1"
student2 = "Student2"

order1 = Order(employee1, student1, [book1, book2, book3], "15.01.2023")
order2 = Order(employee2, student2, [book4], "20.03.2023")

print(order1, "\n")
print("-" * 50)
print(order2, "\n")
