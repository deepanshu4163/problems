"""
    Write a function that uses regular expressions to make sure the password
    string it is passed is strong. A strong password is defined as one that is at
    least eight characters long, contains both uppercase and lowercase charac-
    ters, and has at least one digit.
"""


import re
from getpass import getpass         #getpass module for hiding password while entering password

password_input = getpass("enter password:")

if len(password_input) < 8:             #checking if password is atleast 8 char long
    print("length of password must be eqaul to greater than 8")
elif re.search(r'[a-z]+', password_input) == None:      #checking if password contains one or more lowercase letter
    print("there must be one lower case letter")
elif re.search(r'[A-Z]+', password_input) == None:      #checking if password contains one or more uppercase letter
    print("there must be one upper case letter")
elif re.search(r'[0-9]+', password_input) == None:      #checking if password contains one or more digits
    print("there must be one digit in password")
elif re.search(r'[^0-9A-Za-z]+', password_input) == None:   #checking if password contains one or more special character
    print("there must be one special character")
else:                                                   
    print("valid password")                 #if every test is passed than password is strong enough

