def removeDuplicates(nums):
    if not nums:
        return 0
    
    unique_index = 1

    # Iterate through the array to find unique elements
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[unique_index] = nums[i]
            unique_index += 1

    return unique_index

# Take user input for the array of integers
try:
    nums = list(map(int, input("Enter a sorted array of integers separated by space: ").split()))

    # Remove duplicates in-place and get the number of unique elements
    k = removeDuplicates(nums)

    print("Number of unique elements:", k)
    print("Updated array:", nums[:k])
except ValueError:
    print("Invalid input. Please enter a valid sorted array of integers.")
