Feature: Manage the to-do list

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user lists all tasks
    Then the output should contain:
      | Task          |
      | Buy groceries |
      | Pay bills     |

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task          | Status  |
      | Buy groceries | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Delete a task from the to-do list
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user deletes the task "Buy groceries"
    Then the to-do list should not contain "Buy groceries"
    And the to-do list should contain "Pay bills"

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user clears the to-do list
    Then the to-do list should be empty
