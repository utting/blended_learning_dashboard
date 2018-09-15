"""
@author: B.Clark
"""

class Exercise(object):
    """A basic python object to store exercise information in before saving to database"""

    def __init__(self, name, id=None, completed=False, topics=""):
        """
        Initializes the values for the newly created Exercise Object 
        :param name: Exercise Name.
        :param id: Unique Exercise ID.
        :param completed: Boolean value identifying if exercise is completed.
        :param topics: Exercise Topic (Optional)
        """
        self.name = name
        self.id = id
        self.completed = completed if type(completed) == bool else False
        self.topics = topics


    def get_name(self):
        return self.name


    def get_id(self):
        return self.id


    def get_completed(self):
        return self.completed


    def get_topics(self):
        return self.topics


    def set_id(self, id):
        self.id = id


    def set_completed(self, completed):
        if type(completed) == bool:
            self.completed = completed
        else:
            print("Please pass in a bool (True||False)")


    def set_topics(self, topics):
        self.topics = topics


    def __str__(self):
        return "{0} Name: {1}, ID: {2}, Completed: {3}, Topics: {4}".format(self.__class__,
                                                                            self.get_name(),
                                                                            self.get_id(),
                                                                            self.get_completed(),
                                                                            self.get_topics())
