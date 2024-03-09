def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    zigzag = [''] * numRows
    index, step = 0, 1

    for char in s:
        zigzag[index] += char
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step

    return ''.join(zigzag)

# Take user input
s = input("Enter the string: ")
numRows = int(input("Enter the number of rows: "))

# Call the convert function and print the result
print(convert(s, numRows))
