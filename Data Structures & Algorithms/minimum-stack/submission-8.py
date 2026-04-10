class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            if self.minStack[-1] >= val:
                self.minStack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return 
        else:
            popped = self.stack.pop()
            if self.minStack[-1] == popped:
                self.minStack.pop()
            return popped

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
