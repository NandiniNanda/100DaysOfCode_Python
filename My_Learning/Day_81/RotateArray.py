def rotate(nums, k):
    # Calculate effective rotation amount
    k = k % len(nums)
    
    # Rotate the array using array slicing
    nums[:] = nums[-k:] + nums[:-k]

# Test cases
nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
rotate(nums1, k1)
print(nums1)  # Output: [5, 6, 7, 1, 2, 3, 4]

nums2 = [-1, -100, 3, 99]
k2 = 2
rotate(nums2, k2)
print(nums2)  # Output: [3, 99, -1, -100]
