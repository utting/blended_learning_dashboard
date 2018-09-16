"""
@author: B.Clark
"""

from models.Exercise import Exercise

class Course(Exercise):
    """A basic python course object to store course information in before saving to database"""

    def __init__(self, domain, course_name, language="Python", exercise_dict={}):
        """
        Initializes the values for the newly created Course Object

        :param course_name: Name of Course
        :param language: Programming Langauge of course
        :param exercise_dict: a dictionary with {key=exercise_name : value=exercise_object}
        """
        super().__init__(course_name, domain)
        self.language = language
        self.exercise_dict = exercise_dict


    def get_language(self):
        """ Returns the programming language of the course """
        return self.language


    def set_language(self, language):
        """ Sets the programming language of the course """
        self.language = language


    def get_exercise_dict(self):
        """ Returns the exercise_dict of the course """
        return self.exercise_dict


    def in_exercise_dict(self, exercise_name):
        """ Checks if exercise_name is already in dictionary. Returns True if it is otherwise False """
        if exercise_name in self.exercise_dict.keys():
            return True
        else:
            return False


    def create_exercise(self, exercise_name, exercise_id=None, exercise_completed=False, execise_topics=""):
        """ Creates a Exercise Object of the given name and returns it to the user """
        self.new_exercise = Exercise(exercise_name, self.get_domain(), self.get_name(), exercise_id, exercise_completed, execise_topics)
        return self.new_exercise


    def add_exercise(self, exercise_object):
        """ Adds an already created Course Object to the course_dict """
        if (isinstance(exercise_object, Exercise)) & (not self.in_exercise_dict(self.new_exercise)):
            self.exercise_dict[exercise_object.name] = exercise_object


    def add_exercise_quickly(self, exercise_name, exercise_id=None, exercise_completed=False, execise_topics=""):
        """ Creates new Exercise Object and adds in straight to the exercise_dict.
                Recommended only to use if you already all required info of the exercise"""
        self.new_exercise = self.create_exercise(exercise_name, exercise_id, exercise_completed, execise_topics)
        if not self.in_exercise_dict(self.new_exercise):
            self.exercise_dict[self.new_exercise.name] = self.new_exercise


    def __str__(self):
        """ String representation of this object. Useful for debugging or printing """
        return "Course Name: {}, Domain: {}, ID: {}, Completed: {}, Langauage: {}, Topics: {}," \
               "    Exercise Dict Keys: {}".format(self.get_name(),
                                                   self.get_domain(),
                                                   self.get_id(),
                                                   self.get_completed(),
                                                   self.get_language(),
                                                   self.get_topics(),
                                                   self.exercise_dict.keys())