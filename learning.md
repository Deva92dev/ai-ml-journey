- To return the single book object, use next() with a generator expression to extract the first match
- If you are returing many values from a function, they are in tuple you can not add them like normal variables, you have to unpack them and then yo can perform operations on any single one of them.

- The ChainedAssignmentError occurs because you are using inplace=True on a Series created by indexing (df["Age"]), which behaves as a copy under pandas' Copy-on-Write mode

- to check postgresql server is running from terminal : systemctl status postgresql
- to start databse from terminal: psql books_api_db for books_api_psogtgres project
- to connect from terminal psql -U books_api -d books_api_db
- check current user: SELECT current_user
- The INSERT statement is used to populate a table with rows:

- using psycopg3, the parameters will not be really merged to the query: query and the parameters are sent to the server separately: see Server-side binding(psycopg website) for details.