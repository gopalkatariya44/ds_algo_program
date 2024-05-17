class Solution:
    @staticmethod
    def calculate(s: str) -> int:
        stack = []
        operand = 0
        result = 0
        sign = 1

        for char in s:
            if char.isdigit():
                operand = (operand * 10) + int(char)
            elif char == "+":
                result += sign * operand
                operand = 0
                sign = 1
            elif char == '-':
                result += sign * operand
                operand = 0
                sign = -1
            elif char == "(":
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif char == ")":
                result += sign * operand
                operand = 0
                result *= stack.pop()
                result += stack.pop()
        return result + (sign * operand)


if __name__ == '__main__':
    obj = Solution()
    # Test cases
    print(obj.calculate("1 + 1"))  # Output: 2
    print(obj.calculate(" 2-1 + 2 "))  # Output: 3
    print(obj.calculate("(1+(4+5+2)-3)+(6+8)()"))  # Output: 23
