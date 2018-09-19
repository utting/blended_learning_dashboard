"""
@author: B.Clark & M.Utting
"""

from models.Website import Website
from models.Course import Course
from models.Exercise import Exercise
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Datacamp(Website):

    def login_now(self, username, password):
        self.goto("Sign in | DataCamp")
        """ Navigates to login page and signs user in """
        _user_email = self.get_driver().find_element_by_id("user_email")
        _user_password = self.get_driver().find_element_by_id("user_password")
        # Input users email
        self.enter_text(_user_email, username)
        # Input users password & submit login
        self.enter_text(_user_password, password, submit=True)
        _user_password.submit()
        print("Logging in {} into Datacamp".format(username))
        WebDriverWait(self.get_driver(), 10).until_not(EC.title_contains("Sign in"))


    def refresh_dict(self, course):
        """ This method should contain steps to populate the course_dict and the exercise_dict
        with the given course or if course equals None the default course, and its information ready for retrieval"""
        self.course_dict.clear()
        if course is None:
            course = self.default_course
        _split_name = course.lower().replace('(', ' ').replace('(', ' ').split()
        _course_name = "-".join(_split_name)
        _course_link = "{}{}".format(self.get_url("Datacamp")[1],
                                     _course_name)
        print(_course_link)
        _course_object = Course(self.domain, course)
        self.get_driver().get(_course_link)
        _dc_nav_course = self.get_driver().find_element_by_class_name("dc-nav-course__container")
        _dc_nav_course.click()
        _expand = self.get_driver().find_elements_by_class_name("expand-text")
        for _link in _expand:
            if _link.text == "View Chapter Details":
                _link.click()
        _completed_exercises = self.get_driver().find_elements_by_class_name("course-outline__exercise modal--exercise__completed")
        if not len(_completed_exercises) == 0:
            for _completed in _completed_exercises:
                _name = _completed.find_element_by_class_name("modal--exercise-title")
                exercise = Exercise(_name.text, self.get_domain(), parent_course=_course_object.get_name(), completed=True)
                _course_object.add_exercise(exercise)
        _exercises = self.get_driver().find_elements_by_class_name("modal--exercises")
        for _exs in _exercises:
            _list = _exs.find_elements_by_class_name("modal--exercise-title")
            for _item in _list:
                exercise = Exercise(_item.text, self.get_domain(), parent_course=_course_object.get_name())
                _course_object.add_exercise(exercise)
        self.add_course(_course_object)

        # # # Now log out
        # _user_info = self.get_driver().find_element_by_class_name("header-user")
        # _user_info.click()
        # _user_progress = self.get_driver().find_element_by_link_text("Log Out")
        # _user_progress.click()
        # self.close()


    def __init__(self, driver=None):
        super().__init__(domain="Datacamp")
        self.default_course = "Cleaning Data in Python"
        self.create_driver(driver)
        self.add_url("Sign in | DataCamp", "http://www.datacamp.com/users/sign_in")
        self.add_url("Datacamp", "http://campus.datacamp.com/courses/")



if __name__ == "__main__":
    try:
        tester = Datacamp()
        tester.login_now("username", "password")
        # tester.get_driver().implicitly_wait(5)
        tester.refresh_dict(tester.default_course)
        exercises = tester.get_course_exercise_dict(tester.default_course).values()
        for each in exercises:
            print(each)
    finally:
        tester.close()




