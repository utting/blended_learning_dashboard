from blendedlearning import db, login_manager
from flask_login import UserMixin

#intialisation function for login manager
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	student_id = db.Column(db.Integer, unique=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	# fname = db.Column(db.String(40), unique=False, nullable=False)
	# lname = db.Column(db.String(40), unique=False, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(100), unique=False, nullable=False)
	result = db.relationship('Exercise', backref='result', lazy=True)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}')"

class Exercise(db.Model):
	exercise_id = db.Column(db.Integer, primary_key=True, nullable=False)
	domain = db.Column(db.String(20), unique=True, nullable=True)
	student_id = db.Column(db.Integer, db.ForeignKey('user.student_id'), nullable=False)

	def __repr__(self):
		return f"Exercise('{self.exercise_id}', '{self.domain}')"
