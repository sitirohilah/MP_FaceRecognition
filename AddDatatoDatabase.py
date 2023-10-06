import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://attendacesystem-559a2-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "342319":
        {
            "name": "Ragil A.R",
            "major": "Robotics",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "E",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },

    "718534":
        {
            "name": "Siti Rohilah",
            "major": "Informatics",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "E",
            "year": 5,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    
    "524342":
        {
            "name": "Maudy Ayunda",
            "major": "Politics",
            "starting_year": 2020,
            "total_attendance": 12,
            "standing": "P",
            "year": 7,
            "last_attendance_time": "2022-12-11 00:54:34"
        },

}

for key, value in data.items():
    ref.child(key).set(value)