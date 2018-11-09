"""
@author: B.Clark
"""

from .models.Website import Website
from .models.Course import Course
from .models.Exercise import Exercise
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PracticeIt(Website):


    def login_now(self, username, password):
        self.goto("Login - Practice-It")
        # Retrieve user email and password fields
        _login_form = self.get_driver().find_element_by_id("loginform")
        _email_field = _login_form.find_element_by_id("usernameoremail")
        _password_field = _login_form.find_element_by_id("userpassword")
        # Input users email
        self.enter_text(_email_field, username)
        # Input users password & submit login
        self.enter_text(_password_field, password, submit=True)
        print("Logging in {}".format(username))
        WebDriverWait(self.get_driver(), 10).until_not(EC.title_contains("Login"))


    def _course_listing(self):
        if self.get_driver().title != "Problems - Practice-It":
            self.goto("Problems - Practice-It")
        _page_content = self.get_driver().find_element_by_id("categories")
        _course_headings = _page_content.find_elements_by_xpath("//h4[@class='categorytoplevel']/a")
        _course_headings[len(_course_headings)-1].click()
        _course_areas = _page_content.find_elements_by_xpath("//ul[@class='categorylist']")
        for _course, _course_area in zip(_course_headings, _course_areas):
            self._course_ref[_course.text] = (_course, _course_area)


    def _get_chapters(self, course_object, only_completed=True):
        _course_name = course_object.get_name()
        if self.get_driver().title != "Problems - Practice-It":
            self.goto("Problems - Practice-It")
        print("Retrieving Chapters for {}".format(_course_name))
        if _course_name != "Javascript":
            self._course_ref.get(_course_name)[0].click()
        _chapters = self._course_ref.get(_course_name)[1]
        _chapter_headings = _chapters.find_elements_by_xpath("//li[@class='categoryli']/h4[@class='categorynested']/a")
        _chapter_counts = _chapters.find_elements_by_class_name("problemcount")
        _chapter_areas = _chapters.find_elements_by_xpath("//li[@class='categoryli']/ul[@class='categorylist']")
        for _chapter, _count, _chapter_area in zip(_chapter_headings, _chapter_counts, _chapter_areas):
            try:
                if not _count.text.find(r'/') == -1:
                    _contains_completed = True
                else:
                    _contains_completed = False
                if not _contains_completed and not only_completed:
                    break
                print("Retrieving Exercises for chapter {}".format(_chapter.text))
                _chapter.click()
                self._find_problems(course_object, _chapter_area, _contains_completed, only_completed)
                _chapter.click()
                self.get_driver().implicitly_wait(2)
            except:
                break


    def _find_problems(self, course_object, chapter, has_completed, only_completed=True):
        if has_completed:
            _solved_problems = chapter.find_elements_by_class_name("solvedproblem")
            for _solved in _solved_problems:
                exercise = Exercise(_solved.text, self.get_domain(), parent_course=course_object.get_name(), completed=True)
                course_object.add_exercise(exercise)
        if not only_completed:
            _problems = chapter.find_elements_by_class_name("problemlink")
            for _each in _problems:
                exercise = Exercise(_each.text, self.get_domain(), parent_course=course_object.get_name())
                course_object.add_exercise(exercise)


    def refresh_dict(self, course=None, only_completed=True):
        self.course_dict.clear()
        lang = "Java"
        if course is None:
            course = self.default_course
        self._course_listing()
        if course == "Javascript":
            _lang = "Javascript"
        _course_object = Course(self.domain, course, language=lang)
        self._get_chapters(_course_object, only_completed)
        self.add_course(_course_object)
    #리캡챠 우회해야함 
    def register(self, email, password, username, firstname, lastname, telephone,school="unknown" ):
        self.get_driver().get("https://practiceit.cs.washington.edu/user/create")
        self.get_driver().find_element_by_xpath("//*[@id='createfirstname']").send_keys(firstname)
        self.get_driver().find_element_by_xpath("//*[@id='createlastname']").send_keys(lastname)
        self.get_driver().find_element_by_xpath("//*[@id='createuseremail']").send_keys(email)
        self.get_driver().find_element_by_xpath("//*[@id='createusername']").send_keys(username)
        self.get_driver().find_element_by_xpath("//*[@id='createuserpassword']").send_keys(password)
        self.get_driver().find_element_by_xpath("//*[@id='createschoolselect']").send_keys(school+"\n")
        self.get_driver().find_element_by_xpath("//*[@id='createuseraccepttos']").click()
        self.get_driver().find_element_by_xpath("//*[@id='recaptcha-anchor']/div[5]").click()

    def search(self, course_name, amount=5):
        return None

    def __init__(self, driver=None):
        super().__init__(domain="Practice-It")
        self.default_course = "Building Java Programs, 4th edition"
        self.create_driver(driver)
        self.add_url("Login - Practice-It", "https://practiceit.cs.washington.edu/login")
        self.add_url("Problems - Practice-It", "https://practiceit.cs.washington.edu/problem/list")
        self._course_ref = {}




if __name__ == "__main__":
    tester = PracticeIt()
    tester.register("asdfasdfasdfasdf@asdfasdf.com",
        "fuckfuckfuck1234","phaphaphaphaphapha","Kafuu","Chino","+82 010 7560 0403")






