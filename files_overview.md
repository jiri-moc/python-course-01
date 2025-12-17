# File Overview

## `course_01_basics.py`

Foundational script demonstrating:

- What an algorithm is
- Translating algorithms into code
- Variables and data types (int, float, str, bool, list, dict)
- Conditions (if / elif / else)
- Loops (for, break, continue)
- Functions (def, parameters, return values)
- Functions as first-class objects (passing a function as an argument)

## `course_02_modules.py`

Script focused on modularisation and imports:

- What a module is
- Why we modularise code
- Using standard modules (math, random)
- Import styles:
  - import module
  - from module import function
  - import module as alias
- Concept of __name__ == "__main__"
- Examples of how a project can be split into multiple .py files

## `example_01_unit_conversion.py`

Covers:

- reading user input
- arithmetic operations
- converting °C ↔ °F and km ↔ miles
- simple branching (if)
- basic error handling (try / except)

## `example_02_guess_the_number.py`

Features:

- random.randint() to generate a secret number
- while True game loop
- input validation
- conditional game responses
- attempt counter

## `example_03_text_analysis.py`

Demonstrates:

- string manipulation (split, strip, lower)
- word counting
- finding the longest word
- detecting palindromes
- list comprehensions
- simple custom functions

## `example_04_grades.py`

Teaches:

- dictionaries (student → list of grades)
- simple CRUD-like operations
- averaging values
- working with lists
- loop-based menu

## `example_05_quiz.py`

Includes:

- reading/writing JSON files
- os.path.exists for file checks
- handling malformed JSON
- list of question objects ({ "q": "...", "a": "..." })
- scoring mechanism
- saving results to score.json

## `example_06_calculator.py`

Implements:

- arithmetic functions
- runtime menu using while
- structured logic
- clean error handling for invalid input or division by zero

## `example_07_password_generator.py`

Uses:

- random and string modules
- secure password generation rules
- mixing letters, digits and symbols
- shuffling and assembling strings

## `example_08_seconds_converter.py`

Demonstrates:

- integer math (//, %)
- formatting into HH:MM:SS strings
- returning multiple values from a function
- basic validation

## `example_09_random_name_generator.py`

Features:

- lists of first and last names
- random.choice()
- looping for user-defined number of names
- simple input fallback
