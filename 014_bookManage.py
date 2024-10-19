class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_borrowed = False

    # 对象的字符串表示
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nBorrowed: {'Yes' if self.is_borrowed else 'No'}"

    def borrow(self):
        if self.is_borrowed:
            print("This book is already borrowed.")
        else:
            self.is_borrowed = True
            print("Book borrowed successfully.")

    def return_book(self):
        if not self.is_borrowed:
            print("This book is not borrowed.")
        else:
            self.is_borrowed = False
            print("Book return ed successfully.")

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book removed from the library.")
        else:
            print("Book not found in the library.")

    def list_books(self):
        if len(self.books) == 0:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)
                print("------------------------")

library = Library("My Library")

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
book3 = Book("1984", "George Orwell", "Dystopian")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.list_books()

book2.borrow()
book1.return_book()

library.remove_book(book3)

library.list_books()


"""
1 class Book:：定义了一个 Book 类，表示图书的基本属性和操作。
2 __init__(self, title, author, genre):：
 初始化 Book 对象的属性，包括标题、作者、流派，并将初始的借阅状态设为 False。
3 __str__(self):：返回一个字符串表示 Book 对象的详细信息。
4 borrow(self):：借阅该图书的方法。如果图书已被借出，则打印提示信息；否则，将借阅状态设为 True。
5 return_book(self):：归还该图书的方法。如果图书未被借出，则打印提示信息；否则，将借阅状态设为 False。
6 class Library:：定义了一个 Library 类，表示图书馆，包含管理图书的操作。
7 __init__(self, name):：初始化 Library 对象的属性，包括图书馆名称和一个空的图书列表。
8 add_book(self, book):：向图书馆中添加图书的方法，将图书对象添加到图书列表中。
9 remove_book(self, book):：从图书馆中移除图书的方法，将图书对象从图书列表中移除。
10 list_books(self):：列出图书馆中所有图书的方法，打印每本图书的详细信息。
11 创建一个 Library 对象，表示一个图书馆。
12 创建 Book 对象 book1、book2 和 book3，表示不同的图书。
13 调用 Library 对象的 add_book() 方法，将图书添加到图书馆。
14 调用 Library 对象的 list_books() 方法，列出图书馆中的所有图书。
15 调用 Book 对象的 borrow() 和 return_book() 方法，模拟借阅和归还图书的操作。
16 调用 Library 对象的 remove_book() 方法，从图书馆中移除一本图书。
17 再次调用 Library 对象的 list_books() 方法，列出更新后的图书馆中的所有图书。
这段代码实现了一个简单的图书管理系统。它使用类和对象的概念来表示图书和图书馆，并提供了一些基本的操作，如添加图书、移除图书、借阅图书、归还图书和列出图书馆中的所有图书。
"""