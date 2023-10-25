import click, pytest, sys
from App.controllers.staff import get_staff
from App.models import db, Staff,Review,Student,ReviewList
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users,create_staff )

# This commands file allow you to create convenient CLI commands for testing controllers

api='https://97mm2.sse.codesandbox.io/teachers/'


app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    db.drop_all()
    db.create_all()

    create_staff("rob","robpass")
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_staff(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

@test.command("staff", help="Runs Staff Tests")
@click.argument("type", default="unit")
def staff_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "StaffUnitTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))


app.cli.add_command(test)


staff_test=AppGroup("staff",help='Tests Staff functions')

@staff_test.command("create_staff", help='Test create Staff function')
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_staff_test(username,password):
    staff = create_staff(username, password)
    assert staff.username == "rob"


@staff_test.command("update", help='Test update Staff function')
@click.argument("new_id",default=1)
@click.argument("username",default="billy")
def update_staff_username_test(new_id,username):
    staff=get_staff(new_id)
    if staff:
        staff.username=username
        db.session.add(staff)
        db.session.commit()
    assert staff.username=="billy"

app.cli.add_command(staff_test)

app.cli.add_command(test)