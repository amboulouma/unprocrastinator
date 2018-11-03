from src.main import *

print('Unprocrastinator')
print()
while True:
    print('1- Create a task')
    print('2- View pending tasks')
    print('3- Quit the program')
    choice = int(input('Your choice: '))
    if choice == 1:
        create_task()
    elif choice == 2:
        show_tasks()
    elif choice == 3:
        print('Happy unprocrastination.')
        break
    else:
        print('Please provide a valid entry.')