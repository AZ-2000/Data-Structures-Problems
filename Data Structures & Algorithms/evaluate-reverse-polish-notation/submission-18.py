class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        op_list = ["*","-","/","+"]
        if len(tokens) == 1:
            return int(tokens[0])

        for i in range(len(tokens)):
            if tokens[i] not in op_list:
                num_stack.append(tokens[i])
            elif tokens[i] in op_list:
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
            # elif tokens[i] in op_list and res_stack:
            #     print(res_stack)
            #     op = tokens[i]
            #     if op == "*":
            #         a = res_stack.pop()
            #         b = int(num_stack.pop())
            #         res_stack.append(a*b)
            #     elif op == "+":
            #         a = res_stack.pop()
            #         b = int(num_stack.pop())
            #         res_stack.append(a+b)
            #     elif op == "-":
            #         a = res_stack.pop()
            #         b = int(num_stack.pop())
            #         if str(b) == tokens[i-1]:
            #             res_stack.append(a-b)
            #         else:
            #             res_stack.append(b-a)
            #     elif op == "/":
            #         a = res_stack.pop()
            #         b = int(num_stack.pop())
            #         res_stack.append(int(b/a))
        return num_stack[-1]
