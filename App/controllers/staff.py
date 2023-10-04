from App.models import Staff
from App.models import User
from App.db import db

def create_staff(username,password):
    newStaff=Staff(username,password)
    db.session.add(newStaff)
    db.session.commit()
    return newStaff

def get_staff(id):
    return Staff.query.get(id)

def get_staff_username(username):
    return Staff.query.filter_by(username)

def update_staff_username(id,username):
    staff=get_staff(id)
    if staff:
        staff.username=username
        db.session.add(staff)
        return db.session.commit(staff)
    return None

def update_staff_password(id,password):
    staff=get_staff(id)
    if staff:
        staff.password=password
        db.session.add(staff)
        return db.session.commit(staff)
    return None

def search_student(studid):
    return get_user(studid)

def search_student_by_name(username):
    return get_user_by_username(username)

def addReview():
    
    data=request.json()
    create_review(data['studentID'], data['rating'], data['review'])
    return message="Review Submitted"
    
@staff_controller.route('/logon')
def logon(username, password):
    staff=Staff.get_staff_username(username)
    if staff:
        if staff.password==password:
            return message="Logged in"
    return None


@staff_controller.route('/view_all', method='GET')
@login_required
def getStaff():
    staffs=Staff.query.all()
    return jsonify(staffs)

