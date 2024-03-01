def fourSum(nums, target):
    nums.sort()
    result = []
    
    def threeSum(start, target):
        triplets = []
        for i in range(start, len(nums) - 2):
            if i > start and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return triplets
    
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        triplets = threeSum(i + 1, target - nums[i])
        for triplet in triplets:
            result.append([nums[i]] + triplet)
    
    return result

# Example usage:
nums1 = [1, 0, -1, 0, -2, 2]
target1 = 0
nums2 = [2, 2, 2, 2, 2]
target2 = 8

print("Output for nums1 and target1:", fourSum(nums1, target1))
print("Output for nums2 and target2:", fourSum(nums2, target2))
