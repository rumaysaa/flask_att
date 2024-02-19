
from modules.Config_db import *
import pymongo
from bson.json_util import dumps,loads
from flask import session
from bson.objectid import ObjectId
from datetime import datetime,date
                

def getActiveEmployees():
    data = db.Attendance.find( {
        "date" : datetime.fromisoformat(date.today().isoformat()),
        "checkOutTime" : None
        }).sort('checkInTime', pymongo.DESCENDING)
    if(data != None):
        json = []
        json_data = loads(dumps(list(data)))
        for i in json_data:
            emp = db.Employees.find_one({
            "_id" : ObjectId(i["employeeID"])
            }) 
            if( i["checkInTime"] != None):
                inTime = i["checkInTime"].strftime("%H:%M:%S")
            else:
                inTime = None
            res = {
            "id" : str(i["_id"]),"employeeID":str(i['employeeID']),"name" : emp["first_name"]+" " +emp["last_name"],"email": emp["email"], "in" : inTime ,
            "breakTime": i["breakTime"]+" mins","status":i["inIpRange"]
            }
            if(i["checkOutTime"] != None):
                res["out"] = i["checkOutTime"].strftime("%H:%M:%S")
            json.append(res)
    return json 


def getInactiveEmployees(total_emps,active_emps):
    total_emps_ids = set()
    active_emps_ids = set()
    for i in total_emps:
        _id = str(i['_id'])
        #print(type(_id),type(total_emps_ids))
        total_emps_ids.add(_id)
    for i in active_emps:
        ac_id = str(i['employeeID'])
        active_emps_ids.add(ac_id)
    return total_emps_ids-active_emps_ids
    
def get_todays_checked_out_att():
    data = db.Attendance.find({
    "date" : datetime.fromisoformat(date.today().isoformat()),
    "checkOutTime": { "$ne": None}
    })
    return data

def getProjects():
    data = db.Projects.find({})
    return list(data)

def getPresentEmployees():
    data = list(db.Attendance.find({
    "date" : datetime.fromisoformat(date.today().isoformat()),
    }))
    employee_data = []
    if(data != None):
        for i in data:
            emp = db.Employees.find_one({
            "_id" : ObjectId(i["employeeID"])
            }) 
            res = {
            "name" : emp["first_name"]+" " +emp["last_name"],"email": emp["email"], "in" : i["checkInTime"].strftime("%H:%M:%S") ,
            "breakTime": i["breakTime"]+" mins","status":i["inIpRange"]
            }
            if(i["checkOutTime"] != None):
                res["out"] = i["checkOutTime"].strftime("%H:%M:%S")
            employee_data.append(res)
    return employee_data

