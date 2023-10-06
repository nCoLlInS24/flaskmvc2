from App.models import Student
from App.database import db

def create_student(id,fname,lname):
    newstudent = Student(id=id, firstname=fname,lastname=lname)
    db.session.add(newstudent)
    # ReviewList.create_reviewList(student,review) do this when a review 
    db.session.commit()
    return newstudent

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users



# def update_user(id, username):
#     user = get_user(id)
#     if user:
#         user.username = username
#         db.session.add(user)
#         return db.session.commit()
#     return None
    