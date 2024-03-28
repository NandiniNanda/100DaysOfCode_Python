def permute(nums):
    def backtrack(current_permutation):
        if len(current_permutation) == len(nums):
            permutations.append(current_permutation[:])  # Make a copy of the permutation
            return

        for num in nums:
            if num not in current_permutation:
                current_permutation.append(num)
                backtrack(current_permutation)
                current_permutation.pop()

    permutations = []
    backtrack([])
    return permutations

# Taking user input
nums = list(map(int, input("Enter distinct integers separated by spaces: ").split()))

# Check if the length of the input array is within the constraint
if 1 <= len(nums) <= 6:
    result = permute(nums)
    print("All possible permutations:", result)
else:
    print("Number of integers must be between 1 and 6.")
