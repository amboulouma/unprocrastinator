import datetime
import pprint

from ..classes.Task import Task


class TaskService:
    '''The task service class'''
    def __init__(self, connection):
        self.connection = connection

    def create_task(self, task):
        """
        Create a new task
        :param self:
        :param task:
        :return:
        """
        with self.connection:
            sql = ''' INSERT INTO tasks(name, issuer, priority, deadline, is_done, done_date)
                    VALUES(?,?,?,?,?,?) '''
            cursor = self.connection.cursor()
            cursor.execute(sql, task)
            return cursor.lastrowid


    def update_task(self, task_id, priority, deadline):
        """
        update priority and deadline of a task
        :param self:
        :param task:
        :return: task id
        """

        with self.connection:
            sql = ''' UPDATE tasks
                    SET priority = ? ,
                    deadline = ? 
                    WHERE id = ?'''
            cursor = self.connection.cursor()
            cursor.execute(sql, task_id, priority, deadline)
            return cursor.lastrowid


    def task_done(self, task_id):
        """
        update is_done and done_date  of a task
        :param self:
        :param task:
        :return: project id
        """

        with self.connection:
            sql = ''' UPDATE tasks
                    SET is_done = ? ,
                    done_date = ?
                    WHERE id = ?'''
            cursor = self.connection.cursor()
            cursor.execute(sql, True, str(datetime.datetime.now().date().strftime('%d/%m/%Y')), task_id)
            return cursor.lastrowid


    def show_tasks(self):
        """
        showing the list of tasks
        :param self:
        """

        with self.connection:
            sql = ''' select * from tasks'''
            cursor = self.connection.cursor()
            cursor.execute(sql)
            print(cursor.fetchall())