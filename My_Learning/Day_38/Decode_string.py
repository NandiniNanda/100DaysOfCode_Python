def decodeString(s):
    stack = []
    curr_str = ""
    k = 0
    
    for char in s:
        if char.isdigit():
            k = k * 10 + int(char)
        elif char.isalpha():
            curr_str += char
        elif char == '[':
            stack.append((curr_str, k))
            curr_str = ""
            k = 0
        elif char == ']':
            prev_str, prev_k = stack.pop()
            curr_str = prev_str + curr_str * prev_k
    
    return curr_str

# Take user input
s = input("Enter the encoded string: ")
decoded_string = decodeString(s)
print("Decoded string:", decoded_string)
