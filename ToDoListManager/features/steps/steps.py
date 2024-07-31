from behave import given, when, then
from todo_list import TodoListManager

@given('the to-do list is empty')
def step_given_todo_list_empty(context):
    context.manager = TodoListManager()

@given(u'the to-do list contains tasks')
def step_given_todo_list_contains_tasks(context):
    context.manager = TodoListManager()
    for row in context.table.rows:
        context.manager.add_task(row['Task'])

@when('the user adds a task "{task_name}"')
def step_when_user_adds_task(context, task_name):
    context.manager.add_task(task_name)

@when('the user lists all tasks')
def step_when_user_lists_all_tasks(context):
    context.output = context.manager.list_tasks()

@when('the user marks task "{task_name}" as completed')
def step_when_user_marks_task_completed(context, task_name):
    context.manager.mark_task_completed(task_name)

@when('the user deletes the task "{task_name}"')
def step_when_user_deletes_task(context, task_name):
    context.manager.delete_task(task_name)

@when('the user clears the to-do list')
def step_when_user_clears_todo_list(context):
    context.manager.clear_tasks()

@then('the to-do list should contain "{task_name}"')
def step_then_todo_list_should_contain(context, task_name):
    tasks = context.manager.list_tasks()
    assert f"{task_name.capitalize()} - Pending" in tasks

@then('the to-do list should show task "{task_name}" as completed')
def step_then_todo_list_should_show_task_completed(context, task_name):
    tasks = context.manager.list_tasks()
    assert f"{task_name.capitalize()} - Completed" in tasks

@then('the to-do list should not contain "{task_name}"')
def step_then_todo_list_should_not_contain(context, task_name):
    tasks = context.manager.list_tasks()
    assert f"{task_name.capitalize()} - Pending" not in tasks

@then('the to-do list should be empty')
def step_then_todo_list_should_be_empty(context):
    tasks = context.manager.list_tasks()
    assert len(tasks) == 0

@then(u'the output should contain')
def step_then_output_should_contain(context):
    expected_tasks = [f"{row['Task'].capitalize()} - Pending" for row in context.table.rows]
    actual_tasks = context.output
    assert sorted(expected_tasks) == sorted(actual_tasks)
