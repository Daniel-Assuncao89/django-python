import re
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
"""
name = input("What's yoour name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    # last, first = matches.groups()
    # name = f"{first} {last}"
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
