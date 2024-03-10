from typing import List

def largestNumber(nums: List[int]) -> str:
    def compare(x, y):
        return int(y + x) - int(x + y)
    
    nums = [str(num) for num in nums]
    
    nums.sort(key=lambda x: (x[0], x), reverse=True)
    
    result = ''.join(nums)
    
    result = result.lstrip('0')
    
    return result or '0'

# Test cases
nums1 = [10, 2]
nums2 = [3, 30, 34, 5, 9]

print(largestNumber(nums1)) 
print(largestNumber(nums2))  
