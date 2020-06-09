from invoke import task
import pickle

#initiating list for storing tasks and path to the file where it is exported
#if the file does not exists it will be created
task_list = []
file_path = 'test_storage'


def load_tasks(file):

    '''
    Loads tasks from external file into the list
    If the file does not exists it is created
    If there is nothing to import, an empty list is created
    '''

    global task_list

    try:
        with open(file, 'rb') as input_file:
            task_list = pickle.load(input_file)
    except EOFError:
        task_list = []
    except FileNotFoundError:
        #if the file does not exists, creates a new file
        f = open(file, 'wb')
        f.close()

def save_tasks(file):
    '''Save tasks to the external file'''

    with open(file, 'wb') as output_file:
        pickle.dump(task_list, output_file)

class Task:
    '''
    Class for creating tasks
    '''

    def __init__(self, name, deadline, description):
        '''
        Creator for task object

        Parameters:
            name - Name of the task
            deadline - How many days are left to do the task
            description - Short description of a task
            hash_value - Unique hash value calculated for all objects
        '''

        self.name = name
        self.deadline = deadline
        self.description = description
        self.hash_value = hash(self)

    def __str__(self):
        descr = "Name: {0}, Deadline: {1}, Description: {2}, Hash Value: {3}".format(self.name, self. deadline, self.description, self.hash_value)
        return descr


@task
def add(c, name, deadline, description):
    '''Function for adding task'''

    load_tasks(file_path)
    new_task = Task(name, deadline, description)
    task_list.append(new_task)
    save_tasks(file_path)

@task
def update(c, hash_value, name='', deadline='', description=''):
    '''
    Function for updating file
    hash_value is a default argument
    name, deadline and description are optional arguments
    '''

    load_tasks(file_path)

    if len(task_list) == 0:
        print("Task list is empty")
    else:
        for task in task_list:
            if task.hash_value == int(hash_value):
                if name:
                    task.name = name
                if deadline:
                    task.deadline = deadline
                if description:
                    task.description = description
            else:
                print("Task was not found")

    save_tasks(file_path)

@task
def remove(c, hash_value):
    '''
    Function for removing tasks
    hash_value is a default argument
    '''

    load_tasks(file_path)

    if len(task_list) == 0:
        print("Task list is empty")
    else:
        for task in task_list:
            if task.hash_value == int(hash_value):
                task_list.remove(task)
            else:
                print("Task was not found")

    save_tasks(file_path)

@task
def present(c, deadline='', all=False):
    '''
    Prints tasks in the command line
    deadline - specifies the range of the tasks that will be printed
    all - prints all the tasks
    '''

    load_tasks(file_path)

    if len(task_list) == 0:
        print("Task list is empty")
    else:
        if deadline:    
            for task in task_list:
                if int(task.deadline) <= int(deadline):
                    print(str(task))
        if all:
            for task in task_list:
                print(str(task))



        









