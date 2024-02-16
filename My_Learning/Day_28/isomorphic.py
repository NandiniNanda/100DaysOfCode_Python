def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    mapping_s_to_t = {}
    mapping_t_to_s = {}
    
    for char_s, char_t in zip(s, t):
        if char_s not in mapping_s_to_t:
            mapping_s_to_t[char_s] = char_t
        else:
            if mapping_s_to_t[char_s] != char_t:
                return False
        
        if char_t not in mapping_t_to_s:
            mapping_t_to_s[char_t] = char_s
        else:
            if mapping_t_to_s[char_t] != char_s:
                return False
    
    return True

# Take user input for strings s and t
s = input("Enter the first string (s): ")
t = input("Enter the second string (t): ")

# Call the function and print the result
print("Output:", isIsomorphic(s, t))
