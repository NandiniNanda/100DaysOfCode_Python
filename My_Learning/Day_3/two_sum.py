def twosum(nums, target):
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                return [i, j]

# Take user input for nums
nums_input = input("Enter a list of numbers separated by spaces: ")
nums = [int(num) for num in nums_input.split()]

# Take user input for target
target = int(input("Enter the target sum: "))

result = twosum(nums, target)
if result:
    print(f"Indices of the two numbers that add up to {target}: {result}")
else:
    print("No solution found.")
