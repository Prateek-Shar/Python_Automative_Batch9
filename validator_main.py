from number_validator import validate_number 
from email_validator  import validate_gmail

email = "abc@gmail.com"
contact = 9278197524

print(validate_number(contact))
print(validate_gmail(email))