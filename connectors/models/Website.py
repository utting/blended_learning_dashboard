"""
@author: B.Clark
"""

from Course import Course
from abc import ABC, abstractmethod
from selenium import webdriver

class Website(ABC):
    """A basic python website interface object to store course information in before saving to database"""


    def __init__(self, domain, driver=None, urls={}, course_dict={}):
        """
        Initializes the values for the newly created Website Object 
        :param domain: Name of website
        :param driver: quick reference for selenium driver
        :param urls: a dictionary with {key=url_title : value=url_link}
        :param course_dict: a dictionary with {key=course_name : value=course_object}
        """
        self.domain = domain
        self.driver = driver
        self.urls = urls
        self.course_dict = course_dict


    def set_domain(self, domain):
        self.domain = domain

        
    def get_domain(self):
        return self.domain


    @abstractmethod
    def create_driver(self):
        pass


    def set_driver(self, driver):
        self.driver = driver


    def get_driver(self):
        return self.driver
    
    
    def add_url(self, url_title, url_link):
        if url_title not in self.urls.keys():
            self.urls[url_title] = url_link
    
    
    def get_url(self, url_title):
        if url_title in self.urls.keys():
            return (url_title, self.urls.get(url_title))
        
        
    def get_course_dict(self):
        return self.course_dict


    def get_course(self, course_name):
        self.existing = self.in_dict(course_name)
        if self.existing:
            return self.course_dict.get(course_name)


    def in_dict(self, course_name):
        if course_name in self.course_dict.keys():
            return True
        else:
            return False


    def create_course(self, course_name,  language="Python", exercise_dict={}):
        self.new_course = Course(course_name=course_name,  language="Python", exercise_dict={})
        return self.new_course


    def add_course(self, course_object):
        if (isinstance(course_object, Course)) & (not self.in_dict(self.new_course)):
            self.course_dict[course_object.name] = course_object


    def add_course_quickly(self, course_name,  language="Python", exercise_dict={}):
        self.new_course = Course(course_name=course_name,  language="Python", exercise_dict={})
        if not self.in_dict(self.new_course):
            self.course_dict[self.new_course.name] = self.new_course
        

    def get_course_exercise_list(self, course_title):
        self.current_course = self.get_course(course_title)
        return self.current_course.get_exercise_list()
        
     
        
    def enter_text(form_field, text, submit=False):
        if not isinstance(text, str):
            text = str(text)
        # Input text into form
        form_field.click()
        form_field.clear()
        form_field.send_keys(text)
        # Submit form if submit=True
        if submit:
            form_field.submit()


    def goto(url, title):
        try:
            # Opens website
            self.get_driver.get(url)
            assert title in self.driver.title
        except AssertionError as ae:
            print("Error: {} is not in driver.title ({})".format(title, self.get_driver.title))
            self.get_driver.close()

    
    @abstractmethod
    def login_now(self):
        pass