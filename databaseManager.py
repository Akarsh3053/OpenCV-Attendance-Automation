import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("admin-service-key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iris-attendance-module-default-rtdb.asia-southeast1.firebasedatabase.app/'
})


ref = db.reference('Students')

data = {
    "28442":
    {
        "name": "Akarsh Bajpai",
        "major": "CSE",
        "starting_year": 2020,
        "total_attendance": 77,
        "standing": "E",
        "year": 4,
        "last_attendance_time": "2023-11-20 00:54:34"
    },
    "28523":
    {
        "name": "Mahi Srivastava",
        "major": "Economics",
        "starting_year": 2020,
        "total_attendance": 26,
        "standing": "A",
        "year": 4,
        "last_attendance_time": "2023-11-20 00:54:36"
    },
"28722":
    {
        "name": "Mahi Srivastava",
        "major": "History",
        "starting_year": 2020,
        "total_attendance": 5,
        "standing": "C",
        "year": 4,
        "last_attendance_time": "2023-11-20 00:54:36"
    }
}


for key, value in data.items():
    ref.child(key).set(value)
