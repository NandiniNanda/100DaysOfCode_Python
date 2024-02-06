import math

def getPermutation(n, k):
    nums = list(range(1, n + 1))
    k -= 1
    ans = ""
    for i in range(n, 0, -1):
        index = k // math.factorial(i - 1)
        k %= math.factorial(i - 1)
        ans += str(nums[index])
        nums.pop(index)
    return ans

# Take user input for n and k
n = int(input("Enter the value of n: "))
k = int(input("Enter the value of k: "))

# Calculate and print the result
result = getPermutation(n, k)
print("Output:", result)

