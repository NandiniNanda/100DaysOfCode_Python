def is_palindrome(s):
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())

    # Check if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]

# Take user input
user_input = input("Enter a string: ")

# Check if the input is a palindrome
result = is_palindrome(user_input)

# Display the result
print("Output:", result)
