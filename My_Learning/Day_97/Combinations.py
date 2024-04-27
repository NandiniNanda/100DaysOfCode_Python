from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, k, current):
            if k == 0:
                result.append(current[:])
                return
            for i in range(start, n + 1):
                current.append(i)
                backtrack(i + 1, k - 1, current)
                current.pop()
        
        result = []
        backtrack(1, k, [])
        return result

# Example usage
sol = Solution()
print(sol.combine(4, 2))  # Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(sol.combine(1, 1))  # Output: [[1]]
