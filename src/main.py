import sqlite3

from models.services.TaskService import TaskService

connection = sqlite3.connect('../../unprocrastinator.db')

cursor = connection.cursor()
