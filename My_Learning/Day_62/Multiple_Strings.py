def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    m, n = len(num1), len(num2)
    result = [0] * (m + n)

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            total = mul + result[i + j + 1]
            result[i + j] += total // 10
            result[i + j + 1] = total % 10

    start = 0
    while start < len(result) and result[start] == 0:
        start += 1

    return ''.join(map(str, result[start:]))


# Test cases
num1 = input("Enter num1: ")
num2 = input("Enter num2: ")
print("Output:", multiply(num1, num2))
