import sqlite3
import os.path

from .models.services.TaskService import *
from .models.classes.Task import Task

def create_task():
    print('Create a new task')
    name = input('Name: ')
    issuer = input('Issuer: ')
    priority = input('Priority: ')
    task = Task(name=name, issuer=issuer, priority=priority)
    choice = input('Is the entry {} valid? [Y/n]'.format(task.tuple_form()))
    if choice is not 'n':
        try:
            create_task_service(task.tuple_form())
            print('Task {} has successfully been saved.'.format(task.tuple_form()))
        except:
            print('An error has occured while saving the task.')
        print()


def show_tasks():
    print('Pending Tasks')
    try:
        show_tasks_service()
    except :
        print('An error has occured while saving the task.')
    print()
        