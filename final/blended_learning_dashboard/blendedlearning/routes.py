from flask import render_template, url_for, flash, redirect, request
from blendedlearning import app, db, bcrypt
from blendedlearning.forms import RegistrationForm, LoginForm
from blendedlearning.models import User, Exercise
from flask_login import login_user, current_user, logout_user, login_required
# from .connectors.Collector import Collector
from .Collector import Collector
from selenium import webdriver



#class Result(db.Model):
	




post = [
	{
		'author': 'random author',
		'title': 'first post',
		'content': 'first post content'
	},
	{
		'author': 'second author',
		'title': 'second post',
		'content': 'second post content'
	}
]

@app.route('/')
def default():
	return "<h1>hello world<h1>"

@app.route('/home')
def home():
    return render_template('home.html', posts=post)

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title='Profile')



@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		# Hash Password
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		# Add register info and hashed password to database
		user = User(student_id=form.student_id.data, username=form.username.data, 
					email=form.email.data, password=hashed_password,
					first_name=form.first_name.data, last_name=form.last_name.data,
					telephone=form.telephone.data)

		register_driver = Collector()
		register_driver.dynamic_register(user.email, user.password, user.username, user.first_name, user.last_name,user.telephone)


		print(user.password)
		
		db.session.add(user)
		db.session.commit()
		#flash success message
		flash('Account created!', 'success')
		#redirect to login page
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():

	# If username & password are the same for all sites
	#collect = Collector("username@student.usc.edu.au", "password")  # Change to username and password of student
	# If empty Collector constructor called add username & password seperately
	# collect = Collector()
	# collect.add_login("domain", "username", "password")
	# collect.add_login("Datacamp", "username", "password")
	# collect.add_login("Practice-It", "username", "password")
	# collect.get_results(only_completed=True)
	# for exercise in collect.exercises:
		# print(exercise)


	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		#pull user from database based on email entered
		user = User.query.filter_by(email=form.email.data).first()
		#compare user's entered password and stored password
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			#Direct user to whatever page they clicked the login button
			#from when successfully loging in
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login unsuccessful.', 'danger')
	return render_template('login.html', title='login', form=form)

@app.route('/logout')
def logout():	
	logout_user()
	return redirect(url_for('login'))
