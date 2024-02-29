def combinationSum2(candidates, target):
    candidates.sort()
    result = []
    
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            backtrack(i + 1, target - candidates[i], path + [candidates[i]])
    
    backtrack(0, target, [])
    return result

# Example usage:
candidates1 = [10, 1, 2, 7, 6, 1, 5]
target1 = 8
candidates2 = [2, 5, 2, 1, 2]
target2 = 5

print("Output for candidates1 and target1:", combinationSum2(candidates1, target1))
print("Output for candidates2 and target2:", combinationSum2(candidates2, target2))
