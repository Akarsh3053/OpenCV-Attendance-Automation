import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("admin-service-key.json")
firebase_admin.initialize_app(cred)
