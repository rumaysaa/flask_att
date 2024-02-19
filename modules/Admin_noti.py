
import pymongo
from modules.Config_db import *
from datetime import datetime,date,timedelta


def createNotification(data):
    print(data)
    noti = db.Notifications.insert_one({
        "notification" : data,
        "dateTime" : datetime.now()
        })
    noti = str(noti.inserted_id)
    return noti

def getNotificationDetails():
    data = db.Notifications.find({}).sort('dateTime', -1)
    formated_data = None
    #print("data",len(list(data)),len(list(data)) != '0')
    if(data != None):
        formated_data=[]
        for i in data:
            dateTime =  i['dateTime'].strftime('%A, %d. %B %Y %I:%M%p')
            # convert string to datetime
            dt1 = datetime.strptime(str(i['dateTime']), "%Y-%m-%d %H:%M:%S.%f")
            dt2 = datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f")
            # difference between datetime in timedelta
            delta = dt2 - dt1
            print(f'Difference is {delta.days} days')
            if(delta.days == 0):
                dateTime = "Today"
            elif(delta.days == 1):
                dateTime = "Yesterday"
            #print(dateTime,date.now() - i['dateTime'].date())
            formated_data.append({
                "notification" :i['notification'],
                "dateTime" : dateTime
            })
    return formated_data