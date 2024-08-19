complete_status = " - complete"
incomplete_status= " - incomplete"
to_do_list = []
#task = 0   

# defines custom exception for a task already in list
class TaskInListError(Exception):
    def  __init__(self, message):
        self.message = message
        return None

#function that checks whether the task is in the list and checks for inputs under than 3 characters
def check_task(task, to_do_list):
    if (task + incomplete_status) in to_do_list:
        raise TaskInListError(f"\nLooks like {task} is already on the list")
    elif len(task) < 3:
        raise InvalidEntry("Looks like a valid task wasn't entered. Please enter a task of 3 characters or more")


# defines custom exception that for inputs under 3 characters
class InvalidEntry(Exception):
    def  __init__(self, message):
        self.message = message
        return None
    
class EmptyListError(Exception):
    def __init__(self, message):
        self.message = message
        return None


# this function is for adding a task to the to do list
def add_task(to_do_list, task):
    try:
        check_task(task, to_do_list)
        if (task + incomplete_status) not in to_do_list:
            task = task + incomplete_status
            to_do_list.append(task)
            print(f"\n{task} has been added to your To Do List.")
        return to_do_list, task 
    except TaskInListError as e:
        print(e.message)
    except InvalidEntry as e:
        print(e.message)
    finally:
        print("Returning to menu...\n")

# this function displays the updated to do list
def display_task(to_do_list, task, index):
    try:
        if to_do_list:
            print("\nHere's your To Do List along with complete status:")
            for task in to_do_list:
                index += 1
                print(f"{index}. {task}")
        if not to_do_list:
            raise EmptyListError("\nYour Do List is empty. You can sit back and relax, or add a task.")
    except EmptyListError as e:
        print(e.message)
    finally:
        print("Returning to menu...\n")

def mark_task_complete(index, to_do_list):
    index -= 1 
    if index <= len(to_do_list):
        to_do_list[index] = to_do_list[index].replace(incomplete_status, complete_status)
        print(f"Complete status for {to_do_list[index]} successful. Select option 2 for an updated list")
    return to_do_list      


#this function checks if the task is in the list and removes it if it is
def remove_task(to_do_list, index):
    index -= 1
    if index <= len(to_do_list):
        removed_task = to_do_list.pop(index)
        print(f"{removed_task} has been removed from the To Do List.")
    else:
        print("That task was not in your To Do List.")
    return to_do_list

def to_do_list_main_function():
    #to_do_list = []
    task = 0
    index = 0

    while True:
        print("\nWelcome to the To Do List App!\nMenu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark as complete")
        print("4. Delete a task")
        print("5. Quit")
        option = int(input("Enter option number: "))
        try: 
            option = int(option)
            if option == 1:
                task = input("Enter the task: ")
                add_task(to_do_list, task)
            elif option == 2:
                display_task(to_do_list, task, index)
            elif option == 3:
                index = int(input("What's the task number you'd like to mark complete? "))
                mark_task_complete(index, to_do_list)
            elif option == 4:
                index = int(input("What's the task number you'd like to remove? "))
                remove_task(to_do_list, index)
            elif option == 5:
                print("Leaving main menu\n")
                break
        finally:
            print("Thanks for using the To Do List application! Go seize the day!")

to_do_list_main_function()