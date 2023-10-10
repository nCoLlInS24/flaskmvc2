from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from flask.cli import with_appcontext, AppGroup

from App.models import Staff

from .index import index_views

student_view = Blueprint('student_views', __name__, template_folder='../templates')



# @staff_view.route('/reviews',method=["POST"])
# @login_required
# def createStaff():
#     data=request.json()
#     staff=Staff.create_staff(data['username'],data['password']);
#     if(staff):
#         return jsonify({"Account Created"}),201
#     else:  
#         return jsonify({"Username already exists"}),400



