import sys

tasks = []

def add_task():
    tasks.append(input('Enter the task: '))

def remove_task():
    view_tasks()
    if tasks:
        try:
            index = int(input('Enter the task number to remove: ')) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
            else:
                print('Invalid task number.')
        except ValueError:
            print('Please enter a valid number.')

def view_tasks():
    if not tasks:
        print('No tasks in the list.')
        sys.exit()
    else:
        for task in tasks:
            print(task)
            sys.exit()

while True:
    print('\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit')
    choice = input('Select A Number: ')
    if choice == '1':
        add_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        break
    else:
        print('Invalid choice.')