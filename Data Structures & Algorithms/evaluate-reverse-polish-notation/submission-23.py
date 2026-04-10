class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op_list = ["+","-","*","/"]
        for i in range(len(tokens)):
            if tokens[i] not in op_list:
                stack.append(int(tokens[i]))

            elif tokens[i] in op_list and tokens[i] == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
    
            elif tokens[i] in op_list and tokens[i] == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
                
            elif tokens[i] in op_list and tokens[i] == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
                
            elif tokens[i] in op_list and tokens[i] == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
        return stack[-1]
                
                

               