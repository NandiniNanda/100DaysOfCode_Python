def group_anagrams(strs):
    anagrams = {}
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    
    return list(anagrams.values())

# Taking user input
user_input = input("Enter a list of strings separated by space: ")
strs = user_input.split()

# Grouping anagrams
result = group_anagrams(strs)

# Displaying the result
print("Output:", result)
