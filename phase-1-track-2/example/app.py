from fastapi import FastAPI, status, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response

app = FastAPI(title="My Books API")


class Book(BaseModel):
    id: int
    title: str
    author: str
    price: int
    year_published: int


class PaginatedBooks(BaseModel):
    data: List[Book]
    total: int
    limit: int
    offset: int
    count: int


#  In-memory database
books_database: List[Book] = []


@app.post("/books/", status_code=status.HTTP_201_CREATED)
async def create_one_book(book: Book):
    books_database.append(book)
    return {"message": "Book created", "book": book}


# filtering is remaining
# @app.get("/books/", status_code=status.HTTP_200_OK, response_model=List[Book])
# async def get_all_books(skip: int = 0, limit: int = 3):
#     return books_database[skip : skip + limit]


@app.get("/books/", status_code=status.HTTP_200_OK, response_model=PaginatedBooks)
async def get_all_books(
    q: Optional[str] = Query(None, description="Search by book name", min_length=5),
    author: Optional[str] = Query(
        None, description="Search By Author name", min_length=5
    ),
    min_price: Optional[int] = Query(None),
    max_price: Optional[int] = Query(None),
    limit: int = Query(2, ge=1, le=5, description="Items per page"),
    offset: int = Query(0, ge=0, description="Page Offset"),
):
    results = books_database

    if q:
        q_lower = q.lower()
        results = [item for item in results if q_lower in item.title.lower()]

    if author:
        results = [item for item in results if item.author == author]

    if min_price is not None:
        results = [item for item in results if item.price >= min_price]
    if max_price is not None:
        results = [item for item in results if item.price <= max_price]

    paged_items = results[offset : offset + limit]

    return {
        "data": paged_items,
        "total": len(results),
        "limit": limit,
        "offset": offset,
        "count": len(paged_items),
    }


@app.get("/books/{id}", response_model=List[Book])
async def get_single_book(id: int):
    single_book_data = [item for item in books_database if item.id == id]
    return single_book_data


# fix this
@app.patch("/books/{id}", response_model=Book)
async def update_single_book(id: int, book_update: Book):
    for i, item in enumerate(books_database):
        if item.id == id:
            # Convert existing dict to Pydantic model
            stored_book = Book(
                title="some", author="Author", year_published=2025, id=145, price=150
            )

            # Get only the fields explicitly sent in the request
            update_data = book_update.model_dump(exclude_unset=True)

            # Update the model with only the new data
            updated_book = stored_book.model_copy(update=update_data)

            # Update the in-memory database
            books_database[i] = jsonable_encoder(updated_book)
            return updated_book

    raise HTTPException(status_code=404, detail=f"Item '{id}' not found")


# helper function to find book to delete
def find_book(id: int):
    for index, item in enumerate(books_database):
        if item.id == id:
            return index
    return None


@app.delete("/books/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id: int):
    item = find_book(id)

    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found"
        )

    books_database.pop(item)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
