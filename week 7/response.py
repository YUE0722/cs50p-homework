from validator_collection import is_email


if is_email(input("What is your email address? ")):
    print("Valid")
else:
    print("Invalid")
