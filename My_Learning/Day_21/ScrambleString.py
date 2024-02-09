def isScramble(s1, s2):
    if s1 == s2:
        return True
    if sorted(s1) != sorted(s2):
        return False
    n = len(s1)
    for i in range(1, n):
        if (isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:])) or \
           (isScramble(s1[:i], s2[-i:]) and isScramble(s1[i:], s2[:-i])):
            return True
    return False

# Take user input for the strings s1 and s2
s1 = input("Enter the first string s1: ")
s2 = input("Enter the second string s2: ")

# Check if s2 is a scrambled string of s1
result = isScramble(s1, s2)
print("Output:",result)