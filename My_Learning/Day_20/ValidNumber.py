import re

def isNumber(s):
    pattern = r'^[-+]?\d*\.?\d*(?:[eE][-+]?\d+)?$'
    return bool(re.match(pattern, s.strip()))

# Take user input for the string
s = input("Enter a string: ")

# Check if the input string is a valid number
result = isNumber(s)
print("Output:", result)

