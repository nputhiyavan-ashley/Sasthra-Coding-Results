password = input()

score = 0
failed = []

# Rule 1: Minimum Length
if len(password) >= 8:
    score += 1
else:
    failed.append("length")

# Rule 2: Uppercase Letter
if any(ch.isupper() for ch in password):
    score += 1
else:
    failed.append("uppercase")

# Rule 3: Lowercase Letter
if any(ch.islower() for ch in password):
    score += 1
else:
    failed.append("lowercase")

# Rule 4: Digit
if any(ch.isdigit() for ch in password):
    score += 1
else:
    failed.append("digit")

# Rule 5: Special Character
special = "!@#$%^&*()_+-=[]{};:'\",.<>?/|`~"

if any(ch in special for ch in password):
    score += 1
else:
    failed.append("special")

# Rule 6: No Spaces
if " " not in password:
    score += 1
else:
    failed.append("space")

# Final Output
if score == 6:
    print("VALID score:6")
else:
    print("INVALID:" + ",".join(failed) + " score:" + str(score))
