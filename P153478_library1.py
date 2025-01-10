#!/usr/bin/env python
# coding: utf-8

# In[23]:


# P153478_library.py

class Book:
    
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = False
        self.checked_out_by = None  
    
    def get_book_info(self):
        return f"{self.title} by {self.author}, {self.year}"

    def check_out(self, customer_name):
        self.is_checked_out = True
        self.checked_out_by = customer_name
        print(f"{self.title} has been checked out by {customer_name}.")

    def return_book(self):
        self.is_checked_out = False
        print(f"{self.title} has been returned by {self.checked_out_by}.")
        self.checked_out_by = None  #clear the customer's name

    def update_info(self, title=None, author=None, year=None,print_info=True): #put none to avoid parameter become required
        if title:
            self.title = title
        if author:
            self.author = author
        if year:
            self.year = year
        if print_info: #avoid reprint at eBook
            print(f"Updated book information: {self.get_book_info()}")

class eBook(Book):
    
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size  #in MB

    def get_book_info(self):
        return f"{self.title} by {self.author}, {self.year} (File size: {self.file_size} MB)"

    def download(self):
        print(f"Downloading {self.title}...")

    def update_info(self, title=None, author=None, year=None, file_size=None):
        super().update_info(title, author, year, print_info=False)
        if file_size:
            self.file_size = file_size
        print(f"Updated eBook information: {self.get_book_info()}")

