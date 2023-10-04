from flask import Blueprint, request
from App.models import Staff
from App.models import User
from App.db import db


staff_view = Blueprint('staff_views', __name__, template_folder='../templates')



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
    return User.get_user(studid)

def search_student_by_name(username):
    return User.get_user_by_username(username)

def addReview():
    data=request.json()
    User.create_review(data['studentID'], data['rating'], data['review'])
    return 
    


