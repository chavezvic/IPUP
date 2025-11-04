# IPUP – Introduction to Programming Using Python

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

> **Last Updated:** November 2025  
> **Course:** Introduction to Programming Using Python (IPUP)  
> **Author:** Victor Chavez  

---

## Table of Contents

1. [Overview](#overview)
2. [Course Context (from Instructor Slide Deck)](#course-context-from-instructor-slide-deck)
3. [Module 1 – Python Basics](#module-1--python-basics)
4. [Module 2 – Variables, Input, and Operators](#module-2--variables-input-and-operators)
5. [Module 3 – Comparisons, Loops & Bitwise Operators](#module-3--comparisons-loops--bitwise-operators)
6. [Applied Exercises and Mini-Projects](#applied-exercises-and-mini-projects)
7. [Module 4a – Functions and Variable Scope](#module-4a--functions-and-variable-scope)
8. [Module 4b – Lists, Tuples & Dictionaries](#module-4b--lists-tuples--dictionaries)
9. [How to Run the Examples](#how-to-run-the-examples)
10. [License](#license)

---

## Overview

This repository contains example Python scripts organized by module for the course *Introduction to Programming Using Python*.  
Each module builds upon the previous one — introducing new syntax, logic, and programming concepts.  
All examples are **practical**, **well-commented**, and **tested using Python 3**.

---

## Course Context (from Instructor Slide Deck)

The *Introduction to Programming Using Python (IPUP)* course introduces students to the fundamentals of computer programming through step-by-step examples and real-world applications.  
The content progresses from basic syntax to structured problem solving, emphasizing clarity, logic, and reusable code.

### Key Learning Themes
- **Module 1 – Logic and Syntax**  
  Understand how computers interpret instructions, how Python executes statements line by line, and how pseudocode helps design program logic.  
- **Module 2 – Data and Variables**  
  Explore data types, arithmetic operations, and variable storage concepts. Learn to handle user input and perform calculations using expressions.  
- **Module 3 – Decision Making and Control Flow**  
  Apply Boolean logic, conditionals, and loops to guide program behavior. Introduce bitwise operations for working with binary data and hardware-level logic.  
- **Module 4 – Structure and Modularity**  
  Develop reusable code using functions, manage variable scope, and work with Python’s main data structures (lists, tuples, and dictionaries) to organize and process information efficiently.

### Instructor Note
Each module includes practical exercises inspired by IT and networking scenarios — for example, subnet calculators, network device inventories, and restaurant billing simulations — connecting programming principles to real system-administration tasks.

---

## Module 1 – Python Basics

Fundamentals of Python syntax, printing, escape sequences, and simple arithmetic operations.  

| File | Description |
|------|-------------|
| [hello_world.py](Module1/hello_world.py) | Prints “Hello, World!” |
| [The Zen of Python.py](Module1/The%20Zen%20of%20Python.py) | Displays *The Zen of Python* using `import this` |
| [backslash_escape_example.py](Module1/backslash_escape_example.py) | Demonstrates escape characters and backslashes |
| [print_sep_end_combination.py](Module1/print_sep_end_combination.py) | Demonstrates `sep` and `end` parameters |
| [print_patterns_stars.py](Module1/print_patterns_stars.py) | Prints multi-line ASCII art patterns |
| [string_concatenation_type_error.py](Module1/string_concatenation_type_error.py) | Shows a type error when concatenating strings and integers |

### Learning Outcomes
- Use `print()` for formatted output.  
- Understand escape sequences and line endings.  
- Combine arithmetic and text output.  
- Recognize and debug basic syntax issues.

---

## Module 2 – Variables, Input, and Operators

Covers user input, variables, data types, and basic arithmetic.

| File | Description |
|------|-------------|
| [input_response_example.py](Module2/input_response_example.py) | Prompts for user input and prints a response |
| [input_integer_conversion.py](Module2/input_integer_conversion.py) | Converts input to integers using `int()` |
| [string_concatenation_example.py](Module2/string_concatenation_example.py) | Combines strings using `+` |
| [string_multiplication_example.py](Module2/string_multiplication_example.py) | Repeats strings using `*` |

### Learning Outcomes
- Capture and convert user input.  
- Use arithmetic operators and type conversion.  
- Perform string concatenation and repetition.

---

## Module 3 – Comparisons, Loops & Bitwise Operators

Introduces logic, conditions, iteration, and bitwise operations.

| File | Description |
|------|-------------|
| [if_elif_else_example.py](Module3/if_elif_else_example.py) | Conditional branching using `if`, `elif`, and `else` |
| [while_loop_increment_example.py](Module3/while_loop_increment_example.py) | Demonstrates counting with a `while` loop |
| [for_loop_range_example.py](Module3/for_loop_range_example.py) | Iterates using `range(start, stop, step)` |
| [for_else_loop_example.py](Module3/for_else_loop_example.py) | Shows use of `else` after loop completion |
| [bitwise_xor_operator_example.py](Module3/bitwise_xor_operator_example.py) | Demonstrates XOR bitwise logic |
| [list_reverse_method_example.py](Module3/list_reverse_method_example.py) | Reverses a list using `.reverse()` |
| [sorted_function_example.py](Module3/sorted_function_example.py) | Sorts a list using `sorted()` |

### Learning Outcomes
- Apply logical operators and conditionals.  
- Write and control loops (`for`, `while`).  
- Use bitwise operations for binary logic.  
- Manage list manipulation and iteration.

---

## Applied Exercises and Mini-Projects

Real-world style programming tasks combining logic, control flow, and data handling.

| File | Description |
|------|-------------|
| [cidr_range_calculator.py](Exercises/cidr_range_calculator.py) | Calculates IP address ranges for `/8`, `/16`, `/24` subnets |
| [network_device_inventory.py](Exercises/network_device_inventory.py) | Dictionary-based device inventory system |
| [restaurant_billing_system.py](Exercises/restaurant_billing_system.py) | Calculates bills, applies tax and discounts |

### Learning Outcomes
- Integrate loops, conditionals, and functions.  
- Work with structured user input.  
- Validate data and format readable output.  
- Build small functional applications.

---

## Module 4a – Functions and Variable Scope

Explores function creation, parameters, and variable scope.

| File | Description |
|------|-------------|
| [function_addition_example.py](Module4a/function_addition_example.py) | Adds two numbers using a custom function |
| [function_default_parameter_example.py](Module4a/function_default_parameter_example.py) | Demonstrates default parameter usage |
| [global_variable_modification_example.py](Module4a/global_variable_modification_example.py) | Updates a global variable using `global` |
| [recursive_factorial_example.py](Module4a/recursive_factorial_example.py) | Recursive factorial example |

### Learning Outcomes
- Create and reuse functions.  
- Differentiate between local and global variables.  
- Use recursion for repeated calculations.  
- Apply function parameters and return values effectively.

---

## Module 4b – Lists, Tuples & Dictionaries

Learn Python’s core data structures for ordered and associative data.

| File | Description |
|------|-------------|
| [list_append_insert_example.py](Module4b/list_append_insert_example.py) | Adds and inserts list elements |
| [tuple_indexing_example.py](Module4b/tuple_indexing_example.py) | Access tuple elements with indexing |
| [tuple_iteration_example.py](Module4b/tuple_iteration_example.py) | Iterates over tuple items |
| [dictionary_basic_operations.py](Module4b/dictionary_basic_operations.py) | Adds and retrieves dictionary items |
| [dictionary_items_method_example.py](Module4b/dictionary_items_method_example.py) | Uses `.keys()`, `.values()`, `.items()` |
| [debugging_add_function_example.py](Module4b/debugging_add_function_example.py) | Demonstrates debugging with print tracing |

### Learning Outcomes
- Perform multiple assignments and unpacking.  
- Create and modify lists and tuples.  
- Manage key–value pairs with dictionaries.  
- Iterate efficiently over collections.  
- Debug using strategic print statements.

---

## How to Run the Examples

To run any example:

```bash
python filename.py
