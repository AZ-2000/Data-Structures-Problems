class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        for i in range(len(self.s1)-1):
            self.s2.append(self.s1.pop())
        popped_val = self.s1.pop()
        for value in reversed(self.s2):
            self.s1.append(value)
        self.s2 = []
        return popped_val
    def peek(self) -> int:
        for i in range(len(self.s1)-1):
            self.s2.append(self.s1.pop())
        popped_val = self.s1.pop()
        self.s1.append(popped_val)
        for value in reversed(self.s2):
            self.s1.append(value)
        self.s2 = []
        return popped_val
        
        

    def empty(self) -> bool:
        if not self.s1:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()