from flask import Flask, request, jsonify, render_template
from models import *
from utils import haversine, calculate_eta
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ---------- FRONTEND PAGES ----------
@app.route('/')
def routes_page():
    return render_template('page1_routes.html')

@app.route('/stops')
def stops_page():
    return render_template('page2_stops.html')

@app.route('/driver')
def driver_page():
    return render_template('page3_driver.html')

@app.route('/student')
def student_page():
    return render_template('page4_student.html')


# ---------- ROUTES API ----------
@app.route('/add_route', methods=['POST'])
def add_route_api():
    data = request.json
    add_route(data['route_no'], data['driver_name'], data['phone'])
    return jsonify({"message": "Route added"})


@app.route('/get_routes', methods=['GET'])
def get_routes_api():
    return jsonify(get_routes())


# ---------- STOPS ----------
@app.route('/add_stop', methods=['POST'])
def add_stop_api():
    data = request.json
    add_stop(
        data['route_no'],
        data['stop_number'],
        data['stop_name'],
        data['latitude'],
        data['longitude']
    )
    return jsonify({"message": "Stop added"})


@app.route('/get_stops/<route_no>', methods=['GET'])
def get_stops_api(route_no):
    return jsonify(get_stops(route_no))


# ---------- DRIVER ----------
@app.route('/update_location', methods=['POST'])
def update_location_api():
    data = request.json
    update_location(data['route_no'], data['latitude'], data['longitude'])
    return jsonify({"message": "Location updated"})


# ---------- STUDENT ----------
@app.route('/track/<route_no>', methods=['GET'])
def track(route_no):
    stops = get_stops(route_no)
    driver = get_latest_location(route_no)

    if not driver:
        return jsonify({"error": "No driver location"})

    result = []
    reached = True

    for stop in stops:
        distance = haversine(
            driver['latitude'],
            driver['longitude'],
            stop['latitude'],
            stop['longitude']
        )

        if reached and distance <= 0.2:
            status = "reached"
        else:
            reached = False
            eta = calculate_eta(distance)
            status = f"coming ETA: {eta} min"

        result.append({
            "stop": stop['stop_name'],
            "status": status
        })

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)