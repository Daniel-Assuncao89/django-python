import re

email = input("What's your email? ").strip()

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")
# ------------------------------------------------
# re.search(pattern, string, flags=0)
"""
Regular expressions
. = any character excpet a newline
* = 0 or more repetitions
+ = 1 or more repetitions
? = 0 or 1 repetition
{m} = m repetitions
{m, n} = m-n repetitions
^ = matches the start of the string
$ = matches the end of the string or just before the newline at the end of the string
[] = set of characters that you want to allowed
[^] = complementing the set
A|B = either A or B
(...) = a group
(?:...) = non-capturing version
\d = decimal digit(0-9)
\D = not a decimal digit
\s = whitespaces characters
\S = not a whitespace character
\w = word character, as well as numbers and underscore
\W = not a word character
[a-zA-Z0-9_] = tbm pode ser representado por \w (any word character)
"""

if re.search(r"^\w+@\w+\.(edu|gov|com|gov)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
