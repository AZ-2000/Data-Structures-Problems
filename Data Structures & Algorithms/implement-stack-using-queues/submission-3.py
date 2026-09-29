from collections import deque as queue
class MyStack:
    def __init__(self):
        self.q1 = queue()
        self.q2 = queue()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        for i in range(len(self.q1)-1):
            self.q2.append(self.q1.popleft())
        popped_val = self.q1.popleft()
        for value in self.q2:
            self.q1.append(value)
        self.q2 = queue()
        return popped_val
        
        

    def top(self) -> int:
        for i in range(len(self.q1)-1):
            self.q2.append(self.q1.popleft())
        popped_val = self.q1.popleft()
        for value in self.q2:
            self.q1.append(value)
        self.q1.append(popped_val)
        self.q2 = queue()
        return popped_val


        

    def empty(self) -> bool:
        if not self.q1:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()