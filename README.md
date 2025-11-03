# IPUP – Introduction to Programming Using Python

This repository contains example Python scripts used in **Module 1**, **Module 2**, **Module 3**, and **Module 4a** for the course *Introduction to Programming Using Python*.  
Each file demonstrates a specific concept in Python syntax, output formatting, user input, data handling, control structures, and functions.

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
| bitwise_and_example.py | Another bitwise AND example with different values |
| bitwise_and_zero_result.py | Shows bitwise AND resulting in zero |
| bitwise_and_nonzero_result.py | Shows bitwise AND resulting in a nonzero value |
| bitwise_and_five_result.py | Example: bitwise AND of 7 and 13 equals 5 |
| bitwise_xor_operator_example.py | Demonstrates the bitwise XOR (`^`) operator |
| bitwise_flag_check_example.py | Uses bitwise AND to check a bit in a flag |
| bitwise_or_set_bit_example.py | Uses bitwise OR (`|`) to set a specific bit |
| bitwise_xor_toggle_bit_example.py | Uses bitwise XOR to toggle a specific bit |
| bitwise_not_invert_example.py | Demonstrates bitwise NOT (`~`) inversion |
| bitwise_not_full_inversion.py | Inverts an 8-bit binary value |
| bitwise_left_shift_example.py | Left shift by 2 positions |
| bitwise_left_shift_three_example.py | Left shift by 3 positions |
| bitwise_left_shift_one_example.py | Left shift by 1 position |
| list_element_update_example.py | Updates a list element by index |
| list_negative_index_update.py | Updates an element using negative indexing |
| list_length_example.py | Uses `len()` to determine list length |
| list_element_deletion_example.py | Removes a list element using `del` |
| list_append_example.py | Adds an element to the end using `append()` |
| list_insert_example.py | Inserts an element at a specific position |
| list_square_elements_example.py | Squares each element in a list |
| list_reverse_in_place_example.py | Reverses a list manually by swapping elements |
| list_reverse_method_example.py | Uses `reverse()` to reverse a list |
| floor_division_simple_example.py | Demonstrates floor division using `//` |
| bubble_sort_optimized_example.py | Optimized bubble sort with a swap flag |
| bubble_sort_basic_example.py | Basic bubble sort implementation |
| sorted_function_example.py | Uses built-in `sorted()` to sort a list |
| list_slicing_example.py | Demonstrates list slicing `[start:end]` |
| list_slicing_start_example.py | Slicing from the start `[:end]` |
| list_slicing_end_example.py | Slicing from an index to the end `[start:]` |
| list_slicing_step_example.py | Slicing with a step `[::step]` |
| list_negative_slicing_example.py | Slicing using negative indices `[-3:-1]` |
| list_reverse_slicing_example.py | Reverse slicing using negative step |
| list_slicing_range_step_example.py | Slicing with start, end, and step `[1:5:2]` |
| list_copy_slicing_example.py | Copies a list using slicing `[:]` |
| list_full_reverse_slicing_example.py | Reverses a list using `[::-1]` |
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

## Module 4a – Functions and Variable Scope

This module introduces **functions**, **parameters**, **return values**, and **variable scope** in Python.  
Students learn how to define functions, use arguments (positional, keyword, and default), return single or multiple values, and understand the difference between local and global variables.

### Topics Covered

| File | Description |
|------|-------------|
| function_addition_example.py | Defines a function that adds two numbers and returns the result |
| function_parameters_example.py | Demonstrates passing multiple parameters to a function |
| function_keyword_arguments_example.py | Uses keyword arguments to call a function with parameters in any order |
| function_default_parameter_example.py | Defines a function with a default parameter value |
| function_return_early_example.py | Shows how a function can return early when a condition is met |
| function_multiple_return_values.py | Demonstrates returning multiple values from a function and unpacking them |
| local_variable_scope_example.py | Illustrates local variable scope — variables inside a function are not accessible outside |
| global_variable_access_example.py | Demonstrates accessing a global variable from within a function |
| global_variable_modification_example.py | Shows how to modify a global variable using the `global` keyword |
| global_variable_reference_example.py | Demonstrates referencing a global variable inside a function |
| global_variable_increment_example.py | Uses a global variable and increments it from within a function |
| recursive_factorial_example.py | Demonstrates recursion by calculating the factorial of a number |

### Learning Outcomes

- Define and call functions using parameters and return values.  
- Understand **positional**, **keyword**, and **default** arguments.  
- Return one or multiple values from a function.  
- Differentiate between **local** and **global** variable scopes.  
- Modify global variables safely using the `global` keyword.  
- Apply recursion to solve repetitive problems (e.g., factorial).  

---

## How to Run the Examples

Use Python 3 to execute any file from the terminal or IDE:

```bash
python filename.py
