import certifi
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://attendance_proj:vAezIHAOLszimbcV@cluster0.vabsxvc.mongodb.net/Attendance_management?retryWrites=true&w=majority"

try:
    client = MongoClient(uri,tlsCAFile=certifi.where())
    db = client['Attendance_management']
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

except Exception as e:
    print(e)