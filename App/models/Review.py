class Review(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    studentID = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer,nullable=True)
    review = db.Column(db.String(200),nullable=True)


    def __init__(self,studentID, rating, review):
        self.studentID = studentID
        self.rating=rating
        self.review=review


    def get_json(self):
        return{
            'id': self.id,
            'rating':self.rating,
            'review':self.review
        }

    def set_rating(self, rating):
        self.rating = rating

    def set_review(self, review):
        self.review = review

    def create_review(studid, rating, comment):
        review = Review(studid,rating,comment)
        db.session.add(review)
        db.session.commit()
        return


