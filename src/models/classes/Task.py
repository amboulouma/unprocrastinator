class Task:
    '''The Task class with its attributes'''
    def __init__(self, name, issuer=None, priority=None, deadline=None, is_done=False, done_date=None):
        self.name = name
        self.issuer = issuer
        self.priority = priority
        self.deadline = deadline
        self.is_done = is_done
        self.done_date = done_date
