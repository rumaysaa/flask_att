from modules.Config_db import *
from bson.objectid import ObjectId
from passlib.hash import sha256_crypt


def updateAccountDetails(req):
    emp_att = db.Employees.update_one(
        {'_id' : ObjectId(req["emp_id"])},
        {
        "$set":{ 
            "first_name" : req["fname"],
            "last_name" : req["lname"],
            "email": req["mail"],
            "phone": req["phone"],
            "dob": req["dob"],
            "joining_date": req["joining_date"]
            #"last_edited" : datetime.now()
        }
        })
    return emp_att

def getAccountDetails(empID):
    data = db.Employees.find_one({
        "_id" : ObjectId(empID)
    })
    json = {"fname" : data["first_name"],
            "lname" : data["last_name"],
            "email" : data["email"],
            "phone" : data["phone"],
            "dob" : data["dob"], 
            "joining_date":data["joining_date"],
            "gender": data["gender"],
            "desig" : data['designation'],
            "shift" : data['shift'],
            "address": data['address'],
            "city": data['city'],
            "avatarID" : data['avatarID']
            }
    return json

def updatePasswordByEmpId(empID,new_pass):
    update_pwd = db.Credentials.update_one(
         {'employeeID' : ObjectId(empID)},
        {
        "$set":{"password" : sha256_crypt.hash(new_pass)}
        })
    return update_pwd
        
def updateAccountAvatar(employee_id,avatar_id):
    print(employee_id,avatar_id)
    update_avatar = db.Employees.update_one(
         {'_id' : ObjectId(employee_id)},
        {
        "$set":{"avatarID" : avatar_id}
        })
    return update_avatar