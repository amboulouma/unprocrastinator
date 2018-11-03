from src.main import *

print('Unprocrastinator')
print()
print('A thousand tools to never procrastinate')
print()
while True:
    print('1- Create a task')
    print('2- View all tasks')
    print('3- Quit the program')
    choice = input('Your choice: ')
    print()
    if choice == '1':
        create_task()
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        print('Happy unprocrastination.')
        print()
        break
    else:
        print('Please provide a valid entry.')
        print()