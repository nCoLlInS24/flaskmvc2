from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from flask.cli import with_appcontext, AppGroup
from App.controllers.staff import create_staff
from App.controllers.student import get_student

from App.models import Staff, Student

from App.controllers import addReview, get_staff_username
from App.models.user import User

from.index import index_views

staff_view = Blueprint('staff_view', __name__, template_folder='../templates')



@staff_view.route('/signup',methods=['POST'])
def createStaff():
    data=request.json()
    staff=Staff.create_staff(data['username'],data['password']);
    if(staff):
        return jsonify({"Account Created"}),201
    else:  
        return jsonify({"Username already exists"}),401



@staff_view.route('/getstaffByUsername/<username>',methods=['GET'])
@login_required
def getStaffByUsername(username):
    return get_staff_username(username)

@staff_view.route('/createReview',methods=['POST'])
@login_required
def createReview():
    data=request.json()
    staff=create_staff(username=data['username'],password=data['password'])
    if(staff):
        message={"message":"Account Created","code":201}
        return message
    else:  
        message={"message":"Username already exists","code":400}
        return message


@staff_view.route('/searchStudent',methods=["GET"])
@login_required
def searchStudent(id):
    student=get_student(id=id)
    
    if(student):
        message={"message":"Student found","code":"200"}
        print(student.get_json())
        return message
    else:
        message={"message":"Student not found","code":"400"}
        return message
    return None
    



@staff_view.route('/searchStudentName/<name>',methods=['GET'])
#@login_required
def getStudentName(name):
    user=User.query.filter_by(username=name).first()
    if user:
        return user.get_json()
    return None

@staff_view.route('/getStaffs',methods=['GET'])
def getStaffs():
    staffs=Staff.query.all()
    if not staffs:
        return []
    staffs=[staff.get_json for staff in staffs]
    return staffs

@staff_view.route('/signup', methods=["POST"])
def signupStaff():
    data=request.json()
    message=[]
    staff=create_staff(data["usernaem"],data["password"]);
    if(staff):
        message={"message":"Account Created","code":201}
        return message
    else:  
        message={"message":"Username already exists","code":400}
        return message
    return None