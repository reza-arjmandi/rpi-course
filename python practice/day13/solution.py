import os  # For using os.linesep instead of using a line separator: '\n'

class Book(object):
        # Initialize the book title, author(s) name and price
	def __init__(self, title, author):
                # Assign the value to class variables 
		self.title = title
		self.author = author
   
class MyBook(Book):
        # Title: The book's title
        # Author: author The book's author
        # Price: The book's price
	def __init__(self, title, author, price):
		super().__init__(title, author)
		self.price = price

	def display(self):
                # Print the class variable values
		print("Title:", self.title, os.linesep+"Author:", self.author, os.linesep+"Price:", self.price)

title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
