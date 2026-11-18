# Student Expense Manager😜

A beginner-friendly Python console project for recording student
expenses, viewing saved entries, calculating total spending, and
summarising expenses by category.

This project is designed as a learning exercise. It demonstrates how
basic Python concepts can work together in a small, practical
application.

## Features

-   Add an expense with an amount, category, and description.
-   Store multiple expenses in a list.
-   Display individual expense details.
-   Display all recorded expenses.
-   Calculate the total amount spent.
-   Calculate category-wise spending using a dictionary.

## Requirements

-   Python 3
-   A code editor or terminal

No external Python packages are required.

## How to run

1.  Save your program in a file named `student_expenses.py`.

2.  Open a terminal in the folder containing the file.

3.  Run:

    ``` bash
    python student_expenses.py
    ```

    On some Windows installations, use:

    ``` bash
    py student_expenses.py
    ```

## How the data is stored

Each expense is stored as a three-item list:

``` python
[amount, category, description]
```

For example:

``` python
expenses = [
    [100, "Food", "Lunch"],
    [50, "Travel", "Bus fare"],
    [80, "Food", "Snacks"]
]
```

The outer list contains all expenses. Each inner list represents one
expense.

## Main functions

  -----------------------------------------------------------------------
  Function                            Purpose
  ----------------------------------- -----------------------------------
  `student_expenses()`                Takes input, stores expenses, and
                                      controls the menu loop.

  `total(total_expenses)`             Adds the amount from every expense.

  `category_total(expenses)`          Groups amounts by category using a
                                      dictionary.
  -----------------------------------------------------------------------

### Total calculation

The total function starts at zero and adds each expense amount:

``` python
total_amount = 0

for expense in total_expenses:
    total_amount += expense[0]
```

### Category-wise calculation

The category summary uses the category as a dictionary key. If the
category already exists, the new amount is added to its existing total.
Otherwise, a new key is created.

``` python
if category in category_expenses:
    category_expenses[category] += amount
else:
    category_expenses[category] = amount
```

## Concepts practised

-   Variables and user input
-   Type conversion with `int()`
-   Lists and nested lists
-   Dictionaries
-   `while` and `for` loops
-   `if`, `elif`, and `else`
-   `break` and `continue`
-   Functions and function arguments
-   Accumulator pattern for totals
-   Dictionary-based grouping

## Important programming lessons

1.  **Store data before checking whether to stop.** Add the current
    expense to the list before asking whether the user wants to enter
    another one. This ensures the final entry is not lost when the user
    chooses `no`.
2.  **Understand `break` and `continue`.** `break` exits the loop;
    `continue` skips the rest of the current iteration and starts the
    next one.
3.  **Pass data to functions.** A list created inside
    `student_expenses()` is local to that function. Pass it as an
    argument to `total()` and `category_total()`.
4.  **Check indentation.** Indentation determines whether code runs
    inside a loop or after it.
5.  **Avoid duplicate calculations.** Add an amount only once to a
    category total.

## Suggested improvements

These are optional next steps for anyone extending the project:

-   Validate that the amount is a positive number.
-   Handle invalid numeric input without crashing.
-   Make category searches case-insensitive (for example, `food` and
    `Food`).
-   Add an option to search expenses by category.
-   Add edit and delete options.
-   Save expenses to a CSV or JSON file so they remain available after
    the program closes.
-   Add dates to expenses and show daily or monthly summaries.

## Example test data

Try entering these three expenses:

    Amount Category   Description
  -------- ---------- -------------
       100 Food       Lunch
        50 Travel     Bus fare
        80 Food       Snacks

Expected results:

-   Total expenses: `230`
-   Food: `180`
-   Travel: `50`

## About this project and AI assistance

This project was built as a learning exercise by a beginner Python
programmer. An AI assistant was used for explanations, debugging
guidance, and feedback during development. The goal is to understand the
code rather than simply copy a solution.

If you share or publish this project, keep improving it, test your
changes, and make sure you can explain each function and line of logic
yourself.

## For fellow beginners

You do not need to write every line without help to be a real
programmer. Using documentation, asking questions, learning from
examples, and getting feedback are normal parts of software development.
What matters is that you understand the decisions in your code, test it,
and gradually become more independent.
