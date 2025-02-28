from App.models import Review
from App.models import ReviewList
from App.database import db
from flask import jsonify

def create_review(student_id,staff_id,rating,isPositive,text):
    review = Review(student_id,staff_id,rating,isPositive,text)
    db.session.add(review)
    ReviewList.add_review(review.id,student_id)
    db.session.commit()
    return review


def get_review_by_id(new_id):
    return Review.query.get(new_id)

def get_all_reviews(staff_id):#get all reviews for a specific staff
    reviews=Review.query.filter_by(staffId=staff_id).all()
    if not reviews:#if no reviews then return empty string
        return[]
    else:
        reviews_of= [review.get_json() for review in reviews]
        return jsonify(reviews_of)


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
    

