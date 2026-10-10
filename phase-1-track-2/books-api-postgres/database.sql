DROP TABLE IF EXISTS books;

CREATE TABLE books (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title VARCHAR(80),
    author VARCHAR(80),
    price NUMERIC(10, 2),
    year_published INT
);

INSERT INTO
    books (
        title,
        author,
        price,
        year_published
    )
VALUES (
        'Godan',
        'Premchand',
        150.0,
        1920
    );

INSERT INTO
    books (
        title,
        author,
        price,
        year_published
    )
VALUES (
        'Namak Ka Daroga',
        'Premchand',
        190.0,
        1925
    );

INSERT INTO
    books (
        title,
        author,
        price,
        year_published
    )
VALUES (
        'Idgah',
        'Premchand',
        290.0,
        1922
    );

INSERT INTO
    books (
        title,
        author,
        price,
        year_published
    )
VALUES (
        'Geetanjali',
        'Tagore',
        390.0,
        1914
    );

INSERT INTO
    books (
        title,
        author,
        price,
        year_published
    )
VALUES (
        'Anandmath',
        'Tagore',
        490.0,
        1936
    );

SELECT id, title, author, price, year_published FROM books;

UPDATE books SET "year_published" = 1905 WHERE id = 1;

UPDATE books SET "year_published" = 1926 WHERE id = 4;

DELETE FROM books WHERE id = 2;

TRUNCATE TABLE books RESTART IDENTITY;