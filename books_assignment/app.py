from fastapi import FastAPI
from pydantic import BaseModel

from books_assignment.book import Book
from books_assignment.book_request import BookRequest

BOOKS = [
    Book(1, 'Two Night Stand', 'Chethan Bhagath', 4.1),
    Book(2, 'Harry Potter Part 1', 'JK Rowling', 4.6)
]

app = FastAPI()

# Base root directory 
@app.get('/')
def root():
    return {'Message': 'Welcome !'}

# Post request
@app.put('/add_book/')
def add_book(new_book: BookRequest):
    return new_book

# Getting all books
@app.get('/get_books/')
def get_all_books():
    return BOOKS