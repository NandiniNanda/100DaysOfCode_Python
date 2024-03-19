def combinationSum(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            backtrack(i, target - candidates[i], path + [candidates[i]])

    result = []
    candidates.sort()
    backtrack(0, target, [])
    return result

# Example usage:
candidates1 = [2, 3, 6, 7]
target1 = 7
print(combinationSum(candidates1, target1))  # Output: [[2, 2, 3], [7]]

candidates2 = [2, 3, 5]
target2 = 8
print(combinationSum(candidates2, target2))  # Output: [[2, 2, 2, 2], [2, 3, 3], [5]]

candidates3 = [2]
target3 = 1
print(combinationSum(candidates3, target3))  # Output: []
