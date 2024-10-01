from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


class Book(BaseModel):
    """Data model representing a book entity."""
    id: int
    title: str
    author: str
    published_year: int
    description: Optional[str] = None


# memory storage for books
books_db = []

@app.post("/books/", response_model=Book, status_code=201)
async def create_book(book: Book):
    """
    Create a new book entry in the database.

    Args:
        book (Book): The book details to be created.

    Raises:
        HTTPException: If a book with the same ID already exists.

    Returns:
        Book: The newly created book entry.
    """
    for existing_book in books_db:
        if existing_book.id == book.id:
            raise HTTPException(status_code=400, detail="Book with this ID already exists.")
    books_db.append(book)
    return book

@app.get("/books/", response_model=List[Book])
async def read_books():
    """
    Retrieve a list of all book entries.

    Returns:
        List[Book]: A list containing all book entries in the database.
    """
    return books_db


@app.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: int):
    """
    Retrieve a specific book by its unique ID.

    Args:
        book_id (int): The unique identifier of the book to retrieve.

    Raises:
        HTTPException: If no book is found with the specified ID.

    Returns:
        Book: The book entry that matches the given ID.
    """
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found.")


@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, updated_book: Book):
    """
    Update an existing book entry with new details.

    Args:
        book_id (int): The unique identifier of the book to update.
        updated_book (Book): The updated book details.

    Raises:
        HTTPException: If no book is found with the specified ID.

    Returns:
        Book: The updated book entry.
    """
    for index, book in enumerate(books_db):
        if book.id == book_id:
            books_db[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found.")


@app.delete("/books/{book_id}", status_code=204)
async def delete_book(book_id: int):
    """
    Delete a book entry from the database by its unique ID.

    Args:
        book_id (int): The unique identifier of the book to delete.

    Raises:
        HTTPException: If no book is found with the specified ID.

    Returns:
        None: This endpoint returns no content upon successful deletion.
    """
    for index, book in enumerate(books_db):
        if book.id == book_id:
            books_db.pop(index)
            return {"message": "the book is successfully deleted"}
    raise HTTPException(status_code=404, detail="Book not found.")
