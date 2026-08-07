class Node:
    def __init__(self,val = None, next = None):
        self.val = val
        self.next = next

class MinStack:

    def __init__(self):
        self.head = None 
        self.minima = None
        self.prev_minima = []

    def push(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.minima = new_node.val
        else:
            curr = self.head
            new_node.next = self.head
            self.head = new_node
            if new_node.val <= self.minima:
                self.prev_minima.append(self.minima)
                self.minima = new_node.val


    def pop(self) -> None:
        next_node = self.head.next
        if self.head.val == self.minima:
            if self.prev_minima:
                self.minima = self.prev_minima[-1]
                self.prev_minima.pop()
        self.head.next = None
        self.head = next_node

    def top(self) -> int:
        return self.head.val
        

    def getMin(self) -> int:
        return self.minima
        
