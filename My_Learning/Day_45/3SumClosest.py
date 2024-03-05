def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    n = len(nums)

    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return target  # Found exact match, no need to continue
    return closest_sum

# Test the function
nums1 = [-1, 2, 1, -4]
target1 = 1
print(threeSumClosest(nums1, target1))  # Output: 2

nums2 = [0, 0, 0]
target2 = 1
print(threeSumClosest(nums2, target2))  # Output: 0
