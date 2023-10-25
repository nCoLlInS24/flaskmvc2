import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import db, create_db
from App.models import User

import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup


from App.controllers.staff import(
    Staff,
    create_staff
)

app = create_app()
migrate = get_migrate(app)

LOGGER = logging.getLogger(__name__)

staff_test=AppGroup("staff",help='Tests Staff functions')


class StaffUnitTests(unittest.TestCasse):
    @staff_test.command("create_Staff", help='Test create Staff function')
    @click.argument("username", default="rob")
    @click.argument("password", default="robpass")
    def create_staff_test(username,password):
        user = Staff(username, password)
        assert user.username == "rob"


    def update_staff_username_test(new_id,username):
    staff=get_staff(new_id)
    if staff:
        staff.username=username
        db.session.add(staff)
        db.session.commit(staff)
    assert staff.username=="bill"



app.cli.add_command(staff)