def is_anagram(s, t):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    t = t.replace(" ", "").lower()

    # Check if the sorted characters of both strings are the same
    return sorted(s) == sorted(t)

# Take user input for two strings
s_input = input("Enter the first string: ")
t_input = input("Enter the second string: ")

# Check if the strings are anagrams
result = is_anagram(s_input, t_input)

# Display the result
print(f"Result: {result}")