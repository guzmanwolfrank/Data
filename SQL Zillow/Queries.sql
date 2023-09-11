-- queries.sql

CREATE TABLE IF NOT EXISTS my_table (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);

INSERT INTO my_table (name, age) VALUES ('Alice', 30);
INSERT INTO my_table (name, age) VALUES ('Bob', 25);
