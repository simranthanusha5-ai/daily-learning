# Day 31: Classes and Instances

class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0

    def read(self, pages_read: int):
        self.current_page = min(self.pages, self.current_page + pages_read)
        print(f"Read {pages_read} pages of '{self.title}'. Progress: {self.current_page}/{self.pages}")

b = Book("Fluent Python", "Luciano Ramalho", 800)
b.read(45)
b.read(60)
