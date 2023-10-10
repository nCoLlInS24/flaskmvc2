from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from flask.cli import with_appcontext, AppGroup

from App.models import Staff

from.index import index_views

staff_view = Blueprint('staff_view', __name__, template_folder='../templates')

@staff_view.route('/getStaffs',methods=['GET'])
def getStaffs():
    staffs=Staff.query.all()
    return staffs

@staff_view.route('/signup',methods=['POST'])
@login_required
def createStaff():
    data=request.json()
    staff=Staff.create_staff(data['username'],data['password']);
    if(staff):
        return jsonify({"Account Created"}),201
    else:  
        return jsonify({"Username already exists"}),400



@staff_view.route('/getstaffByUsername/<username>',methods=['GET'])
@login_required
def getStaffByUsername(username):
    return get_staff_by_username(username)

@staff_view.route('/createReview',methods=['POST'])
@login_required
def createReview():
    data=request.json()
    review=addReview(data)
    if(review):
        return jsonify({"Review Posted"}), 201
    else:
        return jsonify({"Error"}),401


@staff_view.route('/searchStudent',methods=["GET"])
@login_required
def searchStudent(id):
    student=Student.get_student(id)
    if(student):
        print(student.get_json())
        return jsonify({"Student Found"}),201
    else:
        return jsonify({"Invalid Student Id Given"}),404

# @app.cli.command("getStaff")
# def getstaff(id):
#     return get_staff(id)

@staff_view.route('/getstaffByUsername/<username>',methods={'GET'})
@login_required
def getStaffByUsername(username):
    return get_staff_by_username(username)

@staff_view.route('/searchStudentName/<name>',methods=['GET'])
@login_required
def getStudentName(name):
    return User.query.filter_by(name)