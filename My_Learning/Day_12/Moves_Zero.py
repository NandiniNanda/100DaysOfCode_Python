def moveZeroes(nums):
    non_zero_index = 0

    # Move non-zero elements to the beginning
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1

# Take user input for the array of integers
try:
    nums = list(map(int, input("Enter an array of integers separated by space: ").split()))

    # Move 0's to the end in-place
    moveZeroes(nums)

    print("Result:", nums)
except ValueError:
    print("Invalid input. Please enter a valid array of integers.")
