import secrets
import string


def generate_string(length):
    # Define the possible characters
    letters = string.ascii_letters
    password = ''
    key = "test"
    chars = list(key)
    # Generate password
    for _ in chars:
        password += secrets.choice(letters)
        
    return password
    
new_password = generate_string(8)
print(new_password)