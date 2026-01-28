# Task Tracker CLI

A simple command-line task tracker to manage your to-do list. Tasks are stored in a JSON file for persistence.

## Installation

1. Ensure you have Python 3 installed
2. Clone or download this repository
3. Navigate to the project directory
    ```bash
    cd "Task Tracker CLI"
    ```

## Usage

```bash
python3 task_tracker.py <command> [arguments]
```

## Commands

| Command | Description | Example |
|---------|-------------|---------|
| `add` | Add a new task | `python task_cli.py add "Buy groceries"` |
| `update` | Update a task's description | `python task_cli.py update 1 "Buy milk"` |
| `delete` | Delete a task | `python task_cli.py delete 1` |
| `mark-in-progress` | Mark a task as in progress | `python task_cli.py mark-in-progress 1` |
| `mark-done` | Mark a task as done | `python task_cli.py mark-done 1` |
| `list` | List all tasks | `python task_cli.py list` |
| `list todo` | List tasks with "todo" status | `python task_cli.py list todo` |
| `list in-progress` | List tasks in progress | `python task_cli.py list in-progress` |
| `list done` | List completed tasks | `python task_cli.py list done` |
| `clear` | Remove all tasks | `python task_cli.py clear` |

## Task Statuses

- `todo` - Task has not been started (default)
- `in-progress` - Task is currently being worked on
- `done` - Task is complete

## Data Storage

Tasks are saved to `task_file.json` in the same directory as the script.


## Install pytest if you haven't
pip install pytest

## Run all tests
pytest test_task_tracker.py -v

## Run with coverage report
pip install pytest-cov
pytest test_task_tracker.py --cov=task_cli --cov-report=term-missing

## Acknowledgments

This project is based on the [Task Tracker CLI](https://roadmap.sh/projects/task-tracker) challenge from [roadmap.sh](https://roadmap.sh).
