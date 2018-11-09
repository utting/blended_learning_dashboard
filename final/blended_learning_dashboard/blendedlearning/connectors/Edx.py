from .models.Website import Website
from .models.Course import Course
from .models.Exercise import Exercise
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

#todo: 끔찍한 코드중복 없애기, explicit wait 사용.
class Edx(Website):
    def login_now(self, username, password):
        self.goto("Sign in or Register | edX")
        """ Navigates to login page and signs user in """
        self.get_driver().implicitly_wait(100)
        _driver = self.get_driver()
        _login_field = _driver.find_element_by_id("login-email")
        _password_field = _driver.find_element_by_id("login-password")
        _login_button = _driver.find_element_by_class_name("login-button")

        _login_field.send_keys(username)
        _password_field.send_keys(password)
        _login_button.click()

        print("Logging in {} into Edx",format(username))
        WebDriverWait(self.get_driver(), 10).until_not(EC.title_contains("Sign in"))
    
    def refresh_dict(self, course=None, only_completed=True):
        if course == None:
            course = self.default_course
        
        self.get_driver().get("https://www.edx.org/")
        _search_field = self.get_driver().find_element_by_class_name("react-autosuggest__input")
        _search_field.send_keys(course)
        self.get_driver().find_element_by_id("edit-submit-home-search").click()
        self.get_driver().find_element_by_css_selector("#search-results-section > div.js-card-list.filtered > div:nth-child(1) > div > a").click()
        
        self.get_driver().implicitly_wait(15) #wait until page loading
        sleep(1)
        self.get_driver().refresh()
        self.get_driver().find_element_by_css_selector(".btn.btn-cta.txt-center.js-enroll-btn.already-enrolled").click()
        
        _course_object = Course(self.domain, course)
        _all_button = self.get_driver().find_element_by_id("expand-collapse-outline-all-button")
        _all_button.click()
        _all_button.click()
        sleep(2)
        _lists = self.get_driver().find_elements_by_css_selector(".section-name.accordion-trigger")
        self.get_driver().implicitly_wait(1) 
        for i in _lists:
            i.click()
            sleep(1.5)
            for j in i.find_elements_by_xpath(".//../ol/li/button/span[contains(@class,'complete-checkmark')]"):
                _title = j.find_element_by_xpath(".//../h4").text
                exercise = Exercise(_title, self.get_domain(), parent_course=_course_object.get_name(), completed=True)
                _course_object.add_exercise(exercise)
                print(_title)
            if not only_completed:
                for exercise_name in [name.text for name in i.find_elements_by_xpath(".//../ol/li/button/h4")]:
                    exercise = Exercise(exercise_name, self.get_domain(), parent_course=_course_object.get_name())
                    _course_object.add_exercise(exercise)
                    print(exercise_name)
        self.add_course(_course_object)
        
    def search(self, course_name, amount=5):
        course_array = []
        self.get_driver().get("https://www.edx.org/course?search_query=" + course_name)
        self.get_driver().implicitly_wait(5)

        _courses = self.get_driver().find_elements_by_css_selector(".discovery-card.course-card.shadow.verified")
        if len(_courses) == 0:
            return None
        
        for i in range(amount):
            if i == len(_courses) - 1:
                break
            _name = _courses[i].find_element_by_xpath(".//div/div/h3").text
            _course_object = Course(self.domain, _name)
            course_array.append(_course_object)
        return course_array

    def register(self, email, password, username, firstname, lastname, telephone,school="unknown" ):
        self.get_driver().get("https://courses.edx.org/register")

        self.get_driver().find_element_by_xpath("//*[@id='register-email']").send_keys(email)
        self.get_driver().find_element_by_xpath("//*[@id='register-password']").send_keys(password)
        self.get_driver().find_element_by_xpath("//*[@id='register-name']").send_keys(firstname + lastname)
        self.get_driver().find_element_by_xpath("//*[@id='register-username']").send_keys(username)
        self.get_driver().find_element_by_xpath("//*[@id='register-country']/option[209]").click()
        self.get_driver().find_element_by_xpath("//*[@id='register']/button").click()
        
    def __init__(self, driver=None):
        super().__init__(domain="Edx")
        self.default_course = "Calculus 1A: Differentiation"
        self.create_driver(driver)
        self.add_url("Sign in or Register | edX", "https://courses.edx.org/login")
        self.add_url("edx", "https://www.edx.org/course")

if __name__ == "__main__":
    tester = Edx()
