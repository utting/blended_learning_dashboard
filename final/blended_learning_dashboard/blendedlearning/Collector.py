"""
@author: B.Clark
"""

import os
import importlib
from selenium import webdriver
import blendedlearning.connectors as conn
# from models.Website import Website
# from models.Exercise import Exercise

class Collector():
    def __init__(self, default_user="", default_password=""):
        # print(os.listdir())
        self.file_list = [file for file in os.listdir("blendedlearning/connectors") if file.endswith(".py")]
        # print(self.file_list)
        self.login_dict = {}
        self.default_user = default_user
        self.default_password = default_password
        self.exercises = []

    def add_login(self, domain, username, password):
        self.login_dict[domain] = (username, password)


    def get_login(self, domain):
        return self.login_dict.get(domain)


    def get_user(self, domain):
        return self.login_dict.get(domain)[0]


    def get_password(self, domain):
        return self.login_dict.get(domain)[1]


    def dynamic_importer(self, file_name):
        _name = file_name[:-3]
        _tester_object = importlib.__import__("blendedlearning.connectors." + _name)
        # for item in dir(_tester_object):
        #     print(item)
        # print(_tester_object)
        _class_name = getattr(_tester_object, "connectors")
        # for item in dir(_class_name):
        #     print(item)
        _class = getattr(_class_name, _name)
        _class = getattr(_class, _name)
        # print(_class)
        return _class
    def search_courses(self, course_name, driver=None, amount=5):
        pass
    def get_results(self, driver=None, only_completed=True):
        self.exercises.clear()
        for file in self.file_list:
            _class = self.dynamic_importer(file)
            _website_object = _class(driver)
            if file in self.login_dict.keys():
                _user = self.get_user(file)
                _pass = self.get_password(file)
            else:
                _user = self.default_user
                _pass = self.default_password
            _website_object.login_now(_user, _pass)
            _website_object.refresh_dict(only_completed=only_completed)
            _course_exercise = _website_object.get_course_exercise_dict(_website_object.default_course).values()
            for _each in _course_exercise:
                self.exercises.append(_each)
            _website_object.close()
        return self.exercises
    
    def dynamic_register(self, email, password, username, firstname, lastname, telephone, school="unknown", driver=None ):
        for file in self.file_list:
            _class = self.dynamic_importer(file)
            _website_object = _class(driver)
            _website_object.register(self, email, password, username, firstname, lastname, telephone, school="unknown")
            _website_object.close()


if __name__ == "__main__":
    # If username & password are the same for all sites
    collect = Collector("username", "password")
    # If username & password are different
    # collect.add_login("domain", "username", "password")
    # collect.add_login("domain", "username", "password")
    collect.get_results(None, only_completed=True)
    for exercise in collect.exercises:
        print(exercise)
