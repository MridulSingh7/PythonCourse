"""
 Challenge: Terminal-Based Task List Manager

Create a Python script that lets users manage a to-do list directly from the terminal.

Your program should:
1. Allow users to:
   - Add a task
   - View all tasks
   - Mark a task as completed
   - Delete a task
   - Exit the app
2. Save all tasks in a text file named `tasks.txt` so data persists between runs.
3. Display tasks with an index number and a ✔ if completed.

Example menu:
1. Add Task  
2. View Tasks  
3. Mark Task as Completed  
4. Delete Task  
5. Exit

Example output:
Your Tasks:

Buy groceries||not_done
Finish Python project||done
Read a || book||not_done


Bonus:
- Prevent empty tasks from being added
- Validate task numbers before completing/deleting
"""

import os #we will use os functions to check valid paths
TASK_FILE = "tasks.txt" #name of the file you want to open

def load_tasks():
    tasks = [] #created an empty list to hold all the tasks
    if(os.path.exists(TASK_FILE)): #only runs if there is a file tastks.txt in the given path inside parantheses
        with open(TASK_FILE, 'r', encoding="utf-8") as f: #open it as reading, openingf and refering to it as f
            for line in f: #we iterate in the file line by line aise
                text, status = line.strip().rsplit("||", 1) #rsplit = right side split, 1 means only one time from the right 
                tasks.append({"text": text, "done": status == "done"}) #appending every task jo text form me tha into a list
    return tasks #returning the list which has all the task and its status

def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f: #opening a file in write mode, encoding is always utf8
        for task in tasks:
            status = "done" if task["done"] else "not_done" #sabka status determine karlo
            f.write(f"{task['text']}||{status}\n") #writing on the file jaisa pattern bola hai waisa 


def display_tasks(tasks):
    if not tasks:
        print(f"NO tasks found") #handling empty task array
    else:
        for i, task in enumerate(tasks, 1):
            checkbox = "✅" if task["done"] else " " #formatting the output of displaying according to the question stated
            print(f"{i}. [{checkbox}] {task['text']}")
    print()


#main function
def task_manager():
    tasks = load_tasks()#pehle we store all the tasks in the task list from the load_task function

    while True:
        print("\n------Task List Manager -------")
        print("1. Add task")
        print("2. View Tasks")
        print("3. Mark Task as complete")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5)").strip()

        match choice: #switch case wala same chiz hai
            case "1":
                text = input("Enter your task").strip()
                if text:
                    tasks.append({"text":text, "done": False})
                    save_tasks(tasks)
                else:
                    print("Task cannot be empty")

            case "2":
                display_tasks(tasks)
            case "3":
                display_tasks(tasks)
                try:
                    num = int(input("Enter task number"))
                    if 1 <= num <= len(tasks):
                        tasks[num-1]["done"] = True
                        save_tasks(tasks)
                        print("task marked as DONE")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Please enter a number")
            case "4":
                display_tasks(tasks)
                try:
                    num = int(input("Enter task number to delete"))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num-1)
                        save_tasks(tasks)
                        print(f"task removed {removed['text']}")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Please enter a number")
            case "5":
                print("Exiting task Manager")
                break
            case _:
                print("Please choose a valid option")

task_manager()#running the function

'''
important : file i/o, using os , rsplit and etc
'''