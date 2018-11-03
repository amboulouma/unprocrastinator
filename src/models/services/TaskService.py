import datetime
import pprint
import os
import sqlite3

from ..classes.Task import Task


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "../../../unprocrastinator.db")

connection = sqlite3.connect(db_path)

def create_task_service(task):
    """
    Create a new task
    :param task:
    :return:
    """
    with connection:
        sql = ''' INSERT INTO tasks(name, issuer, priority, is_done)
                VALUES(?,?,?,?) '''
        cursor = connection.cursor()
        cursor.execute(sql, task)
        return cursor.lastrowid


def update_task_service(task_id, priority):
    """
    update priority of a task
    :param priority:
    :return: task id
    """

    with connection:
        sql = ''' UPDATE tasks
                SET priority = ? ,
                WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, task_id, priority)
        return cursor.lastrowid


def task_done_service(task_id):
    """
    update is_done and done_date  of a task
    :param task:
    :return: project id
    """

    with connection:
        sql = ''' UPDATE tasks
                SET is_done = ? ,
                done_date = ?
                WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, True, task_id)
        return cursor.lastrowid


def show_tasks_service():
    """
    showing the list of tasks
    :param 
    """
    with connection:
        sql = ''' select * from tasks'''
        cursor = connection.cursor()
        cursor.execute(sql)
        print(cursor.fetchall())