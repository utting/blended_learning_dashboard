"""
@author: B.Clark
"""

from Exercise import Exercise

class Course(Exercise):
    """A basic python course object to store course information in before saving to database"""

    def __init__(self, domain, course_name, language="Python", exercise_dict={}):
        """
        Initializes the values for the newly created Course Object
        :param domain: Name of website where course is located
        :param course_name: Name of Course
        :param language: Programming Langauge of course
        :param exercise_dict: a dictionary with {key=exercise_name : value=exercise_object}
        """
        super().__init__(course_name)
        self.domain = domain
        self.language = language
        self.exercise_dict = exercise_dict


    def get_domain(self):
        return self.domain


    def get_language(self):
        return self.language


    def set_language(self, language):
        self.language = language


    def get_exercise_dict(self):
        return self.exercise_dict


    def in_dict(self, exercise_name):
        if exercise_name in self.exercise_dict.keys():
            return True
        else:
            return False


    def create_exercise(self, exercise_name, exercise_id=None, exercise_completed=False, execise_topics=""):
        self.new_exercise = Exercise(name=exercise_name, id=exercise_id, completed=exercise_completed, topics=execise_topics)
        return self.new_exercise


    def add_exercise(self, exercise_object):
        if (isinstance(exercise_object, Exercise)) & (not self.in_dict(self.new_exercise)):
            self.exercise_dict[exercise_object.name] = exercise_object


    def add_exercise_quickly(self, exercise_name, exercise_id=None, exercise_completed=False, execise_topics=""):
        self.new_exercise = Exercise(name=exercise_name, id=exercise_id, completed=exercise_completed, topics=execise_topics)
        if not self.in_dict(self.new_exercise):
            self.exercise_dict[self.new_exercise.name] = self.new_exercise


    def __str__(self):
        return "Course Name: {}, Domain: {}, ID: {}, Completed: {}, Langauage: {}, Topics: {}," \
               "    Exercise Dict Keys: {}".format(self.get_name(),
                                                   self.get_domain(),
                                                   self.get_id(),
                                                   self.get_completed(),
                                                   self.get_language(),
                                                   self.get_topics(),
                                                   self.exercise_dict.keys())