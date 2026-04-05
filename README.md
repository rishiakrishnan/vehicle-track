cd backend

# create DB
sqlite3 ../database/bus.db < ../database/schema.sql

# install flask
pip install flask

# run
python app.py


cd frontend
xdg-open page1_routes.html