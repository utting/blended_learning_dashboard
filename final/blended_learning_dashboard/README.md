Blended Learning Dashboard
==========

The goal of the Blended Learning App is to apply theoretical knowledge in a practical manner to create a dashboard that
 future USC ICT students will use to access learning sites, and visually monitor their progress in order to learn
  information on key programming concepts. The app aims to automates account creation and login processes to allow
   students to spend more time learning instead of account management.

## Getting Started

### Prerequisites

To run this package the following dependancies are required to be install:

 - python 3
 - flask
 - flask_sqlalchemy
 - flask_bcrypt
 - flask_login
 - flask_wtf
 - wtforms
 - selenium
 - geckodriver

### Setting-up

Setup the database by running the create_db.py script or call the following command from within the blended_learning_dashboard directory

```
python create_db.py
```

### Running

To run the blended learning dashboard run the run.py script or call the following command from within the blended_learning_dashboard directory

```
python run.py
```

Then open your web browser and navigate to localhost:5000/

## Files

### Database
 * site.db - database file
 * run.py - script to run the webapp
 * create_db.py - create database file
 * forms.py - custom form classes
 * models.py - mapping for information in database
 * routes.py - defines web routes available in the webapp
 * static - contains static files for webapp
 * templates - contains custom html files for webapp

### Connectors

 * Collector.py - dynamic class in charge of communications between web connectors and the rest of the webapp
 * PracticeIt.py - web connector for [Practice-It](https://www.practiceit.cs.washington.edu/)
 * Edx.py - web connector for [Edx](https://www.edx.org/)
 * DataCamp.py - web connector for [Datacamp](https://www.datacamp.com/)

#### Models

 * Website.py - abstract class for learning web connectors
 * Course.py - custom class to model information associated with online courses
 * Exercise.py - custom class to model information for individual exercises found on online courses

## Built With

* [Python 3](https://www.python.org/) - A high-level programming language
* [Flask](http://flask.pocoo.org/) - A microframework for Python based on Werkzeug and Jinja 2
* [Selenium](https://selenium-python.readthedocs.io/) - Used to automate web browser interaction from Python.

## Author & Contributor List

* [Brock Clark](https://github.com/usc-bac021)
* [Francis Kang](https://github.com/Franciskkang)
* [Robert Studdock](https://github.com/RStuddock)
* [Mark Utting](https://github.com/utting)
