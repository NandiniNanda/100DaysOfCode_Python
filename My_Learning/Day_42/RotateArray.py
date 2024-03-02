def rotate(nums, k):
    n = len(nums)
    k %= n
    
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)

# Example usage:
nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
nums2 = [-1, -100, 3, 99]
k2 = 2

rotate(nums1, k1)
rotate(nums2, k2)

print("Output for nums1:", nums1)  # Output: [5, 6, 7, 1, 2, 3, 4]
print("Output for nums2:", nums2)  # Output: [3, 99, -1, -100]
