import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("admin-service-key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iris-attendance-module-default-rtdb.asia-southeast1.firebasedatabase.app/'
})


ref = db.reference('Students')

data = {
    "312654":
    {
        "name": "Akarsh Bajpai",
        "major": "Computer Science",
        "starting_year": 2020,
        "total_attendance": 77,
        "standing": "E",
        "year": 4,
        "last_attendance_time": "2023-11-20 00:54:34"
    }
}


for key, value in data.items():
    ref.child(key).set(value)
