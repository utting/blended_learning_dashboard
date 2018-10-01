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

    def get_results(self, driver=None):
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
            _website_object.refresh_dict(_website_object.default_course)
            _course_exercise = _website_object.get_course_exercise_dict(_website_object.default_course).values()
            for _each in _course_exercise:
                self.exercises.append(_each)
            _website_object.close()
        return self.exercises



if __name__ == "__main__":
    try:
        driver = webdriver.Firefox()
        # If username & password are the same for all sites
        collect = Collector("username", "password")
        # If username & password are different
        # collect.add_login("domain", "username", "password")
        # collect.add_login("domain", "username", "password")
        collect.get_results(driver)
        for exercise in collect.exercises:
            print(exercise)
    finally:
        driver.close()
