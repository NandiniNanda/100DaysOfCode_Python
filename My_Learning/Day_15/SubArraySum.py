def subarray_sum(nums, k):
    count = 0
    sum_so_far = 0
    sum_count = {0: 1}  # To keep track of the sum and its count

    for num in nums:
        sum_so_far += num
        if sum_so_far - k in sum_count:
            count += sum_count[sum_so_far - k]

        if sum_so_far in sum_count:
            sum_count[sum_so_far] += 1
        else:
            sum_count[sum_so_far] = 1

    return count

# Take user input for an array of integers
user_input_nums = input("Enter a list of integers separated by space: ")
nums = list(map(int, user_input_nums.replace(',', ' ').split()))

# Take user input for the target sum k
k = int(input("Enter the target sum k: "))

# Calculate and print the result
result = subarray_sum(nums, k)
print("Output:", result)

