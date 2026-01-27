import sys

COMMAND = "task-cli"


def add_task(task_list: list, item: str)->None:
    task_list.append(item)
    print(f"Task added successfully (ID: {len(task_list)})")

def update_task_list(task_list: list, task_id: int, new_item:str) -> None:
    task_list[task_id-1] = new_item
    print(f"Task {task_id} updated successfully")

def delete_task(task_list: list, task_id: int) -> None:
    try:
        task_list.pop(task_id-1)
    except IndexError:
        print("This task id doesn't exist")
    
    print(f"Task {task_id} deleted successfully")
    
def clear_task_list(task_list) -> None:
    task_list.clear()
    
def print_task_list(task_list:list) -> None:
    print(task_list)
    
def main():
    task_list = []
    # print(f'Type a command in addition to {COMMAND}')
    if len(sys.argv) < 2:
        print('Try again.')
    else:
        cmd = sys.argv[1]
        if cmd == 'add':
            item = sys.argv[2]
            add_task(task_list, item)
            print(task_list)
        elif cmd == 'update':
            item_id = int(sys.argv[2])
            new_item = sys.argv[3]
            update_task_list(task_list, item_id, new_item)
            
        elif cmd == 'delete':
            item_id = int(sys.argv[2])
            new_item = sys.argv[3]
            delete_task(task_list, item_id)
            
        elif cmd == 'mark-in-progress':
            pass
        elif cmd == 'mark-done':
            pass
        elif cmd == 'list':
            print_task_list(task_list)

if __name__ == '__main__':
    main()