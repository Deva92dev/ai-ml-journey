import psycopg
from dotenv import load_dotenv
import os
from fastapi import FastAPI, Depends, Request
from psycopg_pool import AsyncConnectionPool
from contextlib import asynccontextmanager

load_dotenv()

CONNECTION_STRING = os.getenv("DATABASE_STRING")

@asynccontextmanager
async def lifespan(app:FastAPI):
    # Create pool on startup
    app.state.pool = AsyncConnectionPool(CONNECTION_STRING, open=True)

    yield

    # shut pool on close
    await app.state.pool.close()

app = FastAPI(lifespan=lifespan)

async def get_db(request: Request):
    async with request.app.pool.connection() as conn:
        yield conn




# all_books = [
#     ("Geetanjali", "Tagore", 450.0, 1914),
#     ("Godan", "Premchand", 150.0, 1905),
#     ("Anandmath", "Tagore", 195., 1920),
#     ("Godan", "Premchand", 245.0, 1920)
# ]

with psycopg.connect("dbname=books_api_db user=books_api") as conn:
    with conn.cursor() as curr:
        # curr.execute("""
        #     CREATE TABLE books (
        #     id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        #     title varchar(80),
        #     author varchar(80),
        #     price numeric(10, 2),
        #     year_published int)
        #     """)
        
        # database is connected
        print("connected") 

        # curr.executemany("""INSERT INTO books (title, author, price, year_published)
        #             VALUES (%s, %s, %s, %s); 
        #             """,
        #             all_books 
        #             )

        # to cehck use select query and then you will be able to see the result

        # curr.execute("UPDATE books SET price = %s WHERE id = %s ", (350.0, 1))
        # curr.execute("DELETE FROM books WHERE id = %s", (1,))

        curr.execute("SELECT * FROM books")
        print(curr.fetchall())

