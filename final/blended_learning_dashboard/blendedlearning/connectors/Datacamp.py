"""
@author: B.Clark & M.Utting
"""

from .models.Website import Website
from .models.Course import Course
from .models.Exercise import Exercise
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Datacamp(Website):

    def login_now(self, username, password):
        self.goto("Sign in | DataCamp")
        # Navigates to login page and signs user in
        _user_email = self.get_driver().find_element_by_id("user_email")
        _user_password = self.get_driver().find_element_by_id("user_password")
        # Input users email
        self.enter_text(_user_email, username)
        # Input users password & submit login
        self.enter_text(_user_password, password, submit=True)
        print("Logging in {} into Datacamp".format(username))
        WebDriverWait(self.get_driver(), 10).until_not(EC.title_contains("Sign in"))

    def refresh_dict(self, course=None, only_completed=True):
        """ This method should contain steps to populate the course_dict and the exercise_dict
        with the given course or if course equals None the default course, and its information ready for retrieval"""
        self.course_dict.clear()
        if course is None:
            course = self.default_course
        self.get_driver().get("https://www.datacamp.com/courses")
        _search_field = self.get_driver().find_element_by_css_selector(".dc-input--text.search__textfield.js-focus-eol")
        _search_field.send_keys(course)
        _search_field.submit()
        _course_link = self.get_driver().find_element_by_css_selector(
            ".course-block__link.ds-snowplow-link-course-block").get_attribute("href")
        _course_link = _course_link.replace("https://www.datacamp.com/", "http://campus.datacamp.com/")
        _course_object = Course(self.domain, course)
        self.get_driver().get(_course_link)
        _dc_nav_course = self.get_driver().find_element_by_class_name("dc-nav-course__container")
        sleep(1)
        _dc_nav_course.click()
        _expand = self.get_driver().find_elements_by_class_name("expand-text")
        for _link in _expand:
            if _link.text == "View Chapter Details":
                _link.click()
        _completed_exercises = self.get_driver().find_elements_by_css_selector(
            ".course-outline__exercise.modal--exercise__completed")
        try:
            _is_current_completed = self.get_driver().find_element_by_css_selector(
                ".course-outline__exercise.modal--exercise__current.modal--exercise__completed")
            if _is_current_completed.size != 0:
                _completed_exercises.append(_is_current_completed)
        except:
            pass
        if not len(_completed_exercises) == 0:
            for _completed in _completed_exercises:
                _name = _completed.find_element_by_class_name("modal--exercise-title")
                exercise = Exercise(_name.text, self.get_domain(), parent_course=_course_object.get_name(),
                                    completed=True)
                _course_object.add_exercise(exercise)
        if not only_completed:
            _exercises = self.get_driver().find_elements_by_class_name("modal--exercises")
            for _exs in _exercises:
                _list = _exs.find_elements_by_class_name("modal--exercise-title")
                for _item in _list:
                    exercise = Exercise(_item.text, self.get_domain(), parent_course=_course_object.get_name())
                    _course_object.add_exercise(exercise)
        self.add_course(_course_object)

    def log_out(self):
        # Log out
        _user_info = self.get_driver().find_element_by_class_name("header-user")
        _user_info.click()
        _user_progress = self.get_driver().find_element_by_link_text("Log Out")
        _user_progress.click()
        self.close()

    def register(self, email, password, username, firstname, lastname, telephone, school="unknown"):
        self.get_driver().get("https://www.datacamp.com/users/sign_up")
        _email = self.get_driver().find_element_by_xpath("//*[@id='user_email']")
        _password = self.get_driver().find_element_by_xpath("//*[@id='user_password']")
        _email.send_keys(email)
        _password.send_keys(password)
        _password.submit()
        self.get_driver().find_element_by_xpath("//*[@id='user_first_name']").send_keys(firstname.title())
        self.get_driver().find_element_by_xpath("//*[@id='user_last_name']").send_keys(lastname.title())
        self.get_driver().find_element_by_xpath("//*[@id='user_education']").send_keys(school)
        self.get_driver().find_element_by_xpath("//*[@id='user_company_role']").send_keys("student")
        self.get_driver().find_element_by_xpath("//*[@id='user_phone']").send_keys("+82 " + telephone)
        self.get_driver().find_element_by_xpath('//*[@id="ds-snowplow-form-onboarding"]/div[2]/input').click()

    def search(self, course_name, amount=5):
        course_array = []
        self.get_driver().get("http://www.datacamp.com/courses/q:" + course_name)
        self.get_driver().implicitly_wait(5)
        _courses = self.get_driver().find_elements_by_css_selector(".course-block__link.ds-snowplow-link-course-block")
        if len(_courses) == 0:
            return None
        for i in range(amount):
            if i == len(_courses) - 1:
                break
            _name = _courses[i].find_element_by_xpath(".//div[@class='course-block__body']/h4").text
            _course_object = Course(self.domain, _name)
            course_array.append(_course_object)
        return course_array

    def __init__(self, driver=None):
        super().__init__(domain="Datacamp")
        self.default_course = "Cleaning Data in Python"
        self.create_driver(driver)
        self.add_url("Sign in | DataCamp", "http://www.datacamp.com/users/sign_in")
        self.add_url("Datacamp", "http://campus.datacamp.com/courses/")


if __name__ == "__main__":
    tester = Datacamp()
    try:
        tester.login_now("username", "password")
        # tester.get_driver().implicitly_wait(5)
        tester.refresh_dict(tester.default_course)
        exercises = tester.get_course_exercise_dict(tester.default_course).values()
        for each in exercises:
            print(each)
    finally:
        tester.close()
