class Task:
    '''The Task class with its attributes'''
    def __init__(self, id, name, issuer, priority, deadline, is_done=False, done_date):
        self.id = id
        self.name = name
        self.issuer = issuer
        self.priority = priority
        self.deadline = deadline
        self.is_done = is_done
        self.done_date = done_date