from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dcb70cbd518ad94337ec795ee3b15bb4'
#app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\users\ USERNAME \documents\blendedlearning/site.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from blendedlearning import routes
