# Student Management System

A simple **Student Management System built in Python** using Object-Oriented Programming (OOP) concepts.

The project is designed to demonstrate the **four pillars of OOP** while providing basic student record management functionality through a command-line interface.

## Features

The system provides the following operations:

* Add a student record
* View all student records
* Search for a student by Roll Number
* Update a student record
* Remove a student record
* Delete all student records
* Exit the application

## OOP Concepts Used

This project demonstrates the four fundamental pillars of Object-Oriented Programming.

### 1. Encapsulation

Student information is stored using private attributes such as:

```python
self.__name
self.__age
self.__rollNo
self.__dept
self.__section
self.__cgpa
```

`@property` and setter methods are used to control access to the data.

### 2. Inheritance

The `Student` class inherits from the `Person` class:

```python
class Student(Person):
```

This allows `Student` to reuse the common attributes and functionality of `Person`.

### 3. Abstraction

The `Person` class can be implemented as an abstract class using Python's `ABC` module and `@abstractmethod`.

```python
from abc import ABC, abstractmethod
```

The `displayInfo()` method defines behavior that the child class must implement.

### 4. Polymorphism

The `Student` class provides its own implementation of the `displayInfo()` method defined by the parent class.

```python
def displayInfo(self):
    ...
```

This demonstrates polymorphism because the same method can have different implementations in different classes.

## Student Information

Each student record contains:

* Name
* Roll Number
* Age
* Department
* Section
* CGPA

## Project Structure

The complete project is contained in a single Python file:

```text
Student-Management-System/
│
├── SMS.py
└── README.md
```

## Technologies Used

* Python 3
* Object-Oriented Programming
* Python `abc` module
* Command Line Interface (CLI)

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project directory

```bash
cd Student-Management-System
```

### 3. Run the program

```bash
python SMS.py
```

## Application Menu

When the program starts, the following menu is displayed:

```text
==============================
   STUDENT MANAGEMENT SYSTEM
==============================

1. Add Student
2. View All
3. Search by Roll #
4. Update Record
5. Remove a Record
6. Delete All
7. Exit
```

## Important Note

The current version stores student records **temporarily in a Python list**.

Therefore, all records are lost when the program is closed.

This project currently focuses on demonstrating **Python OOP concepts and basic CRUD operations**, rather than permanent data storage.

## Future Improvements

Possible future improvements include:

* Input validation
* Duplicate Roll Number validation
* Persistent data storage using JSON
* SQLite database integration
* Better command-line formatting
* Exception handling for invalid user input

## Author

**M Umer Shahzad**


Student Management System — Python OOP Project
