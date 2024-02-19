from flask import Blueprint,render_template,session,redirect
from modules.Account import getAccountDetails
from modules.Dashboard import getHeaderInfo
from modules.Admin_noti import getNotificationDetails
from modules.Admin_holidays import getHolidayDetails
from modules.Admin_events import getEventDetails
bp = Blueprint('noti',__name__,)

@bp.route('/', methods=['get'])
def noti():
    empID = session.get("employee_id")
    if(empID == None):
        return redirect('/auth/login')
    data = getAccountDetails(empID)
    header_info = getHeaderInfo(data['fname'])
    notifications = getNotificationDetails()
    no_noti = len(notifications)
    no_holi =  len(getHolidayDetails())
    no_event = len(getEventDetails())
    return render_template('index.html',header_info=header_info,notis=notifications,acc_data=data ,page='notifications.html',no_noti=no_noti,no_holi=no_holi,no_event=no_event)