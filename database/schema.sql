CREATE TABLE routes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    route_no TEXT,
    driver_name TEXT,
    phone TEXT
);

CREATE TABLE stops (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    route_no TEXT,
    stop_number INTEGER,
    stop_name TEXT,
    latitude REAL,
    longitude REAL
);

CREATE TABLE driver_location (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    route_no TEXT,
    latitude REAL,
    longitude REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);