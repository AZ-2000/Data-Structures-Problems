class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        op_list = ["*","-","/","+"]
        if len(tokens) == 1:
            return int(tokens[0])

        for i in range(len(tokens)):
            if tokens[i] not in op_list:
                num_stack.append(tokens[i])
            else:
                op = tokens[i]
                if op == "*":
                    a = int(num_stack.pop())
                    b = int(num_stack.pop())
                    num_stack.append(a*b)
                elif op == "+":
                    a = int(num_stack.pop())
                    b = int(num_stack.pop())
                    num_stack.append(a+b)
                elif op == "-":
                    a = int(num_stack.pop())
                    b = int(num_stack.pop())
                    num_stack.append(b-a)
                elif op == "/":
                    a = int(num_stack.pop())
                    b = int(num_stack.pop())
                    num_stack.append(int(b/a))
            
        return num_stack[-1]
