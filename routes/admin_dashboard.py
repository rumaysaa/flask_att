
from flask import Blueprint,render_template,session,redirect,jsonify
from modules.Admin_dashboard import *
from modules.Dashboard import *
from modules.Account import getAccountDetails
bp = Blueprint('adm_dash',__name__,)
from datetime import timedelta,datetime

@bp.route('/',methods=['get'])
def admin():
    adminID = session.get("admin_id")
    if(adminID == None):
        return redirect('/auth/login')
    active_users_data = getActiveEmployees()
    active_users_no = len(active_users_data)
    active_users_names = [i['name'] for i in getActiveEmployees()]
    allEmp = (db.Employees.find({}))
    inactive_users =  getInactiveEmployees(allEmp,active_users_data)
    inactive_users_no = len(inactive_users)
    inactive_users_details =  [getAccountDetails(i) for i in inactive_users]
    inactive_users_names=[]
    for i in inactive_users_details:
        inactive_users_names.append(i['fname']+" "+i['lname'])
    outside_working_no = 0
    outside_working_names = []
    for i in active_users_data:
        if i['status']==False or i['status'] == "":
            outside_working_no +=1
            outside_working_names.append(i['name'])
    projects_no = len(getProjects())
    data = getAllEmployeesAttendance()
    present_users = getPresentEmployees()
    return render_template('admin_dashboard.html',active_users_no=active_users_no,inactive_users_no=inactive_users_no,active_users_names=active_users_names,inactive_users_names=inactive_users_names,active_users_data=active_users_data,inactive_users_data=inactive_users_details,outside_working_no=outside_working_no,outside_working_names=outside_working_names,projects_no=projects_no,present_users=present_users)

@bp.route('/cal_working_hour',methods=['get'])
def cal_working_hour():
    adminID = session.get("admin_id")
    if(adminID == None):
        return redirect('/auth/login')
    active_users_data = getActiveEmployees()
    data=[]
    ch = list(get_todays_checked_out_att())
    for i in active_users_data:
        inT = i['in']
        outT= datetime.now().strftime("%H:%M:%S")
        (h, m,s) = inT.split(':')
        t1 = timedelta(hours=int(h), minutes=int(m))
        (h, m,s) = outT.split(':')
        t2 = timedelta(hours=int(h), minutes=int(m),seconds=int(s))
        totalhr = str(t2-t1)
        li = totalhr.split(":")
        li.pop(2)
        li = ".".join(li)
        data.append({"name":i['name'],"working_hrs":li})
    return jsonify(data)
    