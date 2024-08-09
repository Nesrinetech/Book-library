# Initailizing a book

class Book:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
        self.last_page = 0


        self.font_size = 12
        self.chars_per_page = calculate(self.font_size)

# Displaying page (last page of the content)
def desplay_page(self):
    start_idx = self.chars_per_page * self.last_page
    end_idx = start_idx + self.chars_per_page
    return self.content[start_idx.end_idx]

def turn_page(self):
    self.last_page += 1
    return self.display_page()

# creating the Library (collection of books + active books)
class Library:
    def __init__(self):
        self.collection = dict()
        self.active_book = None
        self.id_counter = 0

# add to the collection
def add_to_collection(self, title, content):
    new_book = Book(self.id_counter, title, content)
    self.collection[new_book.id] = new_book
    self.id_counter += 1

# Removing the book from the collection based on the id

def remove_from_collection(self, id):
    del self.collection[id]

# User can set a book from their library as active
def set_book_active(self, id):
    self.active_book = id

# The reading app only displays a page of text at a time in the active book
def display_page(self):
    return self.collection[self.active_book].display_page()

def turn_page(self):
    return self.collection[self.active_book].turn_page()