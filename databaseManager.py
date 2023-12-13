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
        "total_attendance": 5,
        "standing": "E",
        "year": 4,
        "last_attendance_time": "2023-11-20 00:54:34"
    },
    "28523":
    {
        "name": "Mahi Srivastava",
        "major": "AIML",
        "starting_year": 2020,
        "total_attendance": 22,
        "standing": "A",
        "year": 4,
        "last_attendance_time": "2023-11-20 00:54:36"
    },
    "28722":
    {
        "name": "Kopal Trivedi",
        "major": "AIML",
        "starting_year": 2020,
        "total_attendance": 0,
        "standing": "C",
        "year": 4,
        "last_attendance_time": "2023-11-20 00:54:36"
    },
    "28372":
    {
        "name": "Shobhit Tiwari",
        "major": "AIML",
        "starting_year": 2020,
        "total_attendance":23,
        "standing": "B",
        "year": 4,
        "last_attendance_time": "2023-11-20 00:54:36"
    },
    "29164":
    {
        "name": "Harsh Srivastava",
        "major": "AIML",
        "starting_year": 2020,
        "total_attendance":9,
        "standing": "A",
        "year": 4,
        "last_attendance_time": "2023-11-20 00:54:36"
    },
    "29329":
    {
        "name": "Monal Kapoor",
        "major": "AI",
        "starting_year": 2020,
        "total_attendance":5,
        "standing": "A",
        "year": 4,
        "last_attendance_time": "2023-11-20 00:54:36"
    },
    "28480":
    {
        "name": "Nidhi Singh",
        "major": "AIML",
        "starting_year": 2020,
        "total_attendance":8,
        "standing": "A",
        "year": 4,
        "last_attendance_time": "2023-11-20 00:54:36"
    },
    "28858":
    {
        "name": "Atul Singh",
        "major": "AIML",
        "starting_year": 2020,
        "total_attendance":2,
        "standing": "B",
        "year": 4,
        "last_attendance_time": "2023-11-20 00:54:36"
    },
    "28356":
    {
        "name": "Bhavya Verma",
        "major": "AIML",
        "starting_year": 2020,
        "total_attendance":25,
        "standing": "B+",
        "year": 4,
        "last_attendance_time": "2023-11-20 00:54:36"
    },
    "28813":
    {
        "name": "Anuj Tiwari",
        "major": "IT",
        "starting_year": 2020,
        "total_attendance":2,
        "standing": "A",
        "year": 4,
        "last_attendance_time": "2023-11-20 00:54:36"
    }
}


for key, value in data.items():
    ref.child(key).set(value)
