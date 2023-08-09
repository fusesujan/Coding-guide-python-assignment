## SOLID Principles

1. **Single Responsibility Principle (SRP):**

   - A class should have only one reason to change, i.e., it should have only one responsibility. Use this principle when designing classes to ensure they focus on a single task or responsibility, promoting maintainability and reducing complexity.
   - When Not to Use: Don't over-split responsibilities to create excessive small classes; balance is key.
   - By keeping classes focused, SRP helps improve code organization, makes debugging and maintenance easier, and enhances reusability.

2. **Open/Closed Principle (OCP):**

   - Software entities (classes, modules, functions) should be open for extension but closed for modification. Use when designing systems to allow easy addition of new features without modifying existing code.
   - When Not to Use: Avoid over-engineering by applying OCP prematurely when requirements are uncertain.
   - OCP promotes code stability, reduces risk of introducing bugs, and encourages a modular and extensible architecture.

3. **Liskov Substitution Principle (LSP):**

   - Objects of a superclass should be replaceable with objects of a subclass without affecting correctness. Use when designing class hierarchies to ensure subtype instances can be used interchangeably without unexpected behavior.
   - When Not to Use: Avoid violating LSP by creating subclasses that don't adhere to the contract of their superclass.
   - LSP ensures polymorphism and helps prevent issues when utilizing inheritance, leading to more maintainable and robust code.

4. **Interface Segregation Principle (ISP):**

   - Clients should not be forced to depend on interfaces they do not use; segregate interfaces to be specific to the client's needs. Use when designing interfaces to avoid "fat" interfaces and to prevent clients from implementing unnecessary methods.
   - When Not to Use: Avoid applying ISP if the interfaces are already small and cohesive.
   - ISP promotes better client-specific interfaces, reduces coupling, and enhances flexibility in component design.

5. **Dependency Inversion Principle (DIP):**
   - High-level modules should not depend on low-level modules; both should depend on abstractions. Abstractions should not depend on details; details should depend on abstractions. Use when designing components to decouple high-level and low-level modules and to make code more resilient to changes.
   - When Not to Use: Avoid over-engineering by applying DIP excessively in simple scenarios.
   - DIP facilitates loose coupling, promotes better testability, and allows for easier adaptation to changes in requirements or technology.

Applying these SOLID principles in Python (or any programming language) can lead to more maintainable, flexible, and scalable software systems.

---

## Design patterns

Design patterns are reusable, proven solutions to recurring software design problems, encapsulating best practices and providing structured templates for creating well-organized, maintainable, and efficient code.

They serve as blueprints for solving common challenges in software development by offering established strategies that help improve code quality, enhance system architecture, and promote the creation of scalable and adaptable software systems.

1. **Factory Design Pattern:**
   The Factory Design Pattern is a creational pattern that provides an interface for creating objects in a super class but allows subclasses to alter the type of objects that will be created. Use the Factory pattern when you want to delegate the responsibility of object creation to a separate class, especially when you have multiple subclasses that can be instantiated based on certain conditions or parameters.

   - **When Not to Use:** Avoid using the Factory pattern when object creation logic is straightforward or when you have only one or a few concrete classes to instantiate.

   The Factory pattern enhances code organization, encapsulates object creation, promotes loose coupling, and simplifies the process of adding new subclasses without impacting existing code.

2. **Builder Design Pattern:**
   The Builder Design Pattern is a creational pattern that separates the construction of a complex object from its representation, allowing the same construction process to create different representations. Use the Builder pattern when you need to create complex objects step by step, with optional features, and you want to hide the details of construction from the client code.

   - **When Not to Use:** Avoid using the Builder pattern when object construction is simple and straightforward, or when there's only one way to build the object.

   The Builder pattern improves readability, maintains a clear separation between construction and representation, enables the creation of varied object configurations, and supports future expansion without affecting client code.

3. **Singleton Design Pattern:**
   The Singleton Design Pattern ensures that a class has only one instance and provides a global point of access to that instance. Use the Singleton pattern when you want to ensure that there is only one instance of a class, such as a configuration manager or a database connection, and you need a centralized point of access.

   - **When Not to Use:** Avoid using the Singleton pattern for objects that should have multiple instances or when global state is not necessary.

   The Singleton pattern provides a way to manage shared resources, reduces resource consumption by maintaining a single instance, and offers a controlled way of managing global state within an application.

Understanding and effectively applying these design patterns in Python (or any programming language), you can create more modular, maintainable, and flexible software architectures that are easier to extend, modify, and debug. These patterns offer solutions to common design challenges and promote best practices for structuring your codebase.

---

## Python Coding Conventions

When building the a Python project, adhering to consistent and meaningful naming conventions is essential for creating clean, readable, and maintainable code. This guide outlines the recommended naming practices to follow throughout your coding journey.

### Proper Indentation

- Indent your code using 4 spaces for each level of indentation. Avoid using tabs.

### Maximum Line Length

- Limit each line of code to a maximum of 79 characters.
- For long lines, break them appropriately using parentheses or backslashes for improved readability.

### Prescriptive Naming Conventions

- **Package and Module Names**: Use lowercase letters for package and module names. Separate words with underscores if needed.
- **Class Names**: Use `UpperCaseCamelCase` for class names. Built-in classes generally use lowercase names.
- **Exception Names**: Exception classes should end with "Error" for clarity.
- **Global Variable Names**: Use lowercase letters for global variables. Separate words with underscores.
- **Function and Variable Names**: Use lowercase letters and underscores to separate words for function and variable names.
- **Method Names**: Method names should be in lowercase with words separated by underscores.
- **Instance Variables**: Use lowercase letters and underscores for instance variable names. Begin non-public instance variables with a single underscore.
- **Constants**: Constants should be written in fully capitalized letters, with words separated by underscores.

### Source File Encoding

- Ensure that the source code files have the appropriate encoding declaration, typically placed at the beginning of the file. For example: `# -*- coding: utf-8 -*-`

### Adding NumPy Docstrings

- Each function should be accompanied by a NumPy-style docstring that describes its purpose, parameters, and return values.
- The docstring should provide clear and concise explanations of the function's functionality, inputs, and expected outputs.

By following these coding guidelines, you'll contribute to a well-structured, consistent, and maintainable codebase that's easy for others to collaborate on. Your adherence to these guidelines ensures that your contributions are in line with established best practices, enhancing the overall quality of the project.

---

## Unittest

In software engineering, unittest refers to a testing methodology and framework that focuses on isolating and verifying individual units (such as functions, methods, or classes) of code to ensure they function correctly in isolation.

Also
unittest is a built-in Python testing framework used for writing and executing unit tests to verify the correctness of code components.

Let's say we have a function that adds two numbers:

<pre>
def add_numbers(a, b):
    return a + b
</pre>

Here in order to write unittest for above code is as follow:

<pre>
import unittest

def add_numbers(a, b):
    return a + b

class TestAddNumbers(unittest.TestCase):

    def test_positive_numbers(self):
        result = add_numbers(3, 5)
        self.assertEqual(result, 8)  # Assert that the result is equal to 8

    def test_negative_numbers(self):
        result = add_numbers(-2, -7)
        self.assertEqual(result, -9)  # Assert that the result is equal to -9

    def test_mixed_numbers(self):
        result = add_numbers(10, -3)
        self.assertEqual(result, 7)  # Assert that the result is equal to 7

if __name__ == '__main__':
    unittest.main()

</pre>

---

## Debugging

Debugging in Python refers to the process of identifying and resolving errors, bugs, or unexpected behavior in your code.

It involves analyzing the code execution, inspecting variables, and tracing program flow to pinpoint the root cause of issues. Python provides tools like print statements, debugging libraries, and integrated development environments (IDEs) with features like breakpoints and variable inspection, enabling developers to step through code, track values, and diagnose problems to ensure the code functions as intended.

Effective debugging enhances code quality, accelerates development, and results in more reliable and efficient Python programs.

---

## Linting and code formatting

Linting and code formatting are two essential practices in Python development that contribute to producing clean, readable, and maintainable code.

**Linting:**
Linting involves using specialized tools, often referred to as "linters," to analyze your code for potential errors, inconsistencies, and adherence to coding standards. Linters scan your code for common programming mistakes, such as syntax errors, undefined variables, and stylistic issues.

**Code Formatting:**
Code formatting refers to the consistent and standardized arrangement of code elements (such as indentation, line breaks, spacing, and capitalization) to enhance readability and maintainability. Proper code formatting makes it easier for developers to understand the structure of the code and collaborate effectively.
