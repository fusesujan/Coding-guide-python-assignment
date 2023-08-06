'''
Create a function that validates email addresses based on following set of rules:
- Proper email format such as presence of “@”, no space in the address
- Presence of valid email providers such as yahoo, gmail and outlook. Make sure
there are no no disposable email providers such as yopmail.
Write unit tests to validate different email addresses against the rules, including valid and
invalid addresses (Use unittest module).

'''

import re
import unittest

def validate_email_address(email):
    # Regular expression for email validation
    email_regex = r'^[a-zA-Z0-9._%+-]+@(yahoo|gmail|outlook)\.[a-zA-Z]{2,}$'

    # Check if the email matches the regular expression
    if re.match(email_regex, email):
        # Check for disposable email providers (yopmail)
        if 'yopmail' not in email:
            return True
    return False

# Unit tests for the validate_email_address function
class TestEmailValidation(unittest.TestCase):
    def test_valid_emails(self):
        valid_emails = [
            'john.doe@gmail.com',
            'jane_smith@yahoo.com',
            'user123@outlook.com',
            'user123@gmail.org',
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(validate_email_address(email))

    def test_invalid_emails(self):
        invalid_emails = [
            'invalid_email',
            'user name@gmail.com',
            'john.doe@yopmail.com',
            'user@unknown.com',
            'user123@yahoo.com.uk',
            'jane_smith@gmmail.com',
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(validate_email_address(email))

if __name__ == '__main__':
    unittest.main()
