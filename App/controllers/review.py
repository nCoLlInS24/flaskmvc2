from App.models import Review
from App.database import db

def create_review(student_id,staff_id,rating,isPositive,text):
    review = Review(student_id,staff_id,rating,isPositive,text)
    db.session.add(review)
    db.session.commit()
    return review


def get_review_by_id(id):
    return Review.query.get(id)

def get_all_reviews(staff_id):#get all reviews for a specific staff
    reviews=Review.query.filter_by(staffId=staff_id).all()
    if not reviews:#if no reviews then return empty string
        return[]
    reviews_of= [review.get_json() for review in reviews]

# def get_all_users_json():
#     users = User.query.all()
#     if not users:
#         return []
#     users = [user.get_json() for user in users]
#     return users

# def update_review(id, username):
#     user = get_user(id)
#     if user:
#         user.username = username
#         db.session.add(user)
#         return db.session.commit()
#     return None
    

