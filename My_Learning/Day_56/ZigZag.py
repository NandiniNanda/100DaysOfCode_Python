def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    index, step = 0, 1

    for char in s:
        rows[index] += char
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step

    return ''.join(rows)

# Test cases
print(convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(convert("A", 1))  # Output: "A"
