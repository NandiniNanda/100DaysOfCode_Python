def findPeakElement(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left

# Example usage:
nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 1, 3, 5, 6, 4]
print("Peak index in nums1:", findPeakElement(nums1))  # Output: 2
print("Peak index in nums2:", findPeakElement(nums2))  # Output: 5
