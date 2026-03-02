from pathlib import Path
import json

def get_stored_user(path):
    """Get stored user if available."""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None

def get_new_user(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    email = input("What is your email? ")
    location = input("What is your location? ")

    user = {
        'username': username,
        'email': email,
        'location': location
    }
    
    contents = json.dumps(user)
    path.write_text(contents)
    return user

def greet_user():
    """Greet the user by name."""
    path = Path('user.json')
    user = get_stored_user(path)
    if user:
        print(f"Welcome back, {user['username']}!")
        print(f"Your email is {user['email']} and your location is {user['location'].title()}.")
    else:
        user = get_new_user(path)
        print(f"We'll remember you when you come back, {user['username']}!")

greet_user()