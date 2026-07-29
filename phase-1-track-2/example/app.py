from enum import Enum

from fastapi import FastAPI, HTTPException, Query, status
from fastapi.responses import Response
from pydantic import BaseModel, Field

app = FastAPI(title="My Books API")


class HealthResponse(BaseModel):
    status: str
    version: str


class Book(BaseModel):
    id: int = Field(gt=0, description="books id")
    title: str = Field(min_length=3, max_length=50, description="Book name")
    author: str = Field(min_length=3, max_length=10, description="Author name")
    price: int = Field(gt=100, description="Price must be greater than 100 rs")
    year_published: int | None = None


class PaginatedBooks(BaseModel):
    data: list[Book]
    total: int
    limit: int
    offset: int
    count: int


class SortOrder(str, Enum):
    ASC = "asc"
    DESC = "desc"


#  In-memory database
books_database: list[Book] = []


@app.post("/books/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_one_book(book: Book):
    books_database.append(book)
    return book


@app.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(status="ok", version="1.0.0")


@app.get("/books/", status_code=status.HTTP_200_OK, response_model=PaginatedBooks)
async def get_all_books(
    q: str | None = Query(None, description="Search by book name", min_length=5),
    author: str | None = Query(None, description="Search By Author name", min_length=5),
    min_price: int | None = Query(None),
    max_price: int | None = Query(None),
    sort_by: str | None = Query("year_published", description="sort by year published"),
    sort_order: SortOrder = Query(  # noqa: B008
        SortOrder.ASC, description="Field to srt by ascending", pattern="^(asc|desc)$"
    ),
    limit: int = Query(5, ge=1, le=10, description="Items per page"),
    offset: int = Query(0, ge=0, description="Page Offset"),
):
    results = books_database
    allowed_fields = {"id", "price", "year_published", "title", "author"}

    if q:
        q_lower = q.lower()
        results = [item for item in results if q_lower in item.title.lower()]

    if author:
        results = [item for item in results if item.author == author]

    if min_price is not None:
        results = [item for item in results if item.price >= min_price]
    if max_price is not None:
        results = [item for item in results if item.price <= max_price]

    if sort_by not in allowed_fields:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Item not properly defined"
        )

    reverse = sort_order.lower() == SortOrder.DESC
    # getattr take values at runtime from class objects
    results = sorted(results, key=lambda x: getattr(x, sort_by), reverse=reverse)

    paged_items = results[offset : offset + limit]

    return {
        "data": paged_items,
        "total": len(results),
        "limit": limit,
        "offset": offset,
        "count": len(paged_items),
    }


@app.get("/books/{id}", response_model=Book)
async def get_single_book(id: int):
    single_book_data = next((item for item in books_database if item.id == id), None)
    if not single_book_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return single_book_data


# fix this
@app.patch("/books/{id}", response_model=Book)
async def update_single_book(id: int, book_update: Book):
    for i, item in enumerate(books_database):
        if item.id == id:
            # Convert existing dict to Pydantic model
            stored_book = item

            # Get only the fields explicitly sent in the request
            update_data = book_update.model_dump(exclude_unset=True)

            # Update the model with only the new data
            updated_book = stored_book.model_copy(update=update_data)

            # Update the in-memory database
            books_database[i] = updated_book
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
