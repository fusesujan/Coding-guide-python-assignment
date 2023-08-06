'''
Write a Python program that takes two integers as input and performs division (num1
/ num2). Handle both ValueError (if non-integer input) and ZeroDivisionError and
display appropriate error messages.

'''


def divide_numbers(num1: int, num2: int) -> float:
    """
    Perform division (num1 / num2) and handle ValueError and ZeroDivisionError.

    Args:
        num1 (int): The dividend.
        num2 (int): The divisor.

    Returns:
        float: The result of division (num1 / num2).

    Raises:
        ValueError: If either num1 or num2 is not an integer.
        ZeroDivisionError: If the second number (divisor) is zero.
    """
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError("Error: Both numbers should be integers.")
    
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        raise ZeroDivisionError("Error: Division by zero is not allowed.")

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = divide_numbers(num1, num2)
    print(f"The result of division is: {result}")
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
