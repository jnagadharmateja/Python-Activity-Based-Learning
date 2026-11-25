password = input("Password to check: ")
errors = []
if len(password) < 8:
    errors.append("At least 8 characters required")
upper = False
lower = False
digit = False
special = False
for ch in password:
    if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        upper = True
    if ch in "abcdefghijklmnopqrstuvwxyz":
        lower = True
    if ch in "0123456789":
        digit = True
    if ch in "!@#$%":
        special = True
if not upper:
    errors.append("Uppercase letter required")
if not lower:
    errors.append("Lowercase letter required")
if not digit:
    errors.append("Digit required")
if not special:
    errors.append("Special character from !@#$% required")
for i in range(len(password) - 2):
    if password[i] == password[i + 1] and password[i] == password[i + 2]:
        errors.append("Three identical consecutive characters not allowed")
        break
if "password" in password.lower():
    errors.append("Prohibited substring: password")
if "admin" in password.lower():
    errors.append("Prohibited substring: admin")
if len(errors) == 0:
    print("Valid password")
else:
    print("Invalid password:")
    for error in errors:
        print("-", error)
