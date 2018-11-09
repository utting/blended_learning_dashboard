"""
@author: B.Clark
"""

class Exercise(object):
    """A basic python object to store exercise information in before saving to database"""

    def __init__(self, name, domain, parent_course=None, id=None, completed=False, topics=""):
        """
        Initializes the values for the newly created Exercise Object
        :param name: Exercise Name.
        :param domain: Name of website where exercise is located
        :param parent_course: Name of course where exercise is located
        :param id: Unique Exercise ID.
        :param completed: Boolean value identifying if exercise is completed.
        :param topics: Exercise Topic (Optional)
        """
        self.name = name
        self.domain = domain
        self.parent_course = parent_course
        self.id = id
        self.completed = completed if type(completed) == bool else False
        self.topics = topics

    def get_parent_course(self):
        """ Returns the course_name where exercise can be found """
        return self.parent_course


    def set_parent_course(self, parent):
        """ Sets the name of the parent_course"""
        self.parent_course = parent


    def set_domain(self, domain_name):
        """ Set domain name of where exercise can be found """
        self.domain = domain_name


    def get_domain(self):
        """ Returns the domain where exercise can be found """
        return self.domain


    def get_name(self):
        """ Returns the exercise name """
        return self.name


    def get_id(self):
        """ Returns the value of id for exercise """
        return self.id


    def get_completed(self):
        """ Returns if exercise has been completed or not """
        return self.completed


    def get_topics(self):
        """ Returns the topics of the exercise object """
        return self.topics


    def set_id(self, id):
        """ Set Unique id for Exercise Object """
        self.id = id


    def set_completed(self, completed):
        """ Set whether an exercise has been completed of not """
        if type(completed) == bool:
            self.completed = completed
        else:
            print("Please pass in a bool (True||False)")


    def set_topics(self, topics):
        """ Set the topic of the Exercise """
        self.topics = topics


    def __str__(self):
        """ String representation of this object. Useful for debugging or printing """
        return "{} Name: {}, Domain: {}, ID: {}, Completed: {}, Topics: {}".format(self.__class__,
                                                                                    self.get_name(),
                                                                                    self.get_domain(),
                                                                                    self.get_id(),
                                                                                    self.get_completed(),
                                                                                    self.get_topics())
