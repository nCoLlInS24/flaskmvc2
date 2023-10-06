from App.models import Student
from App.database import db

def create_student(id,fname,lname):
    newstudent = Student(id=id, firstname=fname,lastname=lname)
    db.session.add(newstudent)
    db.session.commit()
    return newstudent

def get_student(id):
    return Student.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def edit_karma(review):
    student=Student.query.get(review.student_id)
    if(review.isPositive==0):#if the review is negative
        student.karma-=1
    else:
        student.karma+=1
    return None


# def update_user(id, username):
#     user = get_user(id)
#     if user:
#         user.username = username
#         db.session.add(user)
#         return db.session.commit()
#     return None
    