import pytest
from task_tracker import add_task

print(pytest.__version__)
test_task_list = []

def test_add_to_list():
    add_task(test_task_list, 'Item 1')
    assert len(test_task_list) == 1 and test_task_list[0] == 'Item 1'