Install Package requirements: flask, flask_sqlalchemy, flask_bcrypt, flask_login, flask_wtf, wtforms,

1. Open command line
2. Change directory to inside flask folder of blended_learning_dashboard folder
3. type: 

   Python
	 >>> from blendedlearning import db
	 >>> from blendedlearning.models import User, Exercise
	 >>> db.create_all()
	 >>> quit()
	 python run.py

4. Inside browser navigate to localhost:5000/home
