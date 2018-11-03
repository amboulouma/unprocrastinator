from datetime import datetime

class Task:
    '''The Task class with its attributes'''
    def __init__(self, name, issuer='', priority=0, is_done=False):
        self.name = name
        self.issuer = issuer
        self.priority = priority
        self.is_done = is_done

    def tuple_form(self):
        return self.name , self.issuer, self.priority, self.is_done, 