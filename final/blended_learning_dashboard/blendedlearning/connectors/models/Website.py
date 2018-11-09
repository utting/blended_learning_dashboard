"""
@author: B.Clark
"""

from .Course import Course
from abc import ABC, abstractmethod
from selenium import webdriver

class Website(ABC):
    """A basic python website interface object to store course information in before saving to database"""

    def set_domain(self, domain):
        """ Set domain name of the website """
        self.domain = domain

        
    def get_domain(self):
        """ Returns domain name of website"""
        return self.domain


    def set_driver(self, driver):
        """ Set Webdriver for later refernce """
        self.driver = driver


    def get_driver(self):
        """ Returns Webdriver in use """
        return self.driver
    
    
    def add_url(self, url_title, url_link):
        """ Add given url to urls dict with the given title as the key """
        if url_title not in self.urls.keys():
            self.urls[url_title] = url_link
    
    
    def get_url(self, url_title):
        """ Returns url from urls who's title matches given url_title """
        if url_title in self.urls.keys():
            return (url_title, self.urls.get(url_title))
        
        
    def get_course_dict(self):
        """ Returns the entire course_dict to the user """
        return self.course_dict


    def get_course(self, course_name):
        """ Returns the Course Object from course_dict who's name matches given course_name """
        _existing = self.in_course_dict(course_name)
        if _existing:
            return self.course_dict.get(course_name)


    def in_course_dict(self, course_name):
        """ Checks if course_name is already in dictionary. Returns True if it is otherwise False """
        if course_name in self.course_dict.keys():
            return True
        else:
            return False


    def create_course(self, course_name,  language="Python", exercise_dict={}):
        """ Creates a Course Object of the given name and returns it to the user """
        _new_course = Course( self.get_domain(), course_name,  language, exercise_dict)
        return _new_course


    def add_course(self, course_object):
        """ Adds an already created Course Object to the course_dict """
        if (isinstance(course_object, Course)) & (not self.in_course_dict(course_object.name)):
            self.course_dict[course_object.name] = course_object


    def add_course_quickly(self, course_name,  language, exercise_dict):
        """ Creates new Course Object and adds in straight to the course_dict.
        Recommended only to use if you already have the entire exercise_dict for the course"""
        _new_course = self.create_course( course_name, language, exercise_dict)
        if not self.in_course_dict(_new_course):
            self.course_dict[_new_course.name] = _new_course
        

    def get_course_exercise_dict(self, course_title):
        """ Returns exercise list of given course """
        _current_course = self.get_course(course_title)
        return _current_course.get_exercise_dict()
        
     
        
    def enter_text(self, form_field, text, submit=False):
        """ Enter given text into the given field and optional submit """
        if not isinstance(text, str):
            text = str(text)
        # Input text into form
        form_field.click()
        form_field.clear()
        form_field.send_keys(text)
        # Submit form if submit=True
        if submit:
            form_field.submit()


    def goto(self, title):
        """ Searches urls dict for url who's key matches title. Title is also used for assertion """
        try:
            # Opens website
            self.get_driver().get(self.get_url(title)[1])
            assert title in self.driver.title
        except AssertionError as ae:
            print("Error: {} is not in driver.title ({})".format(title, self.get_driver.title))
            self.close()


    def close(self):
        self.get_driver().close()


    def create_driver(self, driver=None):
        """ Create Selenium Webdriver Object"""
        if driver is None:
            self.driver = webdriver.Chrome()
        else:
            self.driver = driver

    
    @abstractmethod
    def login_now(self, username, password):
        """ Navigates to login page and signs user in """
        pass

    @abstractmethod
    def refresh_dict(self, course=None, only_completed=True):
        """ This method should contain steps to populate the course_dict and the exercise_dict
        with the given course or if course equals None the default course, and its information ready for retrieval"""
        pass

    @abstractmethod
    def register(self, email, password, username, firstname, lastname, telephone,school="unknown" ):
        """register site"""
        pass

    @abstractmethod
    def search(self, course_name, amount=5):
        """
        상위 amount만큼 검색한거 읽어들여서 course의 배열 반환
        찾지 못했을시 None 반환 
        """
        pass
    def __init__(self, domain, driver=None, urls={}, course_dict={}, default_course=None):
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
        self.default_course = default_course
