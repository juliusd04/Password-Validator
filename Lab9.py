import re

password = input("Password: ")
invalid = "It is recommended that your password is at least 9 characters long "
if len(password) < 9:
    print(invalid)
elif re.search('[0-9]', password) is None:
    print(invalid)
elif re.search('[A-Z]', password) is None:
    print(invalid)
elif re.search('[a-z]', password) is None:
    print(invalid)
elif re.search('[^a-zA-Z0-9]', password) is None:
    print(invalid)
else:

    print("Valid Password")

