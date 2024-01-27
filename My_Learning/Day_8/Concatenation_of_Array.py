def concatenate_array(nums):
    n = len(nums)
    ans = nums + nums  # Concatenate the array with itself
    return ans

# Take user input for the array
user_input = input("Enter integers separated by space: ")
nums = list(map(int, user_input.split()))

# Create the concatenated array
result = concatenate_array(nums)

# Display the result
print("Output:", result)
