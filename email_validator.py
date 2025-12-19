import re

def validate_gmail(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    return bool(re.match(pattern, email))