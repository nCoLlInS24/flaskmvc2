from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from flask.cli import with_appcontext, AppGroup

from App.models import Staff

from.index import index_views

staff_view = Blueprint('user_views', __name__, template_folder='../templates')


@staff_view.route('/getStaffs',method=['GET'])
def getStaffs():
    return Staff.query.all()


#@staff_view.route('/getStaff/<id>')
#def getstaff(id):
 #   return get_staff(id)

@staff_view.route('/getstaffByUsername/<username>')
def getStaffByUsername(username):
    return get_staff_by_username(username)

@staff_view.route('/createReview')
@login_required
def createReview():
    return addReview()

@staff_view.route('/searchStudent')
@login_required
def createReview():
    return addReview()

@app.cli.command("getStaff")
def getstaff(id):
    return get_staff(id)