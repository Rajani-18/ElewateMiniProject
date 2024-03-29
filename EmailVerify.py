import re

def validate_email(email):
    # Define the regex pattern for a valid email address
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Replace dashes with empty string
    email_without_dashes = email.replace('-', '')

    # Check if the modified email matches the pattern
    if re.match(pattern, email_without_dashes):
        return True
    else:
        return False

# Example usage
email_input = input("Enter email address in dash mode: ")
if validate_email(email_input):
    print("Valid email address!")
else:
    print("Invalid email address.")