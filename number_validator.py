import re

def validate_number(number):
    pattern = r'^[6-9]\d{9}$'
    return bool(re.match(pattern, number))