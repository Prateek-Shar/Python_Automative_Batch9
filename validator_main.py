from number_validator import validate_number 
from email_validator  import validate_gmail

email = input("Enter the email : ")
contact = (input("Enter the number : "))

print(validate_number(contact))
print(validate_gmail(email))