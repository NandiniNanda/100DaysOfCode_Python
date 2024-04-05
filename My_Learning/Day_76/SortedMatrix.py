def kthSmallest(matrix, k):
    n = len(matrix)
    left, right = matrix[0][0], matrix[n - 1][n - 1]

    def count_less_equal(mid):
        count = 0
        row, col = n - 1, 0
        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                count += row + 1
                col += 1
            else:
                row -= 1
        return count

    while left < right:
        mid = left + (right - left) // 2
        count = count_less_equal(mid)
        if count < k:
            left = mid + 1
        else:
            right = mid

    return left

# Example usage:
matrix1 = [
    [1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
]
k1 = 8
print(kthSmallest(matrix1, k1))  # Output: 13

matrix2 = [[-5]]
k2 = 1
print(kthSmallest(matrix2, k2))  # Output: -5
