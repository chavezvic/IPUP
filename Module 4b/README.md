### Concepts from Slides
- Python provides multiple collection data types for grouping values:
  - **Lists** – ordered, mutable collections defined with square brackets `[]`
  - **Tuples** – ordered, immutable collections defined with parentheses `()`
  - **Dictionaries** – unordered, key-value pairs defined with curly braces `{}`
- Lists can store different data types, including other lists, and can be modified with methods like:
  - `.append()`, `.insert()`, `.remove()`, `.pop()`, `.reverse()`, `.sort()`
- Tuples are useful for fixed data that should not change and support unpacking into multiple variables.
- Dictionaries use keys for fast lookups and can be iterated with `.keys()`, `.values()`, and `.items()`.
- Use `for` loops to iterate through collections efficiently.
- Collections help organize and manage data in structured ways for real-world applications.
- Errors when working with collections include:
  - `KeyError` for missing keys
  - `IndexError` for invalid list positions
  - `TypeError` when using incorrect data types
- Exception handling (`try` and `except`) prevents crashes and provides user-friendly error messages.
- Debugging techniques include adding print statements and testing small parts of code at a time.

### Try It Yourself
Create a dictionary representing three network devices (hostname, IP, type).  
Print each key-value pair using a loop.
