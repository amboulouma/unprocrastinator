from ..classes.Task import Task

class TaskService:
    '''The task service class'''
    def __init__(self, connection, task):
        self.connection = connection
        self.task = task


    def create_task(self, connection, task):
        """
        Create a new task
        :param conn:
        :param task:
        :return:
        """

        sql = ''' INSERT INTO tasks(name, issuer, priority, deadline, is_done, done_date)
            VALUES(?,?,?,?,?,?) '''
        cursor = connection.cursor()
        cursor.execute(sql, task)
        return cursor.lastrowid