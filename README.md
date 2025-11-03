# IPUP – Introduction to Programming Using Python

This repository contains example Python scripts used in **Module 1**, **Module 2**, **Module 3**, **Module 4a**, and **Module 4b** for the course *Introduction to Programming Using Python*.  
Each file demonstrates a specific concept in Python syntax, output formatting, user input, data handling, control structures, functions, data structures, and debugging.

---

## Module 1 – Python Basics

This module covers printing, escape sequences, string formatting, and arithmetic operations.

### Topics Covered

| File | Description |
|------|-------------|
| hello_world.py | First Python program printing “Hello, World!” |
| The Zen of Python.py | Displays *The Zen of Python* using `import this` |
| backslash_escape_example.py | Demonstrates printing backslashes and escape sequences |
| division_and_type_conversion.py | Shows division and string conversion with `str()` |
| floor_division_example.py | Demonstrates floor division using `//` |
| multiple_print_statements.py | Prints output across multiple lines using separate `print()` calls |
| print_end_parameter_example.py | Controls line endings with the `end` parameter |
| print_multiple_arguments_example.py | Prints multiple items separated by spaces |
| print_newline_and_end.py | Combines newline characters (`\n`) with custom endings |
| print_patterns_stars.py | Creates star (`*`) patterns using multiple `print()` statements |
| print_quotes_and_escapes.py | Shows how to include quotes inside strings using escapes |
| print_quotes_inside_string.py | Demonstrates quoting text within string literals |
| print_quotes_variations.py | Prints strings using single and double quotes |
| print_sep_and_end_parameters.py | Demonstrates using both `sep` and `end` in `print()` |
| print_sep_end_combination.py | Advanced usage of `sep` and `end` parameters |
| print_sep_order_error.py | Demonstrates incorrect keyword argument order with `sep` |
| print_sep_parameter.py | Changes separators between arguments using `sep` |
| print_statements_example.py | Example using multiple print statements with formatting |
| string_concatenation_type_error.py | Demonstrates a type error caused by mixing strings and integers |

---

## Module 2 – Variables, Input, and Operators

This module introduces **variables**, **user input**, **type conversion**, and **string operations**.

### Topics Covered

| File | Description |
|------|-------------|
| input_response_example.py | Prompts for input and prints a dynamic response |
| input_integer_conversion.py | Converts user input from string to integer |
| string_concatenation_example.py | Combines multiple strings using `+` |
| string_multiplication_example.py | Repeats a string using the `*` operator |

### Learning Outcomes

- Capture and display user input.  
- Convert between string and numeric data types.  
- Concatenate and multiply strings.  
- Understand how variables and operators work together.  

---

## Module 3 – Comparisons, Loops & Bitwise Operators

This module covers comparison operators, boolean evaluation, conditional statements, loops, and basic bitwise operations.

### Topics Covered

| File | Description |
|------|-------------|
| comparison_operators_example.py | Demonstrates equality (`==`) comparisons for user input |
| not_equal_operator_example.py | Demonstrates the not-equal (`!=`) operator |
| greater_than_comparison.py | Uses the greater-than (`>`) operator with constants |
| less_than_comparison.py | Uses the less-than (`<`) operator with constants |
| if_elif_else_example.py | Shows decision-making using `if`, `elif`, and `else` |
| while_loop_increment_example.py | Uses a `while` loop and increments a counter |
| while_else_loop_example.py | Demonstrates a `while` loop with an `else` clause |
| for_loop_range_example.py | Demonstrates a `for` loop with `range(start, stop, step)` |
| while_loop_break_example.py | Shows how to exit a `while` loop early using `break` |
| for_loop_continue_example.py | Skips an iteration using `continue` |
| for_else_loop_example.py | Demonstrates a `for` loop with an `else` clause |
| bitwise_and_operator_example.py | Demonstrates the bitwise AND (`&`) operator |
| bitwise_xor_operator_example.py | Demonstrates the bitwise XOR (`^`) operator |
| bitwise_or_set_bit_example.py | Uses bitwise OR (`|`) to set a specific bit |
| bitwise_not_invert_example.py | Demonstrates bitwise NOT (`~`) inversion |
| bitwise_left_shift_example.py | Demonstrates bitwise left shift (`<<`) |
| list_append_example.py | Adds an element to the end using `append()` |
| list_insert_example.py | Inserts an element at a specific position |
| list_reverse_method_example.py | Uses the built-in `reverse()` method |
| sorted_function_example.py | Uses `sorted()` to sort a list |
| string_slicing_examples.py | Demonstrates string slicing and reversal |

### Learning Outcomes

- Compare values using relational and equality operators.  
- Control program flow with `if`, `elif`, and `else`.  
- Use loops with `break`, `continue`, and `else` blocks.  
- Apply bitwise operations (`&`, `|`, `^`, `~`, `<<`).  
- Work with lists: update, append, insert, reverse, delete, slice.  
- Sort lists manually or with built-in functions.  
- Perform slicing and reversal on lists and strings.

---

## Applied Exercises and Mini-Projects

This section provides **hands-on programming challenges** that combine logic, input/output, and data structures.

| File | Description |
|------|-------------|
| cidr_range_calculator.py | Calculates network IP address ranges for `/8`, `/16`, and `/24` subnets. |
| network_device_inventory.py | Interactive inventory system using dictionaries to store and retrieve network device details. |
| restaurant_billing_system.py | Simulates a restaurant billing app with menu pricing, subtotal, tax, and conditional discounts. |

### Learning Outcomes

- Combine user input, loops, and conditionals in real-world tasks.  
- Manage structured data using lists and dictionaries.  
- Validate user input for robustness.  
- Apply arithmetic and control logic in program design.

---

## Module 4a – Functions and Variable Scope

This module introduces **functions**, **parameters**, **return values**, and **variable scope** in Python.  
Students learn how to define functions, use arguments (positional, keyword, and default), return single or multiple values, and understand local vs. global variables.

### Topics Covered

| File | Description |
|------|-------------|
| function_addition_example.py | Defines a function that adds two numbers and returns the result |
| function_parameters_example.py | Demonstrates passing multiple parameters to a function |
| function_keyword_arguments_example.py | Uses keyword arguments to call a function in any order |
| function_default_parameter_example.py | Demonstrates default parameter values |
| function_return_early_example.py | Shows how a function can return early |
| function_multiple_return_values.py | Returns multiple values and unpacks them |
| local_variable_scope_example.py | Demonstrates local variable scope |
| global_variable_access_example.py | Accesses a global variable inside a function |
| global_variable_modification_example.py | Modifies a global variable using `global` |
| recursive_factorial_example.py | Calculates a factorial using recursion |

### Learning Outcomes

- Define and call functions using parameters and return values.  
- Understand positional, keyword, and default arguments.  
- Return one or multiple values.  
- Differentiate between local and global scope.  
- Safely modify global variables using `global`.  
- Implement recursive functions.

---

## Module 4b – Lists, Tuples & Dictionaries

This module introduces Python’s **data structures** for ordered and associative collections: **lists**, **tuples**, and **dictionaries**.  
Students learn how to create, modify, access, iterate through, and manage these collections — building foundational skills for structured programming.

### Topics Covered

| File | Description |
|------|-------------|
| multiple_assignment_example.py | Demonstrates multiple variable assignment in a single line. |
| list_append_insert_example.py | Adds and inserts elements into a list. |
| tuple_indexing_example.py | Demonstrates accessing tuple elements using positive and negative indices. |
| tuple_immutable_error_example.py | Attempts to modify a tuple element, raising a `TypeError`. |
| dictionary_basic_operations.py | Demonstrates creating and updating dictionary entries. |
| dictionary_update_delete_example.py | Adds, modifies, and deletes key–value pairs. |
| dictionary_keys_values_items_example.py | Shows how to access `.keys()`, `.values()`, and `.items()`. |
| dictionary_iteration_example.py | Iterates over a dictionary to display all keys and values. |
| debugging_add_function_example.py | Demonstrates debugging using print statements to trace variable flow. |

### Learning Outcomes

- Perform **multiple variable assignments** using tuple unpacking.  
- Create and manipulate **lists** using methods like `append()` and `insert()`.  
- Understand **tuple immutability** and indexing.  
- Use **dictionaries** for key–value data management.  
- Iterate over dictionary keys and values efficiently.  
- Apply print-based debugging to trace program execution.

---

## How to Run the Examples

Use Python 3 to execute any file from the terminal or IDE:

```bash
python filename.py
