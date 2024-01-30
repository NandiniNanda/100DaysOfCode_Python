def reverseString(s):
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Take user input for the array of characters
try:
    input_string = input("Enter a string: ")
    char_array = list(input_string)
    
    # Reverse the string in-place
    reverseString(char_array)

    print("Reversed String:", char_array)
except ValueError:
    print("Invalid input. Please enter a valid string.")
