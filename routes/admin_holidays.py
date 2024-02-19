from flask import Blueprint,render_template,url_for,redirect,request

from modules.Admin_holidays import *

bp = Blueprint('adm_holidays',__name__,)

@bp.route('/',methods=['get'])
def view_holidays():
    adminID = session.get("admin_id")
    if(adminID == None):
        return redirect('/auth/login')
    return render_template('admin_create_holidays.html')

@bp.route('/create',methods=['get','post'])
def create_holidays():
    create_holiday(request.form)
    return redirect(url_for('.view_holidays'))