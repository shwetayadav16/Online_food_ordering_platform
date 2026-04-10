CREATE TABLE food_items (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER
);

INSERT INTO food_items (name, price) VALUES
("Pizza", 200),
("Burger", 100),
("Pasta", 150);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    total REAL
);

CREATE TABLE order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    name TEXT,
    price INTEGER,
    quantity INTEGER
);