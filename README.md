To Do list Application Project Features and Requirements
-- Overview --
The To Do List Application is a simple command line tool that helps users manage their tasks. The
program uses Python functions to perform each tasks like add, view, mark tasks as complete, and delete. 
It also includes error handling to ensure a smooth and efficent user experience.

-- Features --
1. Add a Task:
        - Users can add new tasks to their to-do list
        - Each task is marked as "incomplete" by default
        - The program checks if a tasks already exists before adding it
2. View Tasks:
        - Users can view all tasks along with their completion status
        - If the list is empty, the program will notify the user
3. Mark a Task as Complete:
        - Users can mark tasks as complete
        - If a task is alreadt marked as complete, the program  will notify the user
        - The program checks if the entered task number is within the valid range
4. Delete a Task:
        - Users can delete a task from the list
        - The program ensures the task number is within range, providing an 
                error messafe if the number is invalid
5. Error Handling
        - The program uses try-exceot blocks to manage errors and invalid inputs
        - Includes handling for invalid task numbers, incorrect input types, and 
                attempts to mark a task as complete multiple times

-- Requirements --
Python 3.x

-- Usage --
1. Run the Program:
        - Execute the script from the command line using python3 ToDoList.py
2. Menu Options:
        - The Main Menu provides options to add, view, mark complete, delete tasks,
                or quit the program
        - Use the corresponding numbers to navigate through the options

-- Example Menu -- 
Welcome to the To Do List App!
Menu:
1. Add a task
2. View tasks
3. Mark as complete
4. Delete a task
5. Quit

-- Contributing -- 
Contributions are welcoemd to improve the To Do List Application! Here's how you can help:
1. Fork the repository: Start by forking this repository to your Github account

2. Clone the Forked Repository:
git clone https://github.com/codenamehenny/to-do-list-app.git

3. Create a New Branch: create a new branch for your feature or bug fix
git checkout -b feature-name

4. Make Changes: Implement your feature, bug fix, or improve documentation

5. Commit your Changes:
git commit -m "desc. of changes"

6. Push to your Forked Repository:
git push origin feature-name

7. Submit a Pull Request: Open a pull request to the main repository.
Please provide a detailed description of your changes and reasons for them

8. Review and Feedback: Your pull request will be reviewed. Once approved,
your contribution will be merged

~ Any questions or feedback please send to genesis09m@hotmail.com