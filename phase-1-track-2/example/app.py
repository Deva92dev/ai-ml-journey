from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response

app = FastAPI(title="My Books API")


class Book(BaseModel):
    title: str
    author: str
    year_published: int


#  In-memory database
books_database: List[Book] = []


@app.post("/books/", status_code=status.HTTP_201_CREATED)
async def create_one_book(book: Book):
    books_database.append(book)
    return {"message": "Book created", "book": book}


# filtering is remaining
@app.get("/books/", status_code=status.HTTP_200_OK, response_model=List[Book])
async def get_all_books(skip: int = 1, limit: int = 2):
    return books_database[skip : skip + limit]


@app.get("/books/{title}", response_model=List[Book])
async def get_single_book(title: str):
    single_book_data = [item for item in books_database if item.title == title]
    return single_book_data


@app.patch("/books/{title}", response_model=Book)
async def update_single_book(title: str, book_update: Book):
    for i, item in enumerate(books_database):
        if item.title == title:
            # Convert existing dict to Pydantic model
            stored_book = Book(title="some", author="Author", year_published=2025)

            # Get only the fields explicitly sent in the request
            update_data = book_update.model_dump(exclude_unset=True)

            # Update the model with only the new data
            updated_book = stored_book.model_copy(update=update_data)

            # Update the in-memory database
            books_database[i] = jsonable_encoder(updated_book)
            return updated_book

    raise HTTPException(status_code=404, detail=f"Item '{title}' not found")


# helper function to find book to delete
def find_book(title: str):
    for index, item in enumerate(books_database):
        if item.title == title:
            return index
    return None


@app.delete("/books/{title}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(title: str):
    item = find_book(title)

    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{title} not found"
        )

    books_database.pop(item)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
