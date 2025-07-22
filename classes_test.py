from pprint import pprint

class Book:
    def __init__(self, title = "The Cat in the Hat", author = "Dr. Seuss", year = "1957"):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        print("Title:", self.title + ", Author:", self.author + ", Year:", str(self.year))

    def is_classic(self):
        if int(self.year) < 1970:
            return True    

    def __str__(self):
        return str(self.__dict__)




book1 = Book("Project Hail Mary", "Andy Weir", 2021)
book2 = Book()


book1.describe()
book2.describe()
print(book2.is_classic())



pprint(dir(book1))
print("-----------------------")
print(book1)