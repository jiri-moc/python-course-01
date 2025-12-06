# Python Course 01

This repository contains teaching materials and example scripts

The focus is on:

- basic algorithmic thinking,
- Python syntax and core concepts,
- modularisation and imports,
- small, self-contained console projects students can easily understand and extend.

Recommended IDEs:

- [Visual Studio Code](https://code.visualstudio.com/)
- [PyCharm for Education](https://www.jetbrains.com/help/pycharm/pycharm-educational.html)

You can download the Python interpreter from the [official Python Website](https://www.python.org/)

---

## File Overview

### `course_01_basics.py`

Foundational script demonstrating:

- What an algorithm is
- Translating algorithms into code
- Variables and data types (int, float, str, bool, list, dict)
- Conditions (if / elif / else)
- Loops (for, break, continue)
- Functions (def, parameters, return values)
- Functions as first-class objects (passing a function as an argument)

### `course_02_modules.py`

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

### `example_01_unit_conversion.py`

Covers:

- reading user input
- arithmetic operations
- converting °C ↔ °F and km ↔ miles
- simple branching (if)
- basic error handling (try / except)

### `example_02_guess_the_number.py`

Features:

- random.randint() to generate a secret number
- while True game loop
- input validation
- conditional game responses
- attempt counter

### `example_03_text_analysis.py`

Demonstrates:

- string manipulation (split, strip, lower)
- word counting
- finding the longest word
- detecting palindromes
- list comprehensions
- simple custom functions

### `example_04_grades.py`

Teaches:

- dictionaries (student → list of grades)
- simple CRUD-like operations
- averaging values
- working with lists
- loop-based menu

### `example_05_quiz.py`

Includes:

- reading/writing JSON files
- os.path.exists for file checks
- handling malformed JSON
- list of question objects ({ "q": "...", "a": "..." })
- scoring mechanism
- saving results to score.json

### `example_06_calculator.py`

Implements:

- arithmetic functions
- runtime menu using while
- structured logic
- clean error handling for invalid input or division by zero

### `example_07_password_generator.py`

Uses:

- random and string modules
- secure password generation rules
- mixing letters, digits and symbols
- shuffling and assembling strings

### `example_08_seconds_converter.py`

Demonstrates:

- integer math (//, %)
- formatting into HH:MM:SS strings
- returning multiple values from a function
- basic validation

### `example_09_random_name_generator.py`

Features:

- lists of first and last names
- random.choice()
- looping for user-defined number of names
- simple input fallback

## Additional Recommended Example Scripts

Below is a set of __additional mini-projects__ suitable for beginners.  
They extend the course with practical, fun, and well-structured exercises.

---

### 1. Beginner-Friendly Mini Projects

#### __1) BMI Calculator__

__Skills:__ user input, arithmetic operations, conditions  
__Description:__  
User enters weight and height, program calculates BMI and outputs the category.

---

#### __2) Vowel & Consonant Counter__

__Skills:__ string processing, loops, conditions  
Counts vowels, consonants, and other characters in a given text.

---

#### __3) Strong Password Checker__

__Skills:__ string methods, conditions  
Validates if the password contains uppercase, lowercase, digits, special symbols.

---

#### __4) RGB ↔ HEX Color Converter__

__Skills:__ arithmetic, formatting, basic number systems  
Converts RGB values to HEX and back.

---

#### __5) Simple Stopwatch__

__Skills:__ time module, loops, basic logic  
User starts/stops and program measures elapsed time.

---

### 2. File & Data Handling Projects

#### __6) CSV Reader with Basic Report__

__Skills:__ file I/O, string parsing, lists  
Loads CSV file and prints summary statistics (row count, averages).

---

#### __7) TODO List in JSON__

__Skills:__ JSON, lists, dictionaries, CRUD operations  
Add tasks, mark them as finished, save & load the list.

---

#### __8) Daily Journal Generator__

__Skills:__ file creation, timestamps  
Creates a file named `diary_YYYY-MM-DD.txt` and writes user notes inside.

---

#### __9) INI Configuration Reader__

__Skills:__ configparser, structured configuration  
Reads configuration values from an `.ini` file and prints them.

---

### 3. Logic Games & Algorithmic Exercises

#### __10) Tic-Tac-Toe (Console)__

__Skills:__ 2D lists, loops, win-condition checking  
Two-player console game; advanced option: simple AI.

---

#### __11) Rock–Paper–Scissors__

__Skills:__ random, conditions  
Optional: score counter, best-of-N matches.

---

#### __12) Math Quiz Generator__

__Skills:__ loops, random, user input  
Generates N arithmetic problems and evaluates user results.

---

### 4. Modularisation & Structured Code Examples

#### __13) Geometry Utility Module__

__Skills:__ modularisation, imports, functions  
`geometry.py` with area/perimeter functions; `main.py` demonstrates usage.

---

#### __14) Simple Logging Utility__

__Skills:__ file I/O, timestamps, modular code design  
`logging_utils.py` with functions `log_info()` and `log_error()`.

---

#### __15) Mini "API" Simulation (Without Web)__

__Skills:__ multi-file architecture, separation of concerns  

- `database.py` – stores in-memory items  
- `service.py` – CRUD functions  
- `main.py` – menu interface

Excellent for demonstrating project structure.

---
