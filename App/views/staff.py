from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required
from App.models import Staff



@staff_view.route('/logon')
def logon(username, password):
    staff=Staff.get_staff_username(username)
    if staff:
        


@staff_view.route('/view_all', method='GET')
@login_required
def getStaff():
    staffs=Staff.query.all()
    return jsonify(staffs)
