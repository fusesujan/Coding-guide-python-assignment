'''
Write a Python program that takes two integers as input and performs division (num1
/ num2). Handle both ValueError (if non-integer input) and ZeroDivisionError and
display appropriate error messages.

'''


class WeakPasswordError(Exception):
    """
    Custom exception to handle weak passwords (passwords shorter than 8 characters).
    """

    def __init__(self, message="Weak password! Password should be at least 8 characters long."):
        self.message = message
        super().__init__(self.message)


def check_password_strength(password: str) -> None:
    """
    Check the strength of the password and raise WeakPasswordError if it's weak.

    Args:
        password (str): The password entered by the user.

    Raises:
        WeakPasswordError: If the password is shorter than 8 characters.
    """
    if len(password) < 8:
        raise WeakPasswordError()


try:
    pass_word = input("Enter your password: ")
    check_password_strength(pass_word)
    print("Password is strong and accepted!")
except WeakPasswordError as e:
    print(e.message)
