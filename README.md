# Python Beginner Projects 🐍

This repository contains beginner-friendly Python projects created to practice and improve core programming concepts.
- **Purpose:** To learn Python through hands-on projects and strengthen programming fundamentals.

## Features
- Beginner-friendly projects
- Covers core Python concepts
- Interactive command-line applications
- Well-structured and easy-to-understand code

## 📑Table of Contents
- [Project 1 - Number Guessing Game](#project-1---number-guessing-game)
- [Project 2 - Student Grade Calculator](#project-2---student-grade-calculator)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [How to Run the Code](#how-to-run-the-code)
- [Author](#author)

## Project 1 - Number Guessing Game

A simple command-line game where the computer randomly selects a number and the user tries to guess it.

## Features
- Random number generation
- User input validation
- Too High / Too Low hints
- Attempt counter
- Play Again functionality
  
## Concepts Used
- Functions
- Loops
- Conditional Statements
- Exception Handling
- Random Module
  
**Example**:
```
Welcome to the Number Guessing Game!🙌
Guess a number between 1 and 100.

Enter your guess: 50
Too high! Try again.

Enter your guess: 20
Too high! Try again.

Enter your guess: 18
Too high! Try again.

Enter your guess: 16
🎉 Congratulations! You guessed the number!.

You took 4 attempts.
Do you want to play again? (Yes/No): yes

Welcome to the Number Guessing Game!🙌
Guess a number between 1 and 100.

Enter your guess: 50
Too low! Try again.

Enter your guess: 79
🎉 Congratulations! You guessed the number!.

You took 2 attempts.
Do you want to play again? (Yes/No): no

Thanks for playing! Goodbye 👋
```
## Project 2 - Student Grade Calculator

A simple Python console application that collects student information, accepts subject marks,
calculates the overall result, and displays the student's grade and pass/fail status.

## Features
- Student information management
- User input validation
- Subject-wise marks entry
- Dynamic subject count support
- Marks validation (0–100)
- Automatic total and percentage calculation
- Grade assignment system
- Pass/Fail status evaluation
- Detailed result summary
- Exception handling
- Modular function-based design

## Concepts Used
- Functions
- Loops
- Conditional Statements
- Exception Handling
- Lists
- Dictionaries
- String Manipulation
- User Input Handling
- Data Validation
- Mathematical Operations
- Return Values
- Program Flow Control

## Example:

### Input
```text
Enter student full name: Rahul Kumar
Enter class: 10
Enter roll number: 101

Enter the marks for ENGLISH: 90
Enter the marks for MATHEMATICS: 95
Enter the marks for SCIENCE: 85
Enter the marks for SOCIAL: 88
Enter the marks for HINDI: 92
Enter the marks for TELUGU: 87
```

### Output
```text
================================
  🎓    STUDENT  RESULTS    🎓
=================================
Name   : RAHUL KUMAR
Class   : 10
Roll No : 101
=========Marks Summary==========

ENGLISH : 90
MATHEMATICS : 95
SCIENCE : 85
SOCIAL : 88
HINDI : 92
TELUGU : 87

----------------------------------
Total    : 537 / 600
Percentage : 89.5%
Grade : A
Status : PASS 🎉
==============================

Congratulations RAHUL KUMAR! 🎉
```

## Project Structure
```text
Python_Beginner_Projects/
│
├── guess_the_number.py
├── student_grade_calculator.py
└── README.md
```
## Technologies Used
- Python 3
- VS Code 
- Git & GitHub

## How to Run the Code
1. Clone the repository.

```bash
git clone <repository-url>
```

2.  Navigate to the project folder.

```bash
cd Python-Beginner-Projects
```

3. Run the Python file.

```bash
python guess_the_number.py
```
```bash
python student_grade_system.py
```

## Author

- **NAME**: Shaik Nasreen

- **GitHub**: https://github.com/ShaikNasreenNov25
