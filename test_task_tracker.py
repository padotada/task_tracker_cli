import pytest
import os
import json
from unittest.mock import patch
from task_tracker import (
    add_task,
    update_task_list,
    delete_task,
    clear_task_list,
    mark_in_progress,
    mark_as_done,
    print_task_list,
    print_done_tasks,
    print_tasks_in_progress,
    print_tasks_todo,
    main,
    file_path
)


@pytest.fixture
def empty_task_list():
    return {}


@pytest.fixture
def sample_task_list():
    return {
        "1": {"description": "Buy groceries", "status": "todo"},
        "2": {"description": "Walk the dog", "status": "in-progress"},
        "3": {"description": "Finish project", "status": "done"}
    }


@pytest.fixture
def cleanup_json():
    """Remove the JSON file after each test if it exists."""
    yield
    if os.path.isfile(file_path):
        os.remove(file_path)


class TestAddTask:
    def test_add_task_to_empty_list(self, empty_task_list, cleanup_json, capsys):
        add_task(empty_task_list, "New task")
        
        assert len(empty_task_list) == 1
        assert empty_task_list["1"]["description"] == "New task"
        assert empty_task_list["1"]["status"] == "todo"
        
        captured = capsys.readouterr()
        assert "Task added successfully (ID: 1)" in captured.out

    def test_add_multiple_tasks(self, empty_task_list, cleanup_json):
        add_task(empty_task_list, "First task")
        add_task(empty_task_list, "Second task")
        
        assert len(empty_task_list) == 2
        assert empty_task_list["2"]["description"] == "Second task"

    def test_add_task_persists_to_file(self, empty_task_list, cleanup_json):
        add_task(empty_task_list, "Persistent task")
        
        assert os.path.isfile(file_path)
        with open(file_path, 'r') as f:
            saved_data = json.load(f)
        assert "1" in saved_data or 1 in saved_data


class TestUpdateTask:
    def test_update_existing_task(self, sample_task_list, cleanup_json, capsys):
        update_task_list(sample_task_list, "1", "Updated groceries")
        
        assert sample_task_list["1"]["description"] == "Updated groceries"
        
        captured = capsys.readouterr()
        assert "Task 1 updated successfully" in captured.out

    def test_update_preserves_status(self, sample_task_list, cleanup_json):
        original_status = sample_task_list["2"]["status"]
        update_task_list(sample_task_list, "2", "New description")
        
        assert sample_task_list["2"]["status"] == original_status

    def test_update_nonexistent_task(self, sample_task_list, cleanup_json):
        with pytest.raises(KeyError):
            update_task_list(sample_task_list, "99", "This should fail")


class TestDeleteTask:
    def test_delete_existing_task(self, sample_task_list, cleanup_json, capsys):
        delete_task(sample_task_list, "1")
        
        assert "1" not in sample_task_list
        
        captured = capsys.readouterr()
        assert "Task 1 deleted successfully" in captured.out

    def test_delete_nonexistent_task(self, sample_task_list, cleanup_json, capsys):
        delete_task(sample_task_list, "99")
        
        captured = capsys.readouterr()
        assert "This task id doesn't exist" in captured.out


class TestClearTaskList:
    def test_clear_removes_all_tasks(self, sample_task_list, cleanup_json):
        clear_task_list(sample_task_list)
        
        assert len(sample_task_list) == 0

    def test_clear_empty_list(self, empty_task_list, cleanup_json):
        clear_task_list(empty_task_list)
        
        assert len(empty_task_list) == 0


class TestMarkInProgress:
    def test_mark_task_in_progress(self, sample_task_list, cleanup_json, capsys):
        mark_in_progress(sample_task_list, "1")
        
        assert sample_task_list["1"]["status"] == "in-progress"
        
        captured = capsys.readouterr()
        assert "Task 1 has been marked as in progress" in captured.out

    def test_mark_in_progress_empty_list(self, empty_task_list, capsys):
        mark_in_progress(empty_task_list, "1")
        
        captured = capsys.readouterr()
        assert "There is no task to mark as in progress" in captured.out


class TestMarkAsDone:
    def test_mark_task_done(self, sample_task_list, cleanup_json, capsys):
        mark_as_done(sample_task_list, "1")
        
        assert sample_task_list["1"]["status"] == "done"
        
        captured = capsys.readouterr()
        assert "Task 1 has been marked as done" in captured.out

    def test_mark_done_empty_list(self, empty_task_list, capsys):
        mark_as_done(empty_task_list, "1")
        
        captured = capsys.readouterr()
        assert "There is no task to mark as done" in captured.out


class TestPrintFunctions:
    def test_print_empty_list(self, empty_task_list, capsys):
        print_task_list(empty_task_list)
        
        captured = capsys.readouterr()
        assert "No tasks to print" in captured.out

    def test_print_all_tasks(self, sample_task_list, capsys):
        print_task_list(sample_task_list)
        
        captured = capsys.readouterr()
        assert "Buy groceries" in captured.out
        assert "Walk the dog" in captured.out
        assert "Finish project" in captured.out

    def test_print_done_tasks(self, sample_task_list, capsys):
        print_done_tasks(sample_task_list)
        
        captured = capsys.readouterr()
        assert "Finish project" in captured.out
        assert "Buy groceries" not in captured.out

    def test_print_in_progress_tasks(self, sample_task_list, capsys):
        print_tasks_in_progress(sample_task_list)
        
        captured = capsys.readouterr()
        assert "Walk the dog" in captured.out
        assert "Finish project" not in captured.out

    def test_print_todo_tasks(self, sample_task_list, capsys):
        print_tasks_todo(sample_task_list)
        
        captured = capsys.readouterr()
        assert "Buy groceries" in captured.out
        assert "Walk the dog" not in captured.out

    def test_print_done_empty_list(self, empty_task_list, capsys):
        print_done_tasks(empty_task_list)
        
        captured = capsys.readouterr()
        assert "No tasks to print" in captured.out

    def test_print_in_progress_empty_list(self, empty_task_list, capsys):
        print_tasks_in_progress(empty_task_list)
        
        captured = capsys.readouterr()
        assert "No tasks to print" in captured.out

    def test_print_todo_empty_list(self, empty_task_list, capsys):
        print_tasks_todo(empty_task_list)
        
        captured = capsys.readouterr()
        assert "No tasks to print" in captured.out


class TestMain:
    def test_no_arguments(self, capsys):
        with patch('sys.argv', ['task_cli.py']):
            main()
        
        captured = capsys.readouterr()
        assert "Try again" in captured.out

    def test_add_command(self, cleanup_json, capsys):
        with patch('sys.argv', ['task_cli.py', 'add', 'Test task']):
            main()
        
        captured = capsys.readouterr()
        assert "Task added successfully" in captured.out

    def test_list_command(self, cleanup_json, capsys):
        with patch('sys.argv', ['task_cli.py', 'add', 'Test task']):
            main()
        with patch('sys.argv', ['task_cli.py', 'list']):
            main()
        
        captured = capsys.readouterr()
        assert "Test task" in captured.out

    def test_list_done_command(self, cleanup_json, capsys):
        with patch('sys.argv', ['task_cli.py', 'add', 'Test task']):
            main()
        with patch('sys.argv', ['task_cli.py', 'list', 'done']):
            main()
        
        captured = capsys.readouterr()
        # Task was just added, so it's "todo" not "done"
        assert "Test task" not in captured.out or "done" in captured.out

    def test_list_todo_command(self, cleanup_json, capsys):
        with patch('sys.argv', ['task_cli.py', 'add', 'Test task']):
            main()
        with patch('sys.argv', ['task_cli.py', 'list', 'todo']):
            main()
        
        captured = capsys.readouterr()
        assert "Test task" in captured.out

    def test_list_in_progress_command(self, cleanup_json, capsys):
        with patch('sys.argv', ['task_cli.py', 'add', 'Test task']):
            main()
        with patch('sys.argv', ['task_cli.py', 'list', 'in-progress']):
            main()
        
        # New task is "todo", not "in-progress"
        captured = capsys.readouterr()
        assert "Test task" not in captured.out

    def test_invalid_list_subcommand(self, cleanup_json, capsys):
        with patch('sys.argv', ['task_cli.py', 'list', 'invalid']):
            main()
        
        captured = capsys.readouterr()
        assert "Invalid command" in captured.out

    def test_invalid_command(self, capsys):
        with patch('sys.argv', ['task_cli.py', 'invalid']):
            main()
        
        captured = capsys.readouterr()
        assert "This is not a valid command" in captured.out

    def test_update_command(self, cleanup_json, capsys):
        with patch('sys.argv', ['task_cli.py', 'add', 'Original task']):
            main()
        with patch('sys.argv', ['task_cli.py', 'update', '1', 'Updated task']):
            main()
        
        captured = capsys.readouterr()
        assert "updated successfully" in captured.out

    def test_delete_command(self, cleanup_json, capsys):
        with patch('sys.argv', ['task_cli.py', 'add', 'Task to delete']):
            main()
        with patch('sys.argv', ['task_cli.py', 'delete', '1']):
            main()
        
        captured = capsys.readouterr()
        assert "deleted successfully" in captured.out

    def test_mark_in_progress_command(self, cleanup_json, capsys):
        with patch('sys.argv', ['task_cli.py', 'add', 'Task']):
            main()
        with patch('sys.argv', ['task_cli.py', 'mark-in-progress', '1']):
            main()
        
        captured = capsys.readouterr()
        assert "marked as in progress" in captured.out

    def test_mark_done_command(self, cleanup_json, capsys):
        with patch('sys.argv', ['task_cli.py', 'add', 'Task']):
            main()
        with patch('sys.argv', ['task_cli.py', 'mark-done', '1']):
            main()
        
        captured = capsys.readouterr()
        assert "marked as done" in captured.out

    def test_clear_command(self, cleanup_json):
        with patch('sys.argv', ['task_cli.py', 'add', 'Task']):
            main()
        with patch('sys.argv', ['task_cli.py', 'clear']):
            main()
        
        with open(file_path, 'r') as f:
            data = json.load(f)
        assert len(data) == 0

    def test_case_insensitive_commands(self, cleanup_json, capsys):
        with patch('sys.argv', ['task_cli.py', 'ADD', 'Test task']):
            main()
        
        captured = capsys.readouterr()
        assert "Task added successfully" in captured.out