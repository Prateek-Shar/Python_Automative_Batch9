from number_validator import validate_number 
from email_validator  import validate_gmail

email = input("Enter the email : ")
contact = (input("Enter the number : "))

#Calling Email Validator Function
if validate_number(contact):
   print("The number is valid")

else:
   print("Number is not valid")


#Calling Number Validator Function
if validate_gmail(email):
   print("Email is valid")

else: 
   print("Email not valid")