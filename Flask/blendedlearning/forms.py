from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blendedlearning.models import User

class RegistrationForm(FlaskForm):
	student_id = StringField('Student ID',
								validators=[DataRequired(), Length(min=7, max=8)])
	username = StringField('Username', 
								validators=[DataRequired(), Length(min=5, max=10)])
	email = StringField('Email',
							validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password',
											validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_student_id(self, student_id):
		user = User.query.filter_by(student_id=student_id.data).first()
		if user:
			raise ValidationError('ID is already in use.')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Username taken.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email taken.')

	


class LoginForm(FlaskForm):
	email = StringField('Email',
							validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')