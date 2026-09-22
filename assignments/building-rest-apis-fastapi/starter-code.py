from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Book API", description="A simple API for managing books.")


class BookCreate(BaseModel):
    title: str
    author: str
    price: float


class Book(BookCreate):
    id: int


books = [
    {"id": 1, "title": "Python Crash Course", "author": "Eric Matthes", "price": 29.99},
    {"id": 2, "title": "Fluent Python", "author": "Luciano Ramalho", "price": 39.95},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API"}


@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    new_book = {
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author,
        "price": book.price,
    }
    books.append(new_book)
    return new_book


@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: BookCreate):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            books[index] = {
                "id": book_id,
                "title": updated_book.title,
                "author": updated_book.author,
                "price": updated_book.price,
            }
            return books[index]

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            deleted_book = books.pop(index)
            return {"message": f"Book {book_id} deleted", "deleted_book": deleted_book}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
