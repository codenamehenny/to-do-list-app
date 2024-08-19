# For more information on features and requirements for the To Do List application, please use the README file.

complete_status = " - complete"
incomplete_status= " - incomplete"

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

# defines custom error for a list that is empty and the user wants to view it    
class EmptyListError(Exception):
    def __init__(self, message):
        self.message = message
        return None


# defines custom error for a task that's being marked complete more than once
class TaskComplete(Exception):
    def __init__(self, message):
        self.message = message
        return None
    
# this function is for adding a task to the to do list and uses another function to check if the task was already added
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

# this function displays the updated to do list and gives error if empty
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

#checks if task is in list and marks it complete, gives error if marked complete more than once, 
# gives error for wrong input type, and gives error if the task number is greater than the amount of tasks.
def mark_task_complete(index, to_do_list):
    index -= 1 
    try:
        if complete_status in to_do_list[index]:
            raise TaskComplete(f"\n{to_do_list[index]} was already marked complete. To delete choose option 4.")
        elif index <= len(to_do_list):
            to_do_list[index] = to_do_list[index].replace(incomplete_status, complete_status)
            print(f"\n{to_do_list[index]} status successful. Select option 2 for an updated list")
            return to_do_list 
    except ValueError:
        print("Please type the task number. You can find it in the list by choosing option 2.")
    except IndexError:
            print(f"\nThere are a total of {len(to_do_list)} tasks. Please choose a number under or equal to {len(to_do_list)}")     
    except TaskComplete as e:
        print(e.message)
    finally:
        print("Returning to menu...\n")

#this function checks if the task is in the list and gives an error if the task number is greater than amount of tasks
def remove_task(to_do_list, index):
    index -= 1
    try:
        if index <= len(to_do_list):
            removed_task = to_do_list.pop(index)
            print(f"{removed_task} has been removed from the To Do List.")
            return to_do_list
    except IndexError:
        print("\nLooks like we selected a number higher than the amount of tasks in the To Do List. Check the list by selecting option 2.")
    finally:
        print("Returning to menu...\n")
def to_do_list_main_function():
    to_do_list = []
    task = 0
    index = 0

    while True:
        print("\nWelcome to the To Do List App!\nMenu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark as complete")
        print("4. Delete a task")
        print("5. Quit")
        try:
            option = int(input("Enter option number: "))
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
        except ValueError:
            print("\nPlease follow the prompt carefully and try again with correct input type (text or number)")
        finally:
            print("Thanks for using the To Do List application! Go seize the day!")

to_do_list_main_function()