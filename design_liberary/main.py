
# library
# rent a book
class Language:
    HEBREW = 1,
    ENGLISH = 2,
    SPANISH = 3,
    RUSSIAN = 4

# Person ABC - @property id, @property first-name, @property last-name
# Book - catalog_number, title, price, publish-year, language (enum), rented: bool
# Author: Person - first, last, optional: list[books]? weak
# ILibrary ABC: rent_a_book (catalog_number) , return_book ()
#               add_book(book), find_book(**kwargs) : books
#               book_available(catalog_number) : bool
# Library: ILibrary ABC - name, address, subjects : list[str], manager-name,
#            books: dict[ catalog_number : list[book] ]
# Customer: Person - address, ph-number
# RentDetails - Book, rent_date, customer, return_date, rented: bool
# rent a book ->
#           check Library.books[catalog_number] > 0
#           Library.books[catalog_number]--