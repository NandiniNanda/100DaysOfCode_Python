def findContentChildren(g, s):
    g.sort()  # Sort the greed factors
    s.sort()  # Sort the sizes of the cookies
    
    content_children = 0
    i = 0  # Pointer for greed factors
    j = 0  # Pointer for sizes of cookies
    
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:  # If the cookie size is greater than or equal to the child's greed factor
            content_children += 1
            i += 1  # Move to the next child
        j += 1  # Move to the next cookie
    
    return content_children

# Test cases
print(findContentChildren([1,2,3], [1,1]))  # Output: 1
print(findContentChildren([1,2], [1,2,3]))  # Output: 2
