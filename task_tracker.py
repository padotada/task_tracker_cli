import sys
import os
import json
from datetime import date, datetime

COMMAND = "task-cli"
file_path = "task_file.json"

def add_task(task_list: dict, item: str)->None:
    task_list.update({len(task_list)+1:{"description":item, "status":"todo"}})
    with open(file_path, 'w') as f:
        json.dump(task_list, f, indent=4)
    print(f"Task added successfully (ID: {len(task_list)})")

def update_task_list(task_list: dict, task_id: str, new_item:str) -> None:
    task_list[task_id].update({"description":new_item})
    with open(file_path, 'w') as f:
        json.dump(task_list, f, indent=4)
    print(f"Task {task_id} updated successfully")

def delete_task(task_list: dict, task_id: str) -> None:
    try:
        task_list.pop(task_id)
        with open(file_path, 'w') as f:
            json.dump(task_list, f, indent=4)
    except KeyError:
        print("This task id doesn't exist")
    else:
        print(f"Task {task_id} deleted successfully")
    
def clear_task_list(task_list: dict) -> None:
    task_list.clear()
    with open(file_path, 'w') as f:
        json.dump(task_list, f, indent=4)

def mark_in_progress(task_list: dict, item_id: str) -> None:
    if len(task_list) == 0:
        print("There is no task to mark as in progress.")
    else:
        task_list[item_id].update({"status":"in-progress"})
        with open(file_path, 'w') as f:
            json.dump(task_list, f, indent=4)
        print(f"Task {item_id} has been marked as in progress.")
        
        
def mark_as_done(task_list: dict, item_id: str) -> None:
    if len(task_list) == 0:
        print("There is no task to mark as done.")
    else:
        task_list[item_id].update({"status":"done"})
        with open(file_path, 'w') as f:
            json.dump(task_list, f, indent=4)
        print(f"Task {item_id} has been marked as done.")


def print_task_list(task_list: dict) -> None:
    print("-------------------------------")
    if len(task_list) == 0:
        print("No tasks to print")
    else:
        for key, value in task_list.items():
            print(f'Key: {key}, Task: {value["description"]}, Status: {value["status"]}')
    print("-------------------------------")

def print_done_tasks(task_list: dict) -> None:
    print("-------------------------------")
    if len(task_list) == 0:
        print("No tasks to print")
    else:
        for key, value in task_list.items():
            if value["status"] == "done":
                print(f'Key: {key}, Task: {value["description"]}, Status: {value["status"]}')
    print("-------------------------------")

def print_tasks_in_progress(task_list: dict) -> None:
    print("-------------------------------")
    if len(task_list) == 0:
        print("No tasks to print")
    else:
        for key, value in task_list.items():
            if value["status"] == "in-progress":
                print(f'Key: {key}, Task: {value["description"]}, Status: {value["status"]}')
    print("-------------------------------")

def print_tasks_todo(task_list: dict) -> None:
    print("-------------------------------")
    if len(task_list) == 0:
        print("No tasks to print")
    else:
        for key, value in task_list.items():
            if value["status"] == "todo":
                print(f'Key: {key}, Task: {value["description"]}, Status: {value["status"]}')
    print("-------------------------------")

def main():
    task_list = {}
    if os.path.isfile(file_path):
        with open(file_path, 'r') as json_file:
            task_list = json.load(json_file)
    # print(f'Type a command in addition to {COMMAND}')
    if len(sys.argv) < 2:
        print('Try again.')
    else:
        cmd = sys.argv[1].lower().strip()
        if cmd == 'add':
            item = sys.argv[2]
            add_task(task_list, item)
        elif cmd == 'update':
            item_id = sys.argv[2]
            new_item = sys.argv[3]
            update_task_list(task_list, item_id, new_item)
            
        elif cmd == 'delete':
            item_id = sys.argv[2]
            delete_task(task_list, item_id)
            
        elif cmd == 'mark-in-progress':
            item_id = sys.argv[2]
            mark_in_progress(task_list, item_id)
            
        elif cmd == 'mark-done':
            item_id = sys.argv[2]
            mark_as_done(task_list, item_id)
        elif cmd == 'list':
            if len(sys.argv) == 2:
                print_task_list(task_list)
            else:
                second_cmd = sys.argv[2].lower().strip()
                if second_cmd == 'done':
                    print_done_tasks(task_list)
                elif second_cmd == 'todo':
                    print_tasks_todo(task_list)
                elif second_cmd == 'in-progress':
                    print_tasks_in_progress(task_list)
                else:
                    print("Invalid command.")
        elif cmd == 'clear':
            clear_task_list(task_list)
        
        else:
            print("This is not a valid command. Try again.")

if __name__ == '__main__':
    main()