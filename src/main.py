import sqlite3

from .models.services.TaskService import TaskService
from .models.classes.Task import Task

connection = sqlite3.connect('../../unprocrastinator.db')
task_service = TaskService(connection)

def create_task():
    while True:
        print()
        print('Create a new task')
        print('1- Creation with name and issuer')
        print('2- Full creation')
        print('3- Quit menu')
        choice = int(input('Your choice: '))
        if choice == 1:
            name = input('Name: ')
            issuer = input('Issuer: ')
            task = Task(name=name, issuer=issuer)
            choice = input(task.tuple_form() + '[Y/n]')
            if choice is not 'n':
                try:
                    task_service.create_task(task)
                    print('Task' + task.tuple_form() + 'has successfully been saved.')
                except:
                    print('An error has occured when saving the task.')
        elif choice == 2:
            name = input('Name: ')
            issuer = input('Issuer: ')
            priority = input('Priority: ')
            deadline = input('Deadline: ')
            task = Task(name=name, issuer=issuer, priority=priority, deadline=deadline)
            choice = input(task.tuple_form() + '[Y/n]')
            if choice is not 'n':
                try:
                    task_service.create_task(task)
                    print('Task' + task.tuple_form() + 'has successfully been saved.')
                except:
                    print('An error has occured when saving the task.')
        elif choice == 3:
            break
        else:
            print('Please provide a valid entry.')

def show_tasks():
    print()
    print('Pending Tasks')
    task_service.show_tasks()