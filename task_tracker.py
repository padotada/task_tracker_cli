import sys
import os
import json
COMMAND = "task-cli"
file_path = "task_file.json"

def add_task(task_list: dict, item: str)->None:
    task_list.update({len(task_list)+1:item})
    with open(file_path, 'w') as f:
        json.dump(task_list, f, indent=4)
    print(f"Task added successfully (ID: {len(task_list)})")

def update_task_list(task_list: dict, task_id: int, new_item:str) -> None:
    task_list[task_id] = new_item
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
    
def print_task_list(task_list:dict) -> None:
    print(task_list)
    
def main():
    task_list = {}
    if os.path.isfile(file_path):
        with open(file_path, 'r') as json_file:
            task_list = json.load(json_file)
    # print(task_list)
    # print(f'Type a command in addition to {COMMAND}')
    if len(sys.argv) < 2:
        print('Try again.')
    else:
        cmd = sys.argv[1]
        if cmd == 'add':
            item = sys.argv[2]
            add_task(task_list, item)
            # print(task_list)
        elif cmd == 'update':
            item_id = int(sys.argv[2])
            new_item = sys.argv[3]
            update_task_list(task_list, item_id, new_item)
            
        elif cmd == 'delete':
            item_id = sys.argv[2]
            delete_task(task_list, item_id)
            
        elif cmd == 'mark-in-progress':
            pass
        elif cmd == 'mark-done':
            pass
        elif cmd == 'list':
            print_task_list(task_list)
        elif cmd == 'clear':
            clear_task_list(task_list)

if __name__ == '__main__':
    main()