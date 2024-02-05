def length_of_last_word(s):
    # Split the string into words using spaces as separators
    words = s.split()

    # Check if there are words in the string
    if len(words) == 0:
        return 0

    # Return the length of the last word
    return len(words[-1])


user_input = input("Enter a string consisting of words and spaces: ")

result = length_of_last_word(user_input)
print("Output:", result)
