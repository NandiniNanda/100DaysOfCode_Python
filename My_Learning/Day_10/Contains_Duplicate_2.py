def containsNearbyDuplicate(nums, k):
    num_indices = {}

    for i, num in enumerate(nums):
        if num in num_indices and abs(i - num_indices[num]) <= k:
            return True
        num_indices[num] = i

    return False

# Take user input for nums and k
try:
    nums = list(map(int, input("Enter array nums separated by space: ").split()))
    k = int(input("Enter value for k: "))
    result = containsNearbyDuplicate(nums, k)
    print(f"Result: {result}")
except ValueError:
    print("Invalid input. Please enter valid values.")
