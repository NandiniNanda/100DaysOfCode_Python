def compareVersion(version1, version2):
    # Split the versions into their respective parts
    parts1 = version1.split('.')
    parts2 = version2.split('.')
    
    # Compare revisions
    for i in range(max(len(parts1), len(parts2))):
        # Get the integer value of the revision (or treat missing revisions as 0)
        num1 = int(parts1[i]) if i < len(parts1) else 0
        num2 = int(parts2[i]) if i < len(parts2) else 0
        
        # Compare the integer values
        if num1 < num2:
            return -1
        elif num1 > num2:
            return 1
    
    # All revisions compared are equal, compare lengths of revision arrays
    if len(parts1) > len(parts2):
        return 1
    elif len(parts1) < len(parts2):
        return -1
    
    # If no difference found, return 0
    return 0

# Test cases
print(compareVersion("1.01", "1.001"))  # Output: 0
print(compareVersion("1.0", "1.0.0"))   # Output: 0
print(compareVersion("0.1", "1.1"))     # Output: -1
