def isMatch(s, p):
    if not p:
        return not s

    first_match = bool(s) and p[0] in {s[0], '.'}

    if len(p) >= 2 and p[1] == '*':
        return (isMatch(s, p[2:]) or
                first_match and isMatch(s[1:], p))
    else:
        return first_match and isMatch(s[1:], p[1:])

# Take user input for the input string s and pattern p
s = input("Enter the input string s: ")
p = input("Enter the pattern string p: ")

# Check if the input string matches the pattern
result = isMatch(s, p)
print("Output:", result)

