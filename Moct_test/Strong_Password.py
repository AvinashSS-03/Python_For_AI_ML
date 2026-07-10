#write a program to validate strong password
#minumum 8 length and 1 uppercaase 1 lowercase 1 digit and 1 spexial character
from mysql.connector.constants import flag_is_set

password=input("Enter the Password: ")
n=len(password)
has_upper=False
has_lower=False
has_digit=False
has_special=False
for ch in password:
    if ch.isdigit():
        has_digit=True

    elif ch.isupper():
        has_upper=True
    elif ch.islower():
        has_lower=True
    else:
        
        has_special = True
if n>8 and has_lower and has_upper and has_special and has_digit:
    print("It is a Strong Password")
else:
    print("Weak")