
from modules.Config_db import *
import pymongo
from datetime import datetime,timedelta

def createEvent(request):
    
    event = db.Events.insert_one({
        "title": request['event-title'],
        "start": datetime.fromisoformat(request['start-date']) ,
        "end": datetime.fromisoformat(request['end-date']),
        "backgroundColor": request['event-colo']
    })
    return event.inserted_id

def getEventDetails():
    events = list(db.Events.find({}))
    data=[]
    for i in events:
        data.append({
        "id" : str(i["_id"]),
        "title": i['title'],
        "start":  str(datetime.strptime(str(i['start']), '%Y-%m-%d %H:%M:%S').date()),
        "end":  str(datetime.strptime(str(i['end']), '%Y-%m-%d %H:%M:%S').date() + timedelta(days=1)),
        "backgroundColor": i['backgroundColor']
        })
        #print(data)
    return data
   