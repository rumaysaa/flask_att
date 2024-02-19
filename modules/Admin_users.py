from modules.Config_db import *
from bson.objectid import ObjectId
from passlib.hash import sha256_crypt

def registerUser(req):
    emp = db.Employees.insert_one({
        "first_name" : req["fname"],
        "last_name" : req["lname"],
        "gender": req["gender"],
        "address": req['add'],
        "city": req['city'],
        "email" : req['email'],
        "phone" : req['phone'],
        "dob" : req["dob"],
        "joining_date" : req["joining_date"],
        "shift" : req["shift"],
        "gender" : req["gender"],
        "designation" : req["desig"],
        "avatarID": "profile"
        }) 
    empID = str(emp.inserted_id)
    cred = db.Credentials.insert_one({
        "employeeID" : ObjectId(empID),
        "username": req["username"],
        "password" : sha256_crypt.hash("algo@123")
    })
    credID = str(cred.inserted_id)
    if empID:
        return True
    else: 
      return False
  
  
def get_users():
    users = list(db.Employees.find({}))
    json = []
    for user in users:
        json.append({
            "id" : str(user['_id']),
            "name" : user['first_name']+' '+ user['last_name'],
            "email" : user["email"],
            "phone" : user["phone"],
            "joining_dt" : user["joining_date"],
            "desig": user["designation"]
        })
    
    #print(json)
    return json

def deleteUserById(user_id):
    try:
        db.Employees.delete_one(
            {"_id": ObjectId(user_id)}
        )
        db.Credentials.delete_one(
            {"employeeID": ObjectId(user_id)}
        )
    except:
        return None
    return "Success"

def getUserById(user_id):
    try:
        user = (db.Employees.find_one({
            "_id" : ObjectId(user_id)
        }))
        
        user_data = {
            "id" : str(user['_id']),
            "fname": user['first_name'],
            "lname" : user['last_name'],
            "dob": user['dob'],
            "joining_date": user['joining_date'],
            "gender": user["gender"],
            "desig" : user['designation'],
            "shift" : user.get('shift'),
            "add": user['address'],
            "city": user['city'],
            "email": user['email'],
            "phone": user['phone']
        }
        print(user_data)
    except:
        return None
    return user_data

def updateUserById(userID,req):
    print(userID)
    up_user = db.Employees.update_one(
            {"_id" : ObjectId(userID)},
            {"$set":{ 
            "first_name": req['fname'],
            "last_name" : req['lname'],
            "dob": req['dob'],
            "joining_date": req['joining_date'],
            "gender": req["gender"],
            "designation" : req['desig'],
            "shift" : req['shift'],
            "address": req['add'],
            "city": req['city'],
            "email": req['email'],
            "phone": req['phone']
            }}
            )
    print(up_user)
    return "Success"
