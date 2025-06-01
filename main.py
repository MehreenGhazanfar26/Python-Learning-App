import streamlit as st
import io
import contextlib
import random

st.set_page_config(page_title="Python Beginner App7", layout="wide")

if "completed_modules" not in st.session_state:
    st.session_state.completed_modules = []

modules = ["Introduction", "Variables", "Data Types", "Conditions", "Loops"]

st.sidebar.title("Python Beginner App")
pages = ["Home Dashboard"] + modules
page_choice = st.sidebar.radio("Go to:", pages)

def run_user_code(code):
    output_buffer = io.StringIO()
    try:
        with contextlib.redirect_stdout(output_buffer):
            exec(code, {})
        return output_buffer.getvalue(), None
    except Exception as e:
        return None, str(e)

def show_module(title, explanation, example_codes, mcqs, practice_prompts):
    st.title(f"Module: {title}")
    st.markdown("### 📘 Explanation")
    st.markdown(explanation)

    if example_codes:
        st.markdown("### 🔍 Example Tasks with Results")
        for i, code in enumerate(example_codes):
            st.markdown(f"**Example {i + 1}**")
            st.code(code, language='python')
            if st.button(f"Run Example {i + 1}", key=f"{title}_ex_run_{i}"):
                output, error = run_user_code(code)
                if output:
                    st.success("Output:")
                    st.code(output)
                elif error:
                    st.error("Error:")
                    st.code(error)
    else:
        st.warning("No examples available.")

    if practice_prompts:
        st.markdown("### 🧠 Practice Tasks")
        for i, task in enumerate(practice_prompts):
            st.markdown(f"**Task {i + 1}:** {task}")
            user_code = st.text_area("Write your code:", height=150, key=f"{title}_practice_{i}")
            if st.button("Check", key=f"{title}_check_{i}"):
                output, error = run_user_code(user_code)
                if output:
                    st.success("Output:")
                    st.code(output)
                elif error:
                    st.error("Mistake:")
                    st.code(error)
    else:
        st.warning("No practice tasks available.")

    st.markdown("### ❓ Quick Quiz")
    if mcqs:
        quiz_key = f"{title}_quiz_submitted"
        if quiz_key not in st.session_state:
            st.session_state[quiz_key] = False
            st.session_state[f"{title}_random_mcqs"] = random.sample(mcqs, min(3, len(mcqs)))

        random_mcqs = st.session_state[f"{title}_random_mcqs"]

        for idx, (question, options, correct) in enumerate(random_mcqs):
            st.radio(f"{idx + 1}. {question}", options, key=f"{title}_q_{idx}")

        if not st.session_state[quiz_key]:
            if st.button("Submit Quiz", key=f"{title}_submit"):
                st.session_state[quiz_key] = True

        if st.session_state[quiz_key]:
            st.markdown("### 🧾 Results")
            for idx, (question, options, correct) in enumerate(random_mcqs):
                user_answer = st.session_state.get(f"{title}_q_{idx}")
                if user_answer == correct:
                    st.success(f"{idx + 1}. ✅ {question} — Correct!")
                else:
                    st.error(f"{idx + 1}. ❌ {question} — Wrong! (Correct: {correct})")


    if st.button("Mark This Module as Completed", key=title + "_complete"):
        if title not in st.session_state.completed_modules:
            st.session_state.completed_modules.append(title)
            st.success(f"Marked '{title}' as completed!")

# ----------------- MODULE DATA -----------------

module_data = {
    "Introduction": {
        "explanation": """
Python is a **high-level, interpreted programming language** created by Guido van Rossum in 1991. It is known for its clean syntax and readability, making it ideal for beginners and professionals alike. Python supports multiple programming paradigms including procedural, object-oriented, and functional programming. It uses the `.py` file extension and comes with an official environment called **IDLE** (Integrated Development and Learning Environment). Python is a dynamically typed language, meaning you don’t need to declare data types explicitly. You can use the `print()` function to display output and `#` for writing comments. Its simplicity and versatility have made Python one of the most popular programming languages in the world.
""",
        "examples": [
            'print("Hello, Python Learners!")',
            'print("Name: Ahmed")',
            '# This program displays the school name\nprint("ABC Public School")',
            'print("Name: Ali")\nprint("Age: 17")\nprint("Class: 10th")',
            '# Display city and country\nprint("City: Karachi")\nprint("Country: Pakistan")'
        ],
        "mcqs": [
            ("What is Python?", ["Game", "Language", "Toy", "Website"], "Language"),
            ("Who uses Python?", ["Chefs", "Programmers", "Drivers", "Artists"], "Programmers"),
            ("Which extension do Python files have?", [".txt", ".exe", ".py", ".html"], ".py")
        ],
        "practices": [
            'Write a program to print "Welcome to Coding!"',
            "Display your favorite fruit using print().",
            "Write a comment and print your college name.",
            "Print three lines: Your hobby, your age, and your grade.",
            "Use two print() statements and three comments."
        ]
    },
    "Variables": {
        "explanation": """
In Python, **variables** are used to store data. You can assign a value to a variable using the equals sign (`=`). Variable names should be meaningful and follow naming rules (start with a letter or underscore, cannot begin with a digit, and cannot be a reserved keyword). Python is dynamically typed, so the type of variable is determined at runtime.
""",
        "examples": [
            '# Assign and print a student\'s name\nstudent_name = "Zara"\nprint("Student Name:", student_name)',
            '# Create and print two variables\ncity = "Lahore"\ncountry = "Pakistan"\nprint(city, country)',
            '# Adding subject scores\nmath = 90\nscience = 85\ntotal = math + science\nprint("Total Marks:", total)',
            '# Reassigning variables\nx = 7\nprint("Before:", x)\nx = 12\nprint("After:", x)',
            '# Declare three variables and print their product\na = 2\nb = 3\nc = 4\nprint("Product:", a * b * c)'
        ],
        "mcqs":   [
            ("Which keyword is used to assign a value?", ["let", "set", "=", "assign"], "="),
            ("What is a variable?", ["A box", "A loop", "A name for a value", "A Python command"], "A name for a value"),
            ("Can a variable name start with a number?", ["Yes", "No"], "No")
        ],
        "practices": [
            "Make a variable my_name and print it.",
            "Assign and print district and province.",
            "Create variables english_score and urdu_score, print the sum.",
            "Set y = 15, then change it to y = 20, and print both.",
            "Create variables p, q, r and print their total."
        ]
    },
    "Data Types": {
        "explanation": """
Python has several **built-in data types** such as:

- `str` – for text (e.g. "hello")
- `int` – for integers (e.g. 5)
- `float` – for decimals (e.g. 3.14)
- `bool` – for True or False
- `list` – for an ordered group of items
- `tuple` – like a list but cannot be changed
- `dict` – for key-value pairs

Use `type()` to check a variable's data type.
""",
        "examples": [
            '# Different types\nname = "Hina"\nage = 22\nis_graduate = True',
            '# List of fruits\nfruits = ["apple", "banana", "grape"]\nprint(fruits)',
            '# Tuple of weekdays\nweekdays = ("Mon", "Tue", "Wed")\nprint(weekdays)',
            '# Float example and checking type\ntemperature = 36.5\nprint(type(temperature))',
            '# Dictionary example\nstudent = {"name": "Ali", "grade": "A"}\nprint(student)'
        ],
        "mcqs": [
            ("What type is 10?", ["int", "float", "str", "bool"], "int"),
            ("What type is 3.14?", ["int", "float", "str", "bool"], "float"),
            ("What type is 'Hi'?", ["int", "float", "str", "bool"], "str")
        ],
        "practices": [
            "Create variables with values: a country (string), population (integer), is_large (Boolean).",
            "Make a list of 3 vegetables and print it.",
            "Define a tuple with 3 seasons and display it.",
            "Declare a float variable for weight and check its type.",
            'Create a dictionary for a book with keys "title" and "author".'
        ]
    },
    "Conditions": {
        "explanation": """
Conditions in Python are used to make decisions in your program. The most common conditional statements are:

- `if` – checks a condition and runs code if it's True
- `else` – runs code if the condition is False
- `elif` – lets you check multiple conditions

You can also use logical operators like `and`, `or`, and `not`.
""",
        "examples": [
            '# Check if user is adult\nage = 20\nif age >= 18:\n    print("Adult")',
            '# Simple pass/fail condition\nmarks = 45\nif marks >= 40:\n    print("Passed")\nelse:\n    print("Failed")',
            '# Check even or odd\nnum = 6\nif num % 2 == 0:\n    print("Even")\nelse:\n    print("Odd")',
            '# Grade system\nscore = 82\nif score >= 90:\n    print("Grade A")\nelif score >= 70:\n    print("Grade B")\nelse:\n    print("Grade C")',
            '# Teenager check\nage = 16\nif age >= 13 and age <= 19:\n    print("Teenager")\nelse:\n    print("Not a Teenager")'
        ],
        "mcqs": [
            ("Which keyword starts a condition?", ["if", "for", "def", "while"], "if"),
            ("What does '==' mean?", ["assign", "equals", "not equal", "less than"], "equals"),
            ("Which block runs if condition is false?", ["if", "else", "elif", "while"], "else")
        ],
        "practices": [
            "Write a program to check if a number is negative.",
            "Use if-else to decide if a student got distinction (marks ≥ 80).",
            "Check if a number is divisible by 3.",
            'Use if-elif-else to print result: "Excellent", "Good", "Needs Improvement".',
            "Ask user for their age and print if they are a senior citizen (age ≥ 60)."
        ]
    },
    "Loops": {
        "explanation": """
Loops help you repeat code multiple times. Python has two main types:

- `for` loop – used for iterating over a sequence (like a list or string)
- `while` loop – runs as long as a condition is True

Use `range()` to create number sequences in a `for` loop.
""",
        "examples": [
            '# Print numbers using for loop\nfor i in range(1, 6):\n    print(i)',
            '# Loop through a string\nword = "Code"\nfor char in word:\n    print(char)',
            '# Countdown with while loop\nn = 3\nwhile n > 0:\n    print(n)\n    n -= 1',
            '# Print even numbers\nfor i in range(2, 11, 2):\n    print(i)',
            '# Ask name 3 times\nfor i in range(3):\n    name = input("Enter your name: ")\n    print("Hello", name)'
        ],
        "mcqs": [
            ("Which loop is used to repeat code?", ["if", "loop", "for", "def"], "for"),
            ("What does range(3) do?", ["1 to 3", "0 to 2", "0 to 3", "1 to 2"], "0 to 2"),
            ("Which keyword stops a loop?", ["exit", "quit", "break", "stop"], "break")
        ],
        "practices": [
            "Use a for loop to print numbers from 5 to 10.",
            'Print each letter in the word "Python".',
            "Use a while loop to print numbers from 1 to 4.",
            "Print all odd numbers between 1 and 10 using loop.",
            'Ask the user 2 times: “What is your favorite subject?”'
        ]
    }
}

# ----------------- PAGE ROUTING -----------------

if page_choice == "Home Dashboard":
    st.title("Welcome to Python Beginner Dashboard")
    completed = len(st.session_state.completed_modules)
    total = len(modules)
    percent = int((completed / total) * 100)
    st.metric("Modules Completed", f"{completed} / {total}")
    st.progress(percent / 100)
    st.markdown("### Your Progress")
    for mod in modules:
        if mod in st.session_state.completed_modules:
            st.success(f"{mod} ✅ Completed")
        else:
            st.warning(f"{mod} ❌ Not Done")
    st.info("Select a module from the sidebar to start learning!")

elif page_choice in modules:
    data = module_data.get(page_choice, {})
    show_module(
        title=page_choice,
        explanation=data.get("explanation", ""),
        example_codes=data.get("examples", []),
        mcqs=data.get("mcqs", []),
        practice_prompts=data.get("practices", [])
    )
