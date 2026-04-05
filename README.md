Here’s your **README.md content** in clean professional format 👇

---

# 🚌 Bus Tracking Web Application

A simple Flask-based web application for managing and tracking buses in real-time.

---

## 🚀 Project Structure

```
bus-tracking/
│
├── backend/
│   ├── app.py
│   ├── db.py
│   ├── models.py
│   ├── utils.py
│
│   ├── templates/
│   │   ├── page1_routes.html
│   │   ├── page2_stops.html
│   │   ├── page3_driver.html
│   │   └── page4_student.html
│
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│
│   └── venv/
│
├── database/
│   ├── bus.db
│   └── schema.sql
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Navigate to Backend

```
cd backend
```

### 2. Activate Virtual Environment

```
source venv/bin/activate
```

### 3. Install Dependencies (if needed)

```
pip install flask
```

### 4. Run Flask Server

```
python app.py
```

---

## 🌐 Access Application

Open your browser and use the following URLs:

| Page         | URL                                                            |
| ------------ | -------------------------------------------------------------- |
| Add Route    | [http://127.0.0.1:5000/](http://127.0.0.1:5000/)               |
| Add Stops    | [http://127.0.0.1:5000/stops](http://127.0.0.1:5000/stops)     |
| Driver Panel | [http://127.0.0.1:5000/driver](http://127.0.0.1:5000/driver)   |
| Track Bus    | [http://127.0.0.1:5000/student](http://127.0.0.1:5000/student) |

---

## 📌 Important Notes

* Do **NOT** use `python -m http.server`
* Flask handles both frontend and backend
* All HTML files must be inside `templates/`
* CSS and JS must be inside `static/`

---

## 🎨 Static Files Usage

In all HTML files, use:

```
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
<script src="{{ url_for('static', filename='js/script.js') }}"></script>
```

---

## 🔧 Troubleshooting

### CSS/JS Not Loading

* Check path using `url_for`
* Hard refresh: `Ctrl + Shift + R`
* Verify:

  ```
  http://127.0.0.1:5000/static/css/style.css
  ```

### Page Not Found (404)

* Ensure route is defined in `app.py`

---

## 🧠 Tech Stack

* Python (Flask)
* HTML, CSS, JavaScript
* SQLite

---

## 🚀 Future Improvements

* Live GPS auto-refresh
* Map integration (Google Maps / Leaflet)
* User authentication
* Mobile responsiveness improvements

---

## 👨‍💻 Author

