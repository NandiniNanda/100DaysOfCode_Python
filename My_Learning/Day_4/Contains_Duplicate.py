import array

def containsDuplicate(nums):
    nums = sorted(nums)  # Sort the array in ascending order

    # Check for duplicates
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True

    # No duplicates found
    return False

# Take user input for the integer array
user_input = input("Enter integers separated by spaces: ")
nums_array = array.array('i', map(int, user_input.split()))

# Check for duplicates and print the result
result = containsDuplicate(nums_array)
print("Output:", result)


