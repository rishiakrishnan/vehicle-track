from db import get_connection

# ROUTES
def add_route(route_no, driver_name, phone):
    conn = get_connection()
    conn.execute(
        "INSERT INTO routes (route_no, driver_name, phone) VALUES (?, ?, ?)",
        (route_no, driver_name, phone)
    )
    conn.commit()
    conn.close()


def get_routes():
    conn = get_connection()
    routes = conn.execute("SELECT * FROM routes").fetchall()
    conn.close()
    return [dict(r) for r in routes]


# STOPS
def add_stop(route_no, stop_number, stop_name, lat, lon):
    conn = get_connection()
    conn.execute(
        "INSERT INTO stops (route_no, stop_number, stop_name, latitude, longitude) VALUES (?, ?, ?, ?, ?)",
        (route_no, stop_number, stop_name, lat, lon)
    )
    conn.commit()
    conn.close()


def get_stops(route_no):
    conn = get_connection()
    stops = conn.execute(
        "SELECT * FROM stops WHERE route_no=? ORDER BY stop_number",
        (route_no,)
    ).fetchall()
    conn.close()
    return [dict(s) for s in stops]


# DRIVER LOCATION
def update_location(route_no, lat, lon):
    conn = get_connection()
    conn.execute(
        "INSERT INTO driver_location (route_no, latitude, longitude) VALUES (?, ?, ?)",
        (route_no, lat, lon)
    )
    conn.commit()
    conn.close()


def get_latest_location(route_no):
    conn = get_connection()
    loc = conn.execute(
        "SELECT * FROM driver_location WHERE route_no=? ORDER BY timestamp DESC LIMIT 1",
        (route_no,)
    ).fetchone()
    conn.close()
    return dict(loc) if loc else None