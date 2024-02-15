def find_triplet(arr, target_sum):
    n = len(arr)
    arr.sort()

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target_sum:
                return arr[i], arr[left], arr[right]
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1

    return None

# Take user input for array elements
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

# Take user input for the target sum
target_sum = int(input("Enter the target sum: "))

result = find_triplet(arr, target_sum)

if result:
    print("Triplet found:", result)
else:
    print("No triplet found for the given sum.")
