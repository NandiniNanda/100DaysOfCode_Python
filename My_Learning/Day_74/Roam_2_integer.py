def romanToInt(s: str) -> int:
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    
    for char in s:
        current_value = roman_dict[char]
        if current_value > prev_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value
        prev_value = current_value
        
    return total

# Take user input
user_input = input("Enter a Roman numeral: ")
print("Integer value:", romanToInt(user_input))
