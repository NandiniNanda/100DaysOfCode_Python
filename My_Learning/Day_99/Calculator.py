class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        result = 0
        sign = 1
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in ['+', '-']:
                result += sign * num
                num = 0
                sign = 1 if char == '+' else -1
            elif char == '(':
                stack.append((result, sign))
                result = 0
                sign = 1
            elif char == ')':
                prev_result, prev_sign = stack.pop()
                result += sign * num
                result *= prev_sign
                result += prev_result
                num = 0
        
        return result + sign * num

# Example usage
sol = Solution()
print(sol.calculate("1 + 1"))               # Output: 2
print(sol.calculate(" 2-1 + 2 "))           # Output: 3
print(sol.calculate("(1+(4+5+2)-3)+(6+8)")) # Output: 23
