
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1

    def turn_page(self):
        if self.current_page < self.pages:
            self.current_page += 1
        else:
            print("You have reached the end of the book.")