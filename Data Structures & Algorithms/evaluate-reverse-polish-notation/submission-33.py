class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-','*','/']

        for item in tokens:
            if item not in operators:
                stack.append(item)
            elif item == '+':
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                val = val1 + val2 
                stack.append(val)
            elif item == '*':
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                val = val1 * val2
                stack.append(val)
            elif item == '-':
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                val = val2 - val1
                stack.append(val)
            elif item == '/':
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                val = int(val2/val1)
                stack.append(val)
        
        return int(stack[-1])
