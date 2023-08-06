'''
Write a Python program that takes two integers as input and performs division
(num1 / num2). Handle the ZeroDivisionError and display a custom error message
when the second number is zero.

'''


def zero_division_errors(num1: int, num2: int) -> float:
    """
    Perform division (num1 / num2) and handle ZeroDivisionError.

    Args:
        num1 (int): The dividend.
        num2 (int): The divisor.

    Returns:
        float: The result of division (num1 / num2).

    Raises:
        ZeroDivisionError: If the second number (divisor) is zero.
    """
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        raise ZeroDivisionError("Error: Division by zero exception occurs.")

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = zero_division_errors(num1, num2)
    print(f"The result of division is: {result}")
except ValueError:
    print("Error: Please enter valid integers.")
except ZeroDivisionError as e:
    print(e)
